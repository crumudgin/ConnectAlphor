from game import Game
import numpy as np

class connect4(Game):

	"""
	Name: __init__
	Description: constructor of the connect4 class
				 Calls generateBoard with the correct dementions of a 
				 connect 4 board
	Parameters: numpy.matrix values - a matrix representation of the board
	"""
	def __init__(self, values=None):
		super(connect4, self).__init__(6, 7, values)


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

	"""
	Name: legalMoves
	Description: calculates a list of all legal moves that can be performed
				 given this gamestate
	Returns: A list of all legal moves
	"""
	def legalMoves(self):
		return [i for i in range(0, len(self.board[0])) if self.board[0,i] == 0]

	"""
	Name: gameEnd
	Description: calculates if the game is over and who the winner is
				 for connect 4 the winner is whoever has 4 pieces in a
				 row, a tie occurs when the entire board is filled with
				 no winner
	Returns: player num if there is a winner
			 0 if the game is not over yet
	"""
	def gameEnd(self):
		countZero = 0
		for col in range(0, len(self.board)):
			for row in range(0, len(self.board[col])):
				if self.board[col,row] != 0:
					h = self.checkHorizontal(col, row)
					v = self.checkVertical(col, row)
					tl = self.checkDiagonalTopLeftBottomRight(col, row)
					tr = self.checkDiagonalTopRightBottomLeft(col, row)
					if h or v or tl or tr:
						return self.board[col,row]
				else:
					countZero += 1
		if countZero == 0:
			return (1, -1)
		return 0


	"""
	Name checkHorizontal
	Description: checks the a defined number of elements in the row to see
				 if there are "winConditions" in a row of a non zero value
	Parameters: int col - the current column index
				int row - the current row index
				int winCondition - the number of elements that must be
								   checked
	Returns: boolean based on if there were 4 elements in a row on any given
			 row
	"""
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

	"""
	Name checkVertical
	Description: checks the a defined number of elements in the column to see
				 if there are "winConditions" in a column of a non zero value
	Parameters: int col - the current column index
				int row - the current row index
				int winCondition - the number of elements that must be
								   checked
	Returns: boolean based on if there were 4 elements in a column on any given
			 column
	"""
	def checkVertical(self, col, row, winCondition=4):
		if col + winCondition < len(self.board[col]):
			for i in range(1, winCondition+1):
				if self.board[col+i,row] != self.board[col,row]:
					print(self.board[col+i, row], self.board[col, row])
					return False
			return True
		return False

	"""
	Name checkDiagonalTopLeftBottomRight
	Description: checks the a defined number of elements in the diagonal moving
				 from top left to bottom right as follows \. to see if there 
				 are "winConditions" in a diagonal of a non zero value
	Parameters: int col - the current column index
				int row - the current row index
				int winCondition - the number of elements that must be
								   checked
	Returns: boolean based on if there were 4 elements in a row on any given
			 diagonal
	"""
	def checkDiagonalTopLeftBottomRight(self, col, row, winCondition=4):
		if row + winCondition < len(self.board[col]) and col + winCondition < len(self.board):
			for i in range(1, winCondition+1):
				if self.board[col+i,row+i] != self.board[col,row]:
					return False
			return True
		return False

	"""
	Name checkDiagonalToprightBottomLeft
	Description: checks the a defined number of elements in the diagonal moving
				 from top right to bottom left as follows /. to see if there 
				 are "winConditions" in a diagonal of a non zero value
	Parameters: int col - the current column index
				int row - the current row index
				int winCondition - the number of elements that must be
								   checked
	Returns: boolean based on if there were 4 elements in a row on any given
			 diagonal
	"""
	def checkDiagonalTopRightBottomLeft(self, col, row, winCondition=4):
		if row + winCondition < len(self.board[col]) and col + winCondition >= 0:
			for i in range(1, winCondition+1):
				if self.board[col-i,row+i] != self.board[col,row]:
					return False
			return True
		return False


	"""
	Name: move
	Description: updates the board with the given move. This method does not
				 check for legality, and will make any move it is able to 
				 regardless of legality. A piece will be placed at the lowest
				 0 value
	Parameters: int player - the number of the player going (1 or -1 for a 2
							 player game)
				int move - the number representing the space on the board where
						   the move is being placed. For connect 4 this will be
						   a value from 0 - 7 
	"""
	def move(self, player, move):
		col = self.board[:,move]
		lastZero = 0
		for index, i in enumerate(col):
			if i == 0:
				lastZero = index
		self.board[lastZero,move] = player

	"""
	Name: move
	Description: creates a new game object with the current board and then performs
				 the designated move
	Parameters: int player - the number of the player going (1 or -1 for a 2
							 player game)
				int move - the number representing the space on the board where
						   the move is being placed. For connect 4 this will be
						   a value from 0 - 7 
	Returns: a new game object
	"""
	def copyAndMove(self, player, move):
		newGame = connect4(self.x, self.y, self.board)
		newGame.move(player, move)
		return newGame

