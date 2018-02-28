from game import Game
import numpy as np

class connect4(Game):
	X = 6
	Y = 7

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
					h = self.checkHorizontal(col, row)
					v = self.checkVertical(col, row)
					tl = self.checkDiagnalTopLeftBottomRight(col, row)
					tr = self.checkDiagnalTopRightBottomLeft(col, row)
					if h or v or tl or tr:
						return self.board[col,row]
		return 0


	def checkHorizontal(self, col, row, winCondition=4):
		if row + winCondition < len(self.board):
			# print(rwinCondition+1)
			for i in range(1, winCondition+1):
				# print(i)
				# print(self.board[col, row+i], self.board[col, row])
				if self.board[col,row+i] != self.board[col,row]:
					# print(self.board[col, row+i], self.board[col, row])
					return False
			return True
		return False

	def checkVertical(self, col, row, winCondition=4):
		# print(col+winCondition)
		# print(len(self.board[col]))
		# print((row + winCondition) < len(self.board[col]))
		if col + winCondition < len(self.board[col]):
			for i in range(1, winCondition+1):
				print(i)
				print(self.board[col+i, row], self.board[col, row])
				if self.board[col+i,row] != self.board[col,row]:
					print(self.board[col+i, row], self.board[col, row])
					return False
			return True
		return False

	def checkDiagnalTopLeftBottomRight(self, col, row, winCondition=4):
		if row + winCondition < len(self.board[col]) and col + winCondition < len(self.board):
			for i in range(1, winCondition+1):
				if self.board[col+i,row+i] != self.board[col,row]:
					return False
			return True
		return False

	def checkDiagnalTopRightBottomLeft(self, col, row, winCondition=4):
		if row + winCondition < len(self.board[col]) and col + winCondition >= 0:
			for i in range(1, winCondition+1):
				if self.board[col-i,row+i] != self.board[col,row]:
					return False
			return True
		return False


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

c = connect4(6,7)
c.move(1, 3)
c.move(-1, 3)
c.move(-1, 3)
c.move(-1, 3)
c.move(-1, 3)
c.move(-1, 3)
print(c.getBoard())
print(c.gameEnd())