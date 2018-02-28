from game import Game
import numpy as np

class connect4(Game):

	def generateBoard(self, values=None):
		if values is None:
			return np.zeros((self.x, self.y))

	def legalMoves(self):
		pass

	def gameEnd(self):
		pass

	def move(self, player, move):
		pass

	def copyAndMove(self, player, move):
		pass

