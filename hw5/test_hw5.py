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


# Handle the fact that the test code may not
# be in the same directory as the solution code
sys.path.insert(0, os.getcwd())

# Don't complain about the position of the import
# pylint: disable=wrong-import-position
import hw5
import board_helpers

MODULE = "hw5"

reveal_tests = [
    ( "five.msf", [
        ( (3,4), 0),
        ( (0,2), 2),
    ] ),
    ( "five.msf", [
        ( (0,0), -1 ),
        ( (3,4), 0),
        ( (0,2), 2),
    ] ),
    ( "five.msf", [
        ( (0,0), -1 ),
        ( (0,0), -2),
        ( (0,0), -2),
    ] ),
    ( "five.msf", [
        ( (0,0), -1 ),
        ( (0,0), -2 ),
        ( (3,4), 0),
        ( (3,4), -2),
        ( (2,2), 3),
        ( (0,2), 2),
    ] ),
    ( "three-four.msf", [
        ( (0,0), 0 ),
        ( (3,0), -2),
        ( (0,2), 0),
        ( (0,2), -2),
        ( (2,0), -1),
        ( (3,2), 1),
    ] ),
    ( "nine.msf", [
        ( (0,0), -2),
        ( (0,0), -2),
        ( (0,0), -2),
        ( (1,1), -1),
        ( (7,3), 8),
        ( (7,3), -2),
        ( (0,8), 0),

    ] ),
]
@pytest.mark.parametrize("board_file, reveals", reveal_tests)
def test_reveal_square(board_file, reveals):
    """
    Do a single test for the function: reveal_square
    """
    steps = [
        "import board_helpers",
        f"board = board_helpers.load_board('{board_file}')",
    ]
    recreate_msg = helpers.gen_recreate_commands(MODULE, steps)
    try:
        board = board_helpers.load_board(board_file)
        for test in reveals:
            steps.append(f"hw5.reveal_square({test[0]}, board)")
            recreate_msg = helpers.gen_recreate_commands(MODULE, steps)
            actual = hw5.reveal_square(test[0], board)
            expected = test[1]

            # Check that the actual result matches the expected result
            err_msg = helpers.check_result(actual, expected, recreate_msg)
            if err_msg is not None:
                pytest.fail(err_msg)
    except Exception as e:
        helpers.fail_and_augment_recreate_unexpected_exception(recreate_msg, e)

count_squares_tests = [
    ("five.msf", 0, 5),
    ("five.msf", 1, 9),
    ("five.msf", 2, 4),
    ("five.msf", 3, 5),
    ("five.msf", 4, 2),
    ("five.msf", 5, 0),
    ("five.msf", 6, 0),
    ("nine.msf", 8, 1),
    ("nine.msf", 7, 0),
    ("nine.msf", 3, 10),
    ("nine.msf", 1, 21),
    ("three-four.msf", 2, 2),
    ("three-four.msf", 0, 4),
    ("three-four.msf", 1, 6),
]
@pytest.mark.parametrize("board_file, count, expected", count_squares_tests)
def test_count_squares(board_file, count, expected):
    """
    Do a single test for the function: count_squares
    """
    steps = [
        "import board_helpers",
        f"board = board_helpers.load_board('{board_file}')",
    ]
    recreate_msg = helpers.gen_recreate_commands(MODULE, steps)
    try:    
        board = board_helpers.load_board(board_file)
        steps.append(f"hw5.count_squares({count}, board)")
        recreate_msg = helpers.gen_recreate_commands(MODULE, steps)
        actual = hw5.count_squares(count, board)

        # Check that the actual result matches the expected result
        err_msg = helpers.check_result(actual, expected, recreate_msg)
        if err_msg is not None:
            pytest.fail(err_msg)
    except Exception as e:
        helpers.fail_and_augment_recreate_unexpected_exception(recreate_msg, e)



zeroes_tests = [
    ("five.msf", 5),
    ("nine.msf", 17),
    ("three-four.msf", 4),
]
@pytest.mark.parametrize("board_file, expected", zeroes_tests)
def test_zero(board_file, expected):
    """
    Do a single test for the function: count_squares
    """
    steps = [
        "import board_helpers",
        f"board = board_helpers.load_board('{board_file}')",
    ]
    recreate_msg = helpers.gen_recreate_commands(MODULE, steps)
    try:    
        board = board_helpers.load_board(board_file)
        steps.append(f"hw5.zero_squares(board)")
        recreate_msg = helpers.gen_recreate_commands(MODULE, steps)
        actual = hw5.zero_squares(board)

        # Check that the actual result matches the expected result
        err_msg = helpers.check_result(actual, expected, recreate_msg)
        if err_msg is not None:
            pytest.fail(err_msg)
    except Exception as e:
        helpers.fail_and_augment_recreate_unexpected_exception(recreate_msg, e)


marked_tests = [
    ("five.msf", 3),
    ("nine.msf", 5),
    ("three-four.msf", 2),
]
@pytest.mark.parametrize("board_file, expected", marked_tests)
def test_count_marked(board_file, expected):
    """
    Do a single test for the function: count_squares
    """
    steps = [
        "import board_helpers",
        f"board = board_helpers.load_board('{board_file}')",
    ]
    recreate_msg = helpers.gen_recreate_commands(MODULE, steps)
    try:    
        board = board_helpers.load_board(board_file)
        steps.append(f"hw5.count_marked(board)")
        recreate_msg = helpers.gen_recreate_commands(MODULE, steps)
        actual = hw5.count_marked(board)

        # Check that the actual result matches the expected result
        err_msg = helpers.check_result(actual, expected, recreate_msg)
        if err_msg is not None:
            pytest.fail(err_msg)
    except Exception as e:
        helpers.fail_and_augment_recreate_unexpected_exception(recreate_msg, e)


checked_marked_tests = [
    ("five.msf", (2,1)),
    ("nine.msf", (3,2)),
    ("three-four.msf", (1,1)),
]
@pytest.mark.parametrize("board_file, expected", checked_marked_tests)
def test_check_marked(board_file, expected):
    """
    Do a single test for the function: count_squares
    """
    steps = [
        "import board_helpers",
        f"board = board_helpers.load_board('{board_file}')",
    ]
    recreate_msg = helpers.gen_recreate_commands(MODULE, steps)
    try:    
        board = board_helpers.load_board(board_file)
        steps.append(f"hw5.check_marked(board)")
        recreate_msg = helpers.gen_recreate_commands(MODULE, steps)
        actual = hw5.check_marked(board)

        # Check that the actual result matches the expected result
        err_msg = helpers.check_result(actual, expected, recreate_msg)
        if err_msg is not None:
            pytest.fail(err_msg)
    except Exception as e:
        helpers.fail_and_augment_recreate_unexpected_exception(recreate_msg, e)

