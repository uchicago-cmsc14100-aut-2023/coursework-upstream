"""
CMSC 14100
Autumn 2023

Test code for Homework #3
"""
import os
import sys

import hw3

import pytest
import helpers

# Handle the fact that the test code may not
# be in the same directory as the solution code
sys.path.insert(0, os.getcwd())

# Don't complain about the position of the import
# pylint: disable=wrong-import-position

MODULE = "hw3"


to_hit_check = [
    (11, 10, True),
    (11, 11, True),
    (11, 12, False),
    (4, 1, True),
    (20, 12, True),
    (20, 20, True),
    (20, 21, True),
    (1, 20, False),
    (1, 0, False),
]

@pytest.mark.parametrize("roll, defense, expected", to_hit_check)
def test_check_hit_no_if(roll, defense, expected):
    """
    Do a test for Exercise 1
    """
    recreate_msg = helpers.gen_recreate_msg(
        MODULE, "check_hit_no_if", roll, defense)
    try:
        actual = hw3.check_hit_no_if(roll, defense)
        err_msg = helpers.check_result(actual, expected, recreate_msg)
        if err_msg is not None:
            pytest.fail(err_msg)
    except Exception as e:
        helpers.fail_and_augment_recreate_unexpected_exception(recreate_msg, e)


@pytest.mark.parametrize("roll, defense, expected", to_hit_check)
def test_check_hit_no_and_or(roll, defense, expected):
    """
    Do a test for Exercise 2
    """
    recreate_msg = helpers.gen_recreate_msg(
        MODULE, "check_hit_no_and_or", roll, defense)
    try:
        actual = hw3.check_hit_no_and_or(roll, defense)
        err_msg = helpers.check_result(actual, expected, recreate_msg)
        if err_msg is not None:
            pytest.fail(err_msg)
    except Exception as e:
        helpers.fail_and_augment_recreate_unexpected_exception(recreate_msg, e)


@pytest.mark.parametrize("midterm, final, hw, expected",
                         [
                             (72, 77, 75, "C"),
                             (72, 77, 95, "C"),
                             (72, 80, 81, "C"),
                             (92, 80, 81, "B"),
                             (82, 82, 81, "B"),
                             (91, 93, 61, "F"),
                             (91, 93, 99, "A"),
                             (91, 93, 89, "B"),
                             (71, 51, 89, "F"),
                             (71, 51, 92, "F"),
                             (51, 71, 92, "B"),
                             (49, 71, 92, "F"),
                         ]
                         )
def test_get_grade(midterm, final, hw, expected):
    """
    Do a test for Exercise 3
    """
    recreate_msg = helpers.gen_recreate_msg(
        MODULE, "get_grade", midterm, final, hw)
    try:
        actual = hw3.get_grade(midterm, final, hw)
        err_msg = helpers.check_result(actual, expected, recreate_msg)
        if err_msg is not None:
            pytest.fail(err_msg)
    except Exception as e:
        helpers.fail_and_augment_recreate_unexpected_exception(recreate_msg, e)


@pytest.mark.parametrize("threshold, values, expected", [
    (0, [1, 2, 3], 6),
    (0, [1, 2, 3, 4, 5, 6, 7, 8, 9], 45),
    (0, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 55),
    (3, [1, 2, 3], 0),
    (2, [1, 2, 3], 3),
    (4, [1, 2, 3], 0),
    (4, [5, 1, 2, 3, 5], 10),
    (2, [5, 1, 2, 3, 5], 13),
    (2, [99, 5, 1, 2, 3, 5], 112)
])
def test_find_sum_greater_than(threshold, values, expected):
    """
    Do a test for Exercise 4
    """
    recreate_msg = helpers.gen_recreate_msg(
        MODULE, "find_sum_greater_than", threshold, values)
    try:
        actual = hw3.find_sum_greater_than(threshold, values)
        err_msg = helpers.check_result(actual, expected, recreate_msg)
        if err_msg is not None:
            pytest.fail(err_msg)
    except Exception as e:
        helpers.fail_and_augment_recreate_unexpected_exception(recreate_msg, e)


@pytest.mark.parametrize("target, values, expected", [
    (0, [1, 2, 3], 0),
    (0, [1, 2, 3, 4, 5, 6, 7, 8, 9], 0),
    (2, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 2),
    (3, [1, 2, 3], -1),
    (2, [1, 2, 3], 2),
    (2, [3, 2, 1], 0),
    (4, [1, 2, 3], -1),
    (4, [5, 1, 2, 3, 5], 0),
    (7, [5, 6, 2, 3, 5, 9], 5),
])
def test_find_first_idx_greater_than(target, values, expected):
    """
    Do a test for Exercise 5
    """
    recreate_msg = helpers.gen_recreate_msg(
        MODULE, "find_first_idx_greater_than", target, values)
    try:
        actual = hw3.find_first_idx_greater_than(target, values)
        err_msg = helpers.check_result(actual, expected, recreate_msg)
        if err_msg is not None:
            pytest.fail(err_msg)
    except Exception as e:
        helpers.fail_and_augment_recreate_unexpected_exception(recreate_msg, e)


@pytest.mark.parametrize("threshold, values, expected", [
    (0, [1, 2, 3], -1),
    (0, [1, 2, 3, 4, 5, 6, 7, 8, 9], -1),
    (2, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 0),
    (3, [1, 2, 3], 0),
    (2, [3, 2, 1], 0),
    (4, [1, 2, 3], 1),
    (2, [1], 1),
    (2, [1, 1, 1, 0], 1),
])
def test_compare_all(threshold, values, expected):
    """
    Do a test for Exercise 6
    """
    recreate_msg = helpers.gen_recreate_msg(
        MODULE, "compare_all", threshold, values)
    try:
        actual = hw3.compare_all(threshold, values)
        err_msg = helpers.check_result(actual, expected, recreate_msg)
        if err_msg is not None:
            pytest.fail(err_msg)
    except Exception as e:
        helpers.fail_and_augment_recreate_unexpected_exception(recreate_msg, e)


@pytest.mark.parametrize("target, values, expected", [
    (7, [1, 2, 4], 2),
    (7, [1, 2, 4, 9], 2),
    (7, [6, 2, 8, 9], 1),
    (7, [7, 9, 7, 8], -1),
    (10, [1, 2, 4], 2),
    (10, [1, 2, 11, 12, 13, 10], 1),
    (10, [1, 2, 11, 12, 13, 9], 5),
])
def test_find_last_idx_less_than(target, values, expected):
    """
    Do a test for Exercise 7
    """
    recreate_msg = helpers.gen_recreate_msg(
        MODULE, "find_last_idx_less_than", target, values)
    try:
        actual = hw3.find_last_idx_less_than(target, values)
        err_msg = helpers.check_result(actual, expected, recreate_msg)
        if err_msg is not None:
            pytest.fail(err_msg)
    except Exception as e:
        helpers.fail_and_augment_recreate_unexpected_exception(recreate_msg, e)


@pytest.mark.parametrize("list_1, list_2, expected", [
    ([0, 2, 0, 1], [1, 1, 0, 0, 4], 6),
    ([0, 2, 0, 1], [3, 4, 5, 8, 4], 0),
    ([0, 2, 0, 1], [3, 4, 5, 1, 4], 1),
    ([0, 2, 0, 1], [3, 0, 5, 8, 4], 2),
    ([0, 2, 0, 1], [3, 0, 5, 8, 2], 3),
    ([1, 1, 1], [1, 1, 1], 9),
    ([1, 1, 1], [], 0),
])
def test_count_matches(list_1, list_2, expected):
    """
    Do a test for Exercise 8
    """
    recreate_msg = helpers.gen_recreate_msg(
        MODULE, "count_matches", list_1, list_2)
    try:
        actual = hw3.count_matches(list_1, list_2)
        err_msg = helpers.check_result(actual, expected, recreate_msg)
        if err_msg is not None:
            pytest.fail(err_msg)
    except Exception as e:
        helpers.fail_and_augment_recreate_unexpected_exception(recreate_msg, e)
