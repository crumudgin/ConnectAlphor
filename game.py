import numpy as np
from abc import ABC, abstractmethod

"""
Name: Game
Inherits: ABC from abc
Description: An abstract class designed to represent a game played on a 2D board
Notes: This exists as a base class for all 2d board games to be developed with this
	   Network, while currently the scope of this project is limited to connect 4
	   I envision creating other game networks from this same codebase.
Author: Zac Chu
"""
class Game(ABC):
	
	"""
	Name: __init__
	Description: Constructor for the Game class
	Parameters: int boardX				- The x dimension of the game board
				int boardY				- The y dimension of the game board
				numpy.matrix boardValues- A game board represented as a 
										  matrix
	"""
	def __init__(self, boardX, boardY, boardValues=None):
		self.x = boardX
		self.y = boardY
		self.N = 0
		self.W = 0
		self.P = 0
		self.board = self.generateBoard(boardValues)

	"""
	Name: getBoard
	Description: Gets the board so it may be viewed and manipulated without
				 changing the gamestate in this object
	Returns: self.board
	"""
	def getBoard(self):
		return self.board

	"""
	Name: getShape
	Description: Gets the x and y values of the board so they may be viewed
				 and manipulated without changing the gamestate in this
				 object
	Returns: self.x
			 self.y
	"""
	def getShape(self):
		return (self.x, self.y)

	"""
	Name: getN
	Description: returns the N value for outside manipulation without effecting
				 the gamestate
	Returns: N
	"""
	def getN():
		return self.N

	"""
	Name: setN
	Description: sets the N value
	"""
	def setN(n):
		self.N = n

	"""
	Name: getW
	Description: returns the W value for outside manipulation without effecting
				 the gamestate
	Returns: W
	"""
	def getW():
		return self.W
	"""
	Name: setW
	Description: sets the W value
	"""
	def setW(w):
		self.W = w

	"""
	Name: getP
	Description: returns the P value for outside manipulation without effecting
				 the gamestate
	Returns: P
	"""
	def getP():
		return self.P
	"""
	Name: setP
	Description: sets the P value
	"""
	def setP(p):
		self.P = p

	"""
	Name: generateBoard
	Description: Abstract method detailing a method that generates a 
				 2D game board matrix of shape y,x where x and y are 
				 defined in the class
	Parameters: numpy.matrix - A game board represented as a matrix.
							   If None, the board will be populated
							   with 0's
	"""
	@abstractmethod
	def generateBoard(self, values=None):
		pass

	"""
	Name: legalMoves
	Description: Generates a list of all legal moves given the current gamestate
	returns: List of all legal moves
	"""
	@abstractmethod
	def legalMoves(self):
		pass

	"""
	Name: gameEnd
	Description: determines if the game is over
	Returns: Winning player(s) or 0 if the game is not over
	"""
	@abstractmethod
	def gameEnd(self):
		pass

	"""
	Name: move
	Description: Plays the designated move on the game board for the specified player
	Parameters: int player - The player moving
				int move - the move(specified from the legalMoves list)
	"""
	@abstractmethod
	def move(self, player, move):
		pass

	"""
	Name: move
	Description: Plays the designated move on the game board for the specified player
				 and copies the gamestate to a new Game object leaving this object in
				 the state it was prior to this function call
	Parameters: int player - The player moving
				int move - the move(specified from the legalMoves list)
	Returns: A new Game object updated with the current board having the move played on it
	"""
	@abstractmethod
	def copyAndMove(self, player, move):
		pass