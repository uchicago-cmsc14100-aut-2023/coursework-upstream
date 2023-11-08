"""
CMSC 14100
Autumn 2022

Test code for Homework #5
"""

import json
import os
import sys
import traceback
import pytest
import helpers

MARK="?"
MINE="X"
NM="-"

# Handle the fact that the test code may not
# be in the same directory as the solution code
sys.path.insert(0, os.getcwd())

# Don't complain about the position of the import
# pylint: disable=wrong-import-position
import board
import board_helpers

from board import ACTIVE_GAME, WON_GAME, LOST_GAME

MODULE = "board"


def test_square_init():
    """
    Do a single test for the class: Square
    """
    steps = [
        "square = board.Square()",
        "str(square)"
    ]
    recreate_msg = helpers.gen_recreate_commands(MODULE, steps)
    try:
        square = board.Square()
        err_msg = helpers.check_result(str(square), NM, recreate_msg)
        if err_msg is not None:
            pytest.fail(err_msg)
    except Exception as e:
        helpers.fail_and_augment_recreate_unexpected_exception(recreate_msg, e)


def test_square_mine():
    """
    Do a single test for the class: Square
    """
    steps = [
        "square = board.Square()",
        "square.set_mine()",
        "square.is_mine()",
    ]
    recreate_msg = helpers.gen_recreate_commands(MODULE, steps)
    try:
        square = board.Square()
        square.set_mine()
        err_msg = helpers.check_result(square.is_mine(), True, recreate_msg)
        if err_msg is not None:
            pytest.fail(err_msg)
        steps.append("square.unset_mine()")
        steps.append("square.is_mine()")
        square.unset_mine()
        err_msg = helpers.check_result(square.is_mine(), False, recreate_msg)
        if err_msg is not None:
            pytest.fail(err_msg)        
    except Exception as e:
        helpers.fail_and_augment_recreate_unexpected_exception(recreate_msg, e)

def test_square_mark():
    """
    Do a single test for the class: Square
    """
    steps = [
        "square = board.Square()",
        "square.set_mark()",
        "square.is_marked()",
        "str(square)"
    ]
    recreate_msg = helpers.gen_recreate_commands(MODULE, steps)
    try:
        square = board.Square()
        square.set_mark()
        err_msg = helpers.check_result(square.is_marked(), True, recreate_msg)
        if err_msg is not None:
            pytest.fail(err_msg)
        err_msg = helpers.check_result(str(square), MARK, recreate_msg)
        if err_msg is not None:
            pytest.fail(err_msg)
        steps.append("square.unset_mark()")
        steps.append("square.is_marked()")
        steps.append("str(square)")
        square.unset_mark()
        err_msg = helpers.check_result(square.is_marked(), False, recreate_msg)
        if err_msg is not None:
            pytest.fail(err_msg)
        err_msg = helpers.check_result(str(square), NM, recreate_msg)
        if err_msg is not None:
            pytest.fail(err_msg)    
    except Exception as e:
        helpers.fail_and_augment_recreate_unexpected_exception(recreate_msg, e)


@pytest.mark.parametrize("i, j", [
    (2,2),
    (3,4),
    (5,5)
])
def test_create(i, j):
    steps = [
        "import board",
        f"board = board.Board({i}, {j})",
    ]
    recreate_msg = helpers.gen_recreate_commands(MODULE, steps)
    try:
        expected_count = i * j
        game_board = board.Board(i, j)
        count = 0
        for row in game_board.board:
            for square in row:
                err_msg = helpers.check_result(str(square), NM, recreate_msg)
                if err_msg is not None:
                    pytest.fail(err_msg)
                count += 1
        assert(count == expected_count)
    except Exception as e:
        helpers.fail_and_augment_recreate_unexpected_exception(recreate_msg, e)

def init_board_helper(board_file, steps):
    if board_file is not None and "," in board_file:
        i, j = (int(v) for v in board_file.split(","))
        steps.append(f"game_board = board.Board({i},{j})")
        game_board = board.Board(i, j)
    else:
        steps.append(f"game_board = board_helpers.board_from_file('{board_file}')")
        game_board = board_helpers.board_from_file(board_file)
    return game_board

def play_move_helper(game_board, steps, test):
    """
    Helper method to run a play move (mark, reveal, set mine) test
    or a check test.

    Inputs:
        steps [list of str]: the steps for recreate
        test [tuple]: the test to run (move, play result, expected square str)

    Returns None or err_msg
    """
    if test[0].startswith("check"):
        i,j = (int(v) for v in test[0].replace("check","").split(","))
    elif test[0].startswith("undo"):
        i,j = (int(v) for v in test[0].replace("undo","").split(","))
        steps.append("game_board.undo_move()")
        game_board.undo_move()
    else:
        steps.append(f"move, location = board_helpers.get_move('{test[0]}')")
        move, location = board_helpers.get_move(test[0])
        steps.append("game_board.play_move(move, location)")
        recreate_msg = helpers.gen_recreate_commands(MODULE, steps)
        actual = game_board.play_move(move, location)
        expected = test[1]
        # Check that the actual result matches the expected result
        err_msg = helpers.check_result(actual, expected, recreate_msg)
        if err_msg is not None:
            return err_msg
        i,j = location
    steps.append(f"str(game_board.board[{i}][{j}])")
    recreate_msg = helpers.gen_recreate_commands(MODULE, steps)
    actual = str(game_board.board[i][j])
    expected = test[2]
    err_msg = helpers.check_result(actual, expected, recreate_msg)
    if err_msg is not None:
        return err_msg
    
    # Check if state test is present
    if len(test) >= 4:
        steps.append(f"game_board.get_game_state()")
        recreate_msg = helpers.gen_recreate_commands(MODULE, steps)
        actual = game_board.get_game_state()
        expected = test[3]
        err_msg = helpers.check_result(actual, expected, recreate_msg)
        if err_msg is not None:
            return err_msg
    return None

play_tests = [
    ( "2,2", [
        ( "m0,0", True, MARK),
        ( "m1,1", True, MARK),
        ( "check0,1", True, NM),
        ( "check1,0", True, NM),
    ] ),
    ( "2,2", [
        ( "m0,0", True, MARK),
        ( "m0,0", False, MARK),
        ( "r0,1", True, "0"),
        ( "r0,1", False, "0"),
    ] ),
    ( "2,2", [
        ( "s0,0", True, NM),
        ( "m0,0", True, MARK),
        ( "r0,1", True, "1"),
        ( "r1,1", True, "1"),
        ( "r1,0", True, "1"),
    ] ),
    ( "2,2", [
        ( "s0,0", True, NM),
        ( "m0,0", True, MARK),
        ( "r0,1", True, "1"),
        ( "r0,0", True, MINE),
    ] ),
    ( "2,2", [
        ( "s0,0", True, NM),
        ( "s0,1", True, NM),
        ( "s1,0", True, NM),
        ( "r1,1", True, "3"),
    ] ),
]
@pytest.mark.parametrize("board_file, moves", play_tests)
def test_play_moves(board_file, moves):
    steps = [
        "import board_helpers",
    ]
    recreate_msg = helpers.gen_recreate_commands(MODULE, steps)
    try:
        game_board = init_board_helper(board_file, steps)
        recreate_msg = helpers.gen_recreate_commands(MODULE, steps)
        for test in moves:
            err_msg = play_move_helper(game_board, steps, test)
            if err_msg is not None:
                pytest.fail(err_msg)
    except Exception as e:
        helpers.fail_and_augment_recreate_unexpected_exception(recreate_msg, e)

undo_tests = [
    ( "2,2", [
        ( "m0,0", True, MARK),
        ( "undo0,0", True, NM),
        ( "m1,1", True, MARK),
        ( "undo1,1", True, NM),
        ( "check0,1", True, NM),
        ( "check1,0", True, NM),
    ] ),
    ( "2,2", [
        ( "r0,1", True, "0"),
        ( "undo0,1", True, NM),
        ( "r0,1", True, "0"),
    ] ),
    ( "2,2", [
        ( "s0,0", True, NM),
        ( "r0,1", True, "1"),
        ( "r1,1", True, "1"),
        ( "r1,0", True, "1"),
        ( "r0,0", True, MINE),
        ( "undo0,0", True, NM),
        ( "undo1,0", True, NM),
        ( "undo1,1", True, NM),
        ( "undo0,1", True, NM),
        ( "undo0,0", True, NM),
        ( "r0,1", True, "0"),
        ( "r1,1", True, "0"),
        ( "r1,0", True, "0"),
        ( "r0,0", True, "0"),
    ] ),
    ( "2,2", [
        ( "s0,0", True, NM),
        ( "s0,1", True, NM),
        ( "s1,0", True, NM),
        ( "r1,1", True, "3"),
        ( "undo1,1", True, NM),
        ( "undo1,0", True, NM),
        ( "r1,1", True, "2"),
    ] ),
    ( "2,2", [
        ( "r0,0", True, "0"),
        ( "s0,1", True, NM),
        ( "check0,0", True, "1"),
        ( "s1,1", True, NM),
        ( "check0,0", True, "2"),
        ( "r1,0", True, "2"),
    ] ),
    ( "2,2", [
        ( "m0,1", True, MARK),
        ( "r0,0", True, "0"),
        ( "r0,0", False, "0"),
        ( "r0,0", False, "0"),
        ( "undo0,0", True, NM),
        ( "check0,0", True, NM),
        ( "check0,1", True, MARK),
        ( "undo0,1", True, NM),
    ] ),
    ( "large.msf", [
        ("undo4,13", True, NM),
        ("undo14,9", True, NM),
    ]),
]
@pytest.mark.parametrize("board_file, moves", undo_tests)
def test_undo_moves(board_file, moves):
    steps = [
        "import board_helpers",
    ]
    recreate_msg = helpers.gen_recreate_commands(MODULE, steps)
    try:
        game_board = init_board_helper(board_file, steps)
        recreate_msg = helpers.gen_recreate_commands(MODULE, steps)
        for test in moves:
            err_msg = play_move_helper(game_board, steps, test)
            if err_msg is not None:
                pytest.fail(err_msg)
    except Exception as e:
        helpers.fail_and_augment_recreate_unexpected_exception(recreate_msg, e)

state_tests = [
    ( "2,2", [
        ( "s0,0", True, NM, ACTIVE_GAME),
        ( "m0,0", True, MARK, ACTIVE_GAME),
        ( "r1,1", True, "1", ACTIVE_GAME),
        ( "r1,0", True, "1", ACTIVE_GAME),
        ( "r0,1", True, "1", WON_GAME),
    ] ),
    ( "2,2", [
        ( "s0,0", True, NM, ACTIVE_GAME),
        ( "r1,1", True, "1", ACTIVE_GAME),
        ( "r0,0", True, MINE, LOST_GAME),
    ] ),
    ( "2,2", [
        ( "s0,0", True, NM, ACTIVE_GAME),
        ( "m0,0", True, MARK, ACTIVE_GAME),
        ( "r0,1", True, "1", ACTIVE_GAME),
        ( "r1,1", True, "1", ACTIVE_GAME),
        ( "r1,0", True, "1", WON_GAME),
        ( "r0,0", False, MARK, WON_GAME),
        ( "r0,0", False, MARK, WON_GAME),
    ] ),
    ( "2,2", [
        ( "s0,0", True, NM, ACTIVE_GAME),
        ( "r1,1", True, "1", ACTIVE_GAME),
        ( "r0,0", True, MINE, LOST_GAME),
        ( "undo0,0", True, NM, ACTIVE_GAME),
        ( "undo1,1", True, NM, ACTIVE_GAME),
        ( "r1,1", True, "1", ACTIVE_GAME),
        ( "r0,0", True, MINE, LOST_GAME),
        ( "undo0,0", True, NM, ACTIVE_GAME),
        ( "m0,0", True, MARK, ACTIVE_GAME),
        ( "r1,1", False, "1", ACTIVE_GAME),
        ( "r1,0", True, "1", ACTIVE_GAME),
        ( "r0,1", True, "1", WON_GAME),
    ] ),
    ( "large.msf", [
        ("m7,0", True, MARK, WON_GAME)
    ]),
    ( "large.msf", [
        ("r7,0", True, MINE, LOST_GAME)
    ]),
]
@pytest.mark.parametrize("board_file, moves", state_tests)
def test_state(board_file, moves):
    steps = [
        "import board_helpers",
    ]
    recreate_msg = helpers.gen_recreate_commands(MODULE, steps)
    try:
        game_board = init_board_helper(board_file, steps)
        recreate_msg = helpers.gen_recreate_commands(MODULE, steps)
        for test in moves:
            err_msg = play_move_helper(game_board, steps, test)
            if err_msg is not None:
                pytest.fail(err_msg)
    except Exception as e:
        helpers.fail_and_augment_recreate_unexpected_exception(recreate_msg, e)



restrict_tests = [
    ( "2,2", [
        ( "s0,0", True, NM),
        ( "s1,1", True, NM),
        ( "r1,0", True, "2"),
        ( "s0,1", False, NM),
    ] ),
    ( "2,2", [
        ( "s0,0", True, NM),
        ( "s1,1", True, NM),
        ( "r1,0", True, "2"),
        ( "s0,1", False, NM),
        ( "undo0,1", True, NM),
        ( "s0,1", True, NM),
    ] ),
]
@pytest.mark.parametrize("board_file, moves", restrict_tests)
def test_restrict(board_file, moves):
    steps = [
        "import board_helpers",
    ]
    recreate_msg = helpers.gen_recreate_commands(MODULE, steps)
    try:

        i, j = (int(v) for v in board_file.split(","))
        steps.append(f"game_board = board.Board({i},{j}, True)")
        game_board = board.Board(i, j, True)
        recreate_msg = helpers.gen_recreate_commands(MODULE, steps)
        for test in moves:
            err_msg = play_move_helper(game_board, steps, test)
            if err_msg is not None:
                pytest.fail(err_msg)
    except Exception as e:
        helpers.fail_and_augment_recreate_unexpected_exception(recreate_msg, e)
