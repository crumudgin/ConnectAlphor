import numpy as np
from connect4 import connect4

class Monte():

	def __init__(game, net):
		self.game = game
		self.net = net

	def runSearch():
		p, w = self.net.run(self.game)
		moves = [self.game.copyAndMove(1, i) for i in self.game.legalMoves()]
