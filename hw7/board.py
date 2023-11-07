"""
CMSC 14100
Aut 23

Classes for representing minesweeper boards
All of your work for hw7 should be in this file.
"""
from stack import Stack

# Constants for game state
ACTIVE_GAME = 1
LOST_GAME = 2
WON_GAME = 3

# Constants for game moves
SET_MINE = "s"
REVEAL_SQUARE = "r"
MARK_SQUARE = "m"
UNDO = "undo"
EXIT = "exit"
PLAY_MOVES = [SET_MINE, REVEAL_SQUARE, MARK_SQUARE]

class Square:
    """
    Represents a single square on a game board
    """
    def __init__(self):
        """
        Create a new square. 
        Initially, it is not revealed, not marked, and not a mine.
        All attributes of the Square *must* be private.
        """
        self.__is_revealed = False
        self.__is_marked = False
        self.__is_mine = False
        self.__count = 0


    def __str__(self):
        """
        Returns a string representation of the square.
        
        Return str:
            "-" if the square is not revealed or marked
            "?" if the square is marked
            "X" if the square is revealed and a mine
            the adjacent mine count if the square is revealed and not a mine
        """
        #TODO homework hw7
        return None



class Board:
    """
    Class to represent a game board. This is the primary way to interact with 
    the game.
    """
    def __init__(self, rows, cols, restrict_mine_placement=False):
        """
        Initialize a board with the given number of rows and columns.
        Each position will hold a tuple/triple of (is_revealed, is_marked, is_mine)

        Inputs:
            rows [int]: the number of rows
            cols [int]: the number of columns
            restrict_mine_placement [bool]: if True, once a reveal or 
            mark is played, no more mines can be set.
        """

        # These attributes must remain public
        self.rows = rows
        self.cols = cols
        self.board = [] # list of lists of Squares
        self.restrict_mine_placement = restrict_mine_placement
        # Attribute used for debugging, this will print in the text UI if set.
        self.debug_message = ""

        #TODO homework hw7
        return None

    def play_move(self, move, location):
        """
        Your Docstring Here
        """

        assert isinstance(move, str) and move in PLAY_MOVES
        assert isinstance(location, tuple)
        assert isinstance(location[0], int)
        assert isinstance(location[1], int)

        #TODO homework hw7
        return True
    
    def undo_move(self):
        """
        Your Docstring Here
        """
        #TODO homework hw7
        return None

    def get_game_state(self):
        """
        Returns the state of the current board

        Return int:
            ACTIVE_GAME if the game is still in progress
            LOST_GAME if the player has lost
            WON_GAME if the player has won
        """
        #TODO homework hw7
        return ACTIVE_GAME

