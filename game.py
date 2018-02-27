import numpy as np
from abc import ABC

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
		self.board = self.generateBoard(boardValues)

	"""
	Name: generateBoard
	Description: Abstract method detailing a method that generates a 
				 2D game board matrix of shape y,x where x and y are 
				 defined in the class
	Parameters: numpy.matrix - A game board represented as a matrix.
							   If None, the board will be poppulated
							   with 0's
	"""
	@abstractmeathod
	def generateBoard(values):
		pass

	@abstractmeathod
	def legalMoves():
		pass

	@abstractmeathod
	def gameEnd():
		pass

	@abstractmeathod
	def move(player, move):
		pass