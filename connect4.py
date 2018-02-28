from game import Game
import numpy as np

class connect4(Game):
	self.X = 6
	self.Y = 7

	"""
	Name: generateBoard
	Description: Generates a connect 4 board (standard size is 6,7) 
	Parameters: numpy.matrix values - a connect 4 game board, if values is 
									  None, the board is initialized as 0's.
									  If values isn't None, the game board 
									  is initialized to values.
	Returns: The game board as either zeros or values
	"""
	def generateBoard(self, values=None):
		if values is None:
			return np.zeros((self.x, self.y))
		#TODO through error if values doesn't match up with specified shape
		return values

	def legalMoves(self):
		return [i for i in range(0, len(self.board[0])) if self.board[0,i] == 0]

	def gameEnd(self):
		for col in range(0, len(self.board)):
			for row in range(0, len(self.board[col])):
				if self.board[col,row] != 0:
					h = checkHorizontal(col, row)
					v = checkVertical(col, row)
					tl = checkDiagnalTopLeftBottomRight(col, row)
					tr = checkDiagnalTopRightBottomLeft(col, row)
					if h or v or tl or tr:
						return self.board[col,row]
		return 0


	def checkHorizontal(col, row, winCondition=4):
		pass

	def checkVertical(col, row, winCondition=4):
		pass

	def checkDiagnalTopLeftBottomRight(col, row, winCondition=4):
		pass

	def checkDiagnalTopRightBottomLeft(col, row, winCondition=4):
		pass

	def move(self, player, move):
		col = self.board[:,move]
		lastZero = 0
		for index, i in enumerate(col):
			if i == 0:
				lastZero = index
		self.board[lastZero,move] = player

	def copyAndMove(self, player, move):
		newGame = connect4(self.x, self.y, self.board)
		newGame.move(player, move)
		return newGame
