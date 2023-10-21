"""
CMSC 14100
Aut 23

Functions for reading and writing minesweeper maps
"""

import os
import sys
import random

CONVERT = {
    "t": True,
    "T": True,
    "1": True,
    1: True,
    "f": False,
    "F": False,
    "0": False,
    0: False,
}

def make_board(rows, cols, expected_random_mines=0, seed=None):
    """
    Make a minesweeper board with the given number of rows and columns.
    Each position will hold a tuple/triple of (is_revealed, is_marked, is_mine)

    Inputs:
        rows [int]: the number of rows
        cols [int]: the number of columns
        expected_random_mines [int]: generate random mines up to this number
        seed [int]: seed for the random number generator
    
    Returns [list[list[tuple(bool, bool, bool)]]]: the board
    """
    board = []
    squares = rows*cols
    if seed is not None:
        random.seed(seed)

    for _ in range(rows):
        new_row = []
        for _ in range(cols):
            if (expected_random_mines > 0 and
                    random.random() < expected_random_mines/squares):
                new_row.append((False, False, True))
                expected_random_mines -= 1
            else:
                new_row.append((False, False, False))
        board.append(new_row)
    return board


def load_board(filename):
    """
    Load a file that is formatted using PPM P3 format.

    Input:
        filename (string): the name of the file containing the image

    Returns: list of lists of colors
    """
    try:
        f = os.path.exists(filename)
    except OSError:
        print(f"Cannot open {filename}")
        sys.exit(1)
    board = []
    with open(filename, "r", encoding="utf-8") as f:
        file_type = f.readline().strip()
        if file_type != "msf":
            print("Wrong file type. This function only loads msf\n",
                file=sys.stderr)
            sys.exit(1)

        width, height = (int(x) for x in f.readline().strip().split())

        for _ in range(height):
            row = []
            vals = f.readline().strip().split()
            assert len(vals) == width
            for v in vals:
                assert len(v) == 3
                cell = (CONVERT[v[0]], CONVERT[v[1]], CONVERT[v[2]])
                row.append(cell)
            board.append(row)
    f.close()
    return board


def write_board(filename, board):
    """
    Write an image to a file in P3 PPM format

    Input:
        filename (string): the name of the file to write
        image (list of lists of colors): the image to write to the file
    """
    with open(filename, "w", encoding="utf-8") as f:
        f.write("msf\n")
        # output width height
        f.write(f"{len(board[0])} {len(board)}\n")
        for row in board:
            for cell in row:
                for tf in cell:
                    if tf:
                        f.write("T")
                    else:
                        f.write("F")
                f.write(" ")
            f.write("\n")
