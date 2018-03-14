import numpy as np
import scipy as sc
import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data

mnist = input_data.read_data_sets("MNIST_data/", one_hot=True)

class CNN():

    def __init__(self, learningRate, epochs):
        self.learningRate = learningRate
        self.epochs = epochs
        self.batchSize = 50
        self.minimize = None
        self.y = tf.placeholder(tf.float32, [None, 10])
        self.x = tf.placeholder(tf.float32, [None, 784])
        self.x_shaped = tf.reshape(self.x, [-1, 28, 28, 1])
        self.previousLayer = self.x_shaped

    def createNewConvLayer(self, numInputChannels, numFilters, filterShape, name, nonLiniarity=tf.nn.relu):
        convFiltShape = [filterShape[0], filterShape[1], numInputChannels, numFilters]
        w = tf.Variable(tf.truncated_normal(convFiltShape, stddev=.03), name=name+'_W')
        bias = tf.Variable(tf.truncated_normal([numFilters]), name=name+'_b')

        outLayer = tf.nn.conv2d(self.previousLayer, w, [1, 1, 1, 1], padding='SAME')

        outLayer += bias

        outLayer = nonLiniarity(outLayer)
        self.previousLayer = outLayer
        return outLayer

    def createPoolLayer(self, poolShape):
        ksize = [1, poolShape[0], poolShape[1], 1]
        strides = [1, 2, 2, 1]
        outLayer = tf.nn.max_pool(self.previousLayer, ksize=ksize, strides=strides, padding='SAME')
        self.previousLayer = outLayer
        return outLayer

    def createConnectedLayer(self, x, z, squash, name):
        wd = tf.Variable(tf.truncated_normal([x, z], stddev=.03), name='wd' + name)
        bd = tf.Variable(tf.truncated_normal([z], stddev=0.01), name='bd' + name)
        dense_layer = tf.matmul(self.previousLayer, wd) + bd
        self.previousLayer = squash(dense_layer)
        return dense_layer

    def setNetwork(self, numOfConvs, numOfBlocks, numOfConnects):
        filters = 32
        inputChannels = 1
        counter = 1
        for i in range(0, numOfBlocks):
            for j in range(0, numOfConvs):
                self.createNewConvLayer(inputChannels, filters, [5, 5], str(counter))
                counter += 1
                inputChannels = filters
                filters *= 2
            self.createPoolLayer([2, 2])
        self.previousLayer = tf.reshape(self.previousLayer, [-1, 7*7*filters//2])
        xSize = 7*7*filters//2
        ySize = 1000
        for i in range(0, numOfConnects):
            finalOut = self.createConnectedLayer(xSize, ySize, tf.nn.relu, str(counter))
            xSize = ySize
            ySize = 10
        finalOut = tf.nn.softmax(finalOut)
        self.previousLayer = finalOut
        cross_entropy = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits_v2(logits=finalOut, labels=self.y))
        self.minimize = cross_entropy
        return cross_entropy

    def train(self):
        if self.minimize is None:
            print("you need to set the network first")
            return
        optimiser = tf.train.AdamOptimizer(learning_rate=self.learningRate).minimize(self.minimize)
        correct_prediction = tf.equal(tf.argmax(self.y, 1), tf.argmax(self.previousLayer, 1))
        accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))
        initOptimiser = tf.global_variables_initializer()

        with tf.Session() as sess:
            # initialise the variables
            sess.run(initOptimiser)
            total_batch = int(len(mnist.train.labels) / self.batchSize)
            for epoch in range(self.epochs):
                avg_cost = 0
                for i in range(total_batch):
                    batch_x, batch_y = mnist.train.next_batch(batch_size=self.batchSize)
                    _, c = sess.run([optimiser, self.minimize], 
                                    feed_dict={self.x: batch_x, self.y: batch_y})
                    avg_cost += c / total_batch
                test_acc = sess.run(accuracy, 
                               feed_dict={self.x: mnist.test.images, self.y: mnist.test.labels})
                print("Epoch:", (epoch + 1), "cost =", "{:.3f}".format(avg_cost), " test accuracy: {:.3f}".format(test_acc))

            print("\nTraining complete!")
            print(sess.run(accuracy, feed_dict={self.x: mnist.test.images, self.y: mnist.test.labels}))


c = CNN(.001, 2)
c.setNetwork(1, 2, 2)
c.train()