"""
CMSC 14100
Aut 23

Functions for reading and writing minesweeper maps
DO NOT MODIFY THIS FILE
"""


from board import Board
from board import PLAY_MOVES

def get_move(string):
    """
    Take a move string and return a tuple of the form (move, (row, col))

    Inputs:
        string [str]: a string of the form "[move]row,col" where move is either
            "r" or "m" and row and col are integers

    Return tuple(str (int, int)) or None if invalid move
    """
    if string.count(",") != 1 and string[0].lower() not in PLAY_MOVES:
        return None
    move = string[0].lower()
    row_str, col_str = string[1:].split(",")
    try:
        row = int(row_str)
        col = int(col_str)
        return (move, (row,col))
    except Exception as e:
        print("Error converting row/col ", e)
    return None

def board_from_file(filename):
    """
    A helper function to create a board from a file.
    """
    with open(filename,"r",encoding="utf8") as board_file:
        rows, cols = (int(v) for v in board_file.readline().split(","))
        board = Board(rows, cols)
        for line in board_file:
            move, square = get_move(line.strip())
            board.play_move(move, square)
        return board
    print("Error reading file")
    return None
