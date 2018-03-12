import numpy as np
import scipy as sc
import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data

mnist = input_data.read_data_sets("MNIST_data/", one_hot=True)

learningRate = .0001
epochs = 10
batch_size = 50

x = tf.placeholder(tf.float32, [None, 784])
x_shaped = tf.reshape(x, [-1, 28, 28, 1])
y = tf.placeholder(tf.float32, [None, 10])

def createNewConvLayer(input_data, num_input_channels, num_filters, filter_shape, name):
    conv_filt_shape = [filter_shape[0], filter_shape[1], num_input_channels, num_filters]
    w = tf.Variable(tf.truncated_normal(conv_filt_shape, stddev=.03), name=name+'_W')
    bias = tf.Variable(tf.truncated_normal([num_filters]), name=name+'_b')

    out_layer = tf.nn.conv2d(input_data, w, [1, 1, 1, 1], padding='SAME')

    out_layer += bias

    out_layer = tf.nn.relu(out_layer)
    return out_layer

def createPoolLayer(in_layer, pool_shape):
    ksize = [1, pool_shape[0], pool_shape[1], 1]
    strides = [1, 2, 2, 1]
    out_layer = tf.nn.max_pool(in_layer, ksize=ksize, strides=strides, padding='SAME')
    return out_layer

def createConnectedLayer(flattend, x, z, squash, name):
    wd = tf.Variable(tf.truncated_normal([x, z], stddev=.03), name='wd' + name)
    bd = tf.Variable(tf.truncated_normal([z], stddev=0.01), name='bd' + name)
    dense_layer = tf.matmul(flattend, wd) + bd
    return dense_layer

l1 = createNewConvLayer(x_shaped, 1, 32, [5, 5], 'layer1')
l2 = createPoolLayer(l1, [2,2])
l3 = createNewConvLayer(l2, 32, 64, [5, 5], 'layer3')
l4 = createPoolLayer(l3, [2, 2])
flattend = tf.reshape(l4, [-1, 7*7*64])
l5 = tf.nn.relu(createConnectedLayer(flattend, 7*7*64, 1000, tf.nn.relu, "1"))
l6 = createConnectedLayer(l5, 1000, 10, tf.nn.softmax, "2")
y_ = tf.nn.softmax(l6)
cross_entropy = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits_v2(logits=l6, labels=y))


optimiser = tf.train.AdamOptimizer(learning_rate=learningRate).minimize(cross_entropy)

correct_prediction = tf.equal(tf.argmax(y, 1), tf.argmax(y_, 1))
accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))

init_op = tf.global_variables_initializer()

with tf.Session() as sess:
    # initialise the variables
    sess.run(init_op)
    total_batch = int(len(mnist.train.labels) / batch_size)
    for epoch in range(epochs):
        avg_cost = 0
        for i in range(total_batch):
            batch_x, batch_y = mnist.train.next_batch(batch_size=batch_size)
            _, c = sess.run([optimiser, cross_entropy], 
                            feed_dict={x: batch_x, y: batch_y})
            avg_cost += c / total_batch
        test_acc = sess.run(accuracy, 
                       feed_dict={x: mnist.test.images, y: mnist.test.labels})
        print("Epoch:", (epoch + 1), "cost =", "{:.3f}".format(avg_cost), " test accuracy: {:.3f}".format(test_acc))

    print("\nTraining complete!")
    print(sess.run(accuracy, feed_dict={x: mnist.test.images, y: mnist.test.labels}))
