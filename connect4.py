from game import Game
import numpy as np

class connect4(Game):

	def generateBoard(self, values=None):
		if values is None:
			return np.zeros((self.x, self.y))

	def legalMoves(self):
		return [i for i in range(0, len(self.board[0])) if self.board[0,i] == 0]

	def gameEnd(self):
		pass

	def move(self, player, move):
		col = self.board[:,move]
		lastZero = 0
		for index, i in enumerate(col):
			if i == 0:
				lastZero = index
		self.board[lastZero,move] = player

	def copyAndMove(self, player, move):
		pass

