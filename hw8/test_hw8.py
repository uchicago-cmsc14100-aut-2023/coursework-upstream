"""
CMSC 14100
Autumn 2022

Test code for Homework #8
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
import hw8
import tree

MODULE = "hw8"

@pytest.mark.timeout(60)
@pytest.mark.parametrize("a, b, c, d, expected",  [
    (1, 1, 5, 2, True),
    (1, 4, 5, 9, True),
    (1, 2, 3, 6, False),    
    (2, 2, 2, 1000, True),
    (1, 4, 62, 45, True),
    (8, 9, 8, 9, True),
    (1, 2, 2, 1, False),
    (1, 1, 10, 12, False),
    (789, 789, 1, 1000, False),
    (2, 2, 1000, 998, True),
    (7, 9, 30, 26, False),
    (4, 1, 28, 29, True),
    (3, 7, 20, 27, False),
    (8, 5, 25, 25, False),
    (10, 5, 21, 29, False),
    (7, 5, 20, 29, False),
    (5, 5, 23, 29, False)
])
def test_has_path(a, b, c, d, expected):
    """
    Test code for has_path
    """
    recreate_msg = helpers.gen_recreate_msg(MODULE, "has_path", a, b, c, d)
    try:
        actual = hw8.has_path(a, b, c, d)
    except Exception as e:
        helpers.fail_and_augment_recreate_unexpected_exception(recreate_msg, e)
        
    err_msg = helpers.check_result(actual, expected, recreate_msg)
    if err_msg is not None:
        pytest.fail(err_msg)
    
    
def mk_doll(lst):
    """
    Make an M-doll from a list.
    """
    doll = tuple()
    for val in lst[::-1]:
        doll = (val, doll)
    return doll


from hw8 import DOLLS_EQUAL, DOLL1_PREFIX_OF_DOLL2, DOLL2_PREFIX_OF_DOLL1

@pytest.mark.timeout(60)
@pytest.mark.parametrize("d1, d2, expected",  [
    # empty dolls
    (mk_doll([]), mk_doll([]), DOLLS_EQUAL),

    # dolls of length 1
    (mk_doll(["A"]), mk_doll(["A"]), DOLLS_EQUAL),
    (mk_doll(["A"]), mk_doll(["B"]), 0),

    # Compare an empty doll with a non-empty doll
    (mk_doll(["A", "B", "C"]), mk_doll([]), DOLL2_PREFIX_OF_DOLL1),
    (mk_doll([]), mk_doll(["A", "B", "C"]), DOLL1_PREFIX_OF_DOLL2),           

    # Compare prefix
    (mk_doll(["A", "B", "C"]), mk_doll(["A", "B", "C", "D", "E"]),
     DOLL1_PREFIX_OF_DOLL2),
    (mk_doll(["A", "B", "C", "D", "E"]), mk_doll(["A", "B", "C"]),
     DOLL2_PREFIX_OF_DOLL1),


    # Compare dolls that are equal
    (mk_doll(["A", "B", "C"]), mk_doll(["A", "B", "C"]), DOLLS_EQUAL),

    # Compare dolls that are different
    (mk_doll(["A", "B", "C", "D", "E"]),
     mk_doll(["X", "B", "C", "D", "F"]), 0),
    (mk_doll(["X", "B", "C", "D", "E"]),
     mk_doll(["A", "B", "C", "D", "F"]), 0),

    (mk_doll(["A", "X", "C", "D", "F"]),
     mk_doll(["A", "B", "C", "D", "E"]), 1),

    (mk_doll(["A", "B", "C", "D", "E"]),
     mk_doll(["A", "X", "C", "D", "F"]), 1),

    (mk_doll(["A", "B", "C", "E"]), mk_doll(["A", "B", "D", "E"]), 2),
    (mk_doll(["A", "B", "D", "E"]), mk_doll(["A", "B", "E", "E"]), 2),    

    (mk_doll(["A", "B", "C", "D", "F"]),
     mk_doll(["A", "B", "C", "D", "E"]), 4),
    (mk_doll(["A", "B", "C", "D", "E"]),
     mk_doll(["A", "B", "C", "D", "F"]), 4),

])
def test_doll_first_diff(d1, d2, expected):
    """
    Test code for doll_first_diff
    """
    steps = [
        f"doll1 = {d1}",
        f"doll2 = {d2}",
        f"hw8.doll_first_diff(doll1, doll2)"
        ]
    recreate_msg = helpers.gen_recreate_commands(MODULE, steps)
    try:
        actual = hw8.doll_first_diff(d1, d2)
    except Exception as e:
        helpers.fail_and_augment_recreate_unexpected_exception(recreate_msg, e)

    err_msg = helpers.check_result(actual, expected, recreate_msg)
    if err_msg is not None:
        pytest.fail(err_msg)

    

@pytest.mark.timeout(60)
@pytest.mark.parametrize("input_filename, expected", [
    ("test_data/paths-004.in", 1),
    ("test_data/paths-005.in", 1),        
    ("test_data/paths-001.in", 4),
    ("test_data/paths-002.in", 8),
    ("test_data/paths-003.in", 3)
])
def test_count_leaves(input_filename, expected):
    """
    Test code for count_leaves
    """
    t = tree.load_tree(input_filename)
    if t is None:
        pytest.fail(f"Cannot open file: '{input_filename}'")

    steps = [
        f"import tree",
        f"t = tree.load_tree('{input_filename}')",
        f"hw8.count_leaves(t)"
        ]
    recreate_msg = helpers.gen_recreate_commands(MODULE, steps)

    try:
        actual = hw8.count_leaves(t)
    except Exception as e:
        helpers.fail_and_augment_recreate_unexpected_exception(recreate_msg, e)

    err_msg = helpers.check_result(actual, expected, recreate_msg)
    if err_msg is not None:
        pytest.fail(err_msg)

        
@pytest.mark.timeout(60)
@pytest.mark.parametrize("input_filename, expected", [
    ("test_data/paths-001.in", [0, 10, 5, 36]),
    ("test_data/paths-002.in", [20, 21, 22, 23, 24, 25, 26, 27]),
    ("test_data/paths-003.in", [2, 5, 0]),
    ("test_data/paths-004.in", [27]),
    ("test_data/paths-005.in", [25])
])
def test_find_leaf_values(input_filename, expected):
    """
    Test code for find_leaf_values
    """
    t = tree.load_tree(input_filename)
    if t is None:
        pytest.fail(f"Cannot open file: '{input_filename}'")

    steps = [
        f"import tree",
        f"t = tree.load_tree('{input_filename}')",
        f"hw8.find_leaf_values(t)"
        ]
    recreate_msg = helpers.gen_recreate_commands(MODULE, steps)

    try:
        actual = hw8.find_leaf_values(t)
    except Exception as e:
        helpers.fail_and_augment_recreate_unexpected_exception(recreate_msg, e)

    err_msg = helpers.check_1d_iterable(actual, expected, recreate_msg)
    if err_msg is not None:
        pytest.fail(err_msg)
        
            
@pytest.mark.timeout(60)
@pytest.mark.parametrize("input_filename, expected", [
    ("test_data/paths-001.in", (1, 1, 6)),
    ("test_data/paths-002.in", (0, 0, 15)),
    ("test_data/paths-003.in", (1, 1, 2)),
    ("test_data/paths-004.in", (0, 0, 1)),
    ("test_data/paths-005.in", (1, 1, 2)),
    ("test_data/paths-006.in", (0, 1, 0)),
    ("test_data/paths-007.in", (1, 0, 0))
])
def test_characterize_values(input_filename, expected):
    """
    Test code for characterize_values
    """
    t = tree.load_tree(input_filename)
    if t is None:
        pytest.fail(f"Cannot open file: '{input_filename}'")

    steps = [
        f"import tree",
        f"t = tree.load_tree('{input_filename}')",
        f"hw8.characterize_values(t)"
        ]
    recreate_msg = helpers.gen_recreate_commands(MODULE, steps)

    try:
        actual = hw8.characterize_values(t)
    except Exception as e:
        helpers.fail_and_augment_recreate_unexpected_exception(recreate_msg, e)

    err_msg = helpers.check_1d_iterable(actual, expected, recreate_msg)
    if err_msg is not None:
        pytest.fail(err_msg)
            

@pytest.mark.timeout(60)
@pytest.mark.parametrize("input_filename, expected", [
    ("test_data/paths-001.in", 2),
    ("test_data/paths-002.in", 0),
    ("test_data/paths-003.in", 3),
    ("test_data/paths-004.in", 1),
    ("test_data/paths-005.in", 1),
    ("test_data/paths-006.in", 1),
    ("test_data/paths-007.in", 1)
])
def test_count_monotonic_paths(input_filename, expected):
    """
    Test code for count_monotonic_paths
    """
    t = tree.load_tree(input_filename)
    if t is None:
        pytest.fail(f"Cannot open file: '{input_filename}'")

    steps = [
        f"import tree",
        f"t = tree.load_tree('{input_filename}')",
        f"hw8.count_monotonic_paths(t)"
        ]
    recreate_msg = helpers.gen_recreate_commands(MODULE, steps)

    try:
        actual = hw8.count_monotonic_paths(t)
    except Exception as e:
        helpers.fail_and_augment_recreate_unexpected_exception(recreate_msg, e)

    err_msg = helpers.check_result(actual, expected, recreate_msg)
    if err_msg is not None:
        pytest.fail(err_msg)
        


@pytest.mark.timeout(60)
@pytest.mark.parametrize("input_filename, expected", [
    ("test_data/paths-001.in", [[1, 4, 7], [1, 4, 8]]),
    ("test_data/paths-002.in", []),
    ("test_data/paths-003.in", [[1, 2], [1, 3], [1, 4]]),
    ("test_data/paths-004.in", [[1]]),
    ("test_data/paths-005.in", [[1, 2, 3, 4]]),
    ("test_data/paths-006.in", [[1]]),
    ("test_data/paths-007.in", [[1]])
])
def test_find_monotonic_paths(input_filename, expected):
    """
    Test code for find_monotonic_paths
    """
    t = tree.load_tree(input_filename)
    if t is None:
        pytest.fail(f"Cannot open file: '{input_filename}'")

    steps = [
        f"import tree",
        f"t = tree.load_tree('{input_filename}')",
        f"hw8.find_monotonic_paths(t)"
        ]
    recreate_msg = helpers.gen_recreate_commands(MODULE, steps)

    try:
        actual = hw8.find_monotonic_paths(t)
    except Exception as e:
        helpers.fail_and_augment_recreate_unexpected_exception(recreate_msg, e)

    err_msg = helpers.check_1d_iterable(actual, expected, recreate_msg)
    if err_msg is not None:
        pytest.fail(err_msg)
        
    
        
@pytest.mark.timeout(60)
@pytest.mark.parametrize("input_filename, k, expected", [
    ("test_data/paths-001.in", 3, True),
    ("test_data/paths-001.in", 2, False),
    ("test_data/paths-001.in", 1, False),        

    ("test_data/paths-002.in", 1, True),

    ("test_data/paths-003.in", 0, True),

    ("test_data/paths-004.in", 1, True),

    ("test_data/paths-008.in", 1, False),
    ("test_data/paths-008.in", 2, True),    
])
def test_is_k_balanced(input_filename, k, expected):
    t = tree.load_tree(input_filename)
    if t is None:
        pytest.fail(f"Cannot open file: '{input_filename}'")

    steps = [
        f"import tree",
        f"t = tree.load_tree('{input_filename}')",
        f"hw8.is_k_balanced(t, {k})"
        ]
    recreate_msg = helpers.gen_recreate_commands(MODULE, steps)

    try:
        actual = hw8.is_k_balanced(t, k)
    except Exception as e:
        helpers.fail_and_augment_recreate_unexpected_exception(recreate_msg, e)

    err_msg = helpers.check_result(actual, expected, recreate_msg)
    if err_msg is not None:
        pytest.fail(err_msg)


def compare_schedules(s1, s2):
    """
    Compare two schedules.  The order of the instructors assigned to a given day
    is not relevant.  We could have used sets, but we did not teach the students
    about sets this year.
    """
    # verify that all the key value pairs in
    # s1 also occur in s2.
    for s1_day, s1_instructors in s1.items():
        if s1_day not in s2:
            return s1_instructors == []
        if len(s1_instructors) != len(s2[s1_day]):
            return False
        if set(s1_instructors) != set(s2[s1_day]):
            return False

    # verify that all the key value pairs that
    # occur in s2 also occur in s1.
    for s2_day, s2_instructors in s2.items():
        if s2_day not in s1:
            return s2_instructors == []
        if len(s2_instructors) != len(s1[s2_day]):
            return False
        if set(s2_instructors) != set(s1[s2_day]):
            return False
    return True

def look_for_schedule_in_list(s1, list_of_schedules):
    """
    Look for a schedule in a list of schedules.
    """
    for s in list_of_schedules:
        if compare_schedules(s1, s):
            return True
    return False


ONE_INSTRUCTOR = ["a"]
THREE_INSTRUCTORS = ["a", "b", "c"]
FOUR_INSTRUCTORS = ["a", "b", "c", "d"]
@pytest.mark.timeout(60)
@pytest.mark.parametrize("instructors, constraints, max_per_day, expected", [
    (ONE_INSTRUCTOR, {"a": [1, 2, 3]}, 1,
     [{1: ['a']}, {2: ['a']}, {3: ['a']}]),
    (ONE_INSTRUCTOR, {"a": [1, 2, 3]}, 2,
     [{1: ['a']}, {2: ['a']}, {3: ['a']}]),
    (ONE_INSTRUCTOR, {"a": [1]}, 1,
     [{1: ['a']}]),
    (THREE_INSTRUCTORS, {"a": [1,2], "b": [1], "c": [1,2] }, 2,
     [{2: ['c'], 1: ['b', 'a']},
      {1: ['c', 'b'], 2: ['a']},
      {2: ['c', 'a'], 1: ['b']}]),
    (THREE_INSTRUCTORS,  { "a": [1,2], "b": [1], "c": [1,2,3] }, 2,
     [{2: ['c'], 1: ['b', 'a']},
      {3: ['c'], 1: ['b', 'a']},
      {1: ['c', 'b'], 2: ['a']},
      {2: ['c', 'a'], 1: ['b']},
      {3: ['c'], 1: ['b'], 2: ['a']}]),
    (FOUR_INSTRUCTORS,  { "a": [1], "b": [1],  "c": [1], "d": [1]}, 2,
     []),
    (FOUR_INSTRUCTORS, { "a": [1], "b": [1], "c": [2], "d": [2]}, 2,
     [{2: ['d', 'c'], 1: ['b', 'a']}]),
    (THREE_INSTRUCTORS,  { "a": [1,2], "b": [1,2], "c": [1,2] }, 3,
     [{1: ['c', 'b', 'a']},
      {2: ['c'], 1: ['b', 'a']},
      {1: ['c', 'a'], 2: ['b']},
      {2: ['c', 'b'], 1: ['a']},
      {1: ['c', 'b'], 2: ['a']},
      {2: ['c', 'a'], 1: ['b']},
      {1: ['c'], 2: ['b', 'a']},
      {2: ['c', 'b', 'a']}])
    ])
def test_find_schedules(instructors, constraints, max_per_day, expected):
    """
    Test code for find_schedules
    """
    steps = [
        f"instructors = {instructors}",
        f"constraints = {constraints}",
        f"hw8.find_schedules(instructors, constraints, {max_per_day})"
        ]
    recreate_msg = helpers.gen_recreate_commands(MODULE, steps)

    try:
        actual = hw8.find_schedules(instructors, constraints, max_per_day)
    except Exception as e:
        helpers.fail_and_augment_recreate_unexpected_exception(recreate_msg, e)


    # Check that the actual value is not None
    msg = helpers.check_not_none(actual, recreate_msg)
    if msg is not None:
        pytest.fail(msg)

    # Check the type of actual value
    msg = helpers.check_type(actual, expected, recreate_msg)
    if msg is not None:
        pytest.fail(msg)

    # Check that the actual value is the correct length
    msg = helpers.check_list_length(actual, expected, recreate_msg)
    if msg is not None:
        pytest.fail(msg)

    # Check the schedules
    # Order of the results is not relevant
    # Look for an actual value without a mate in the expected value
    for i, schedule in enumerate(actual):
        msg = f"Checking list of schedules.  Problem found at index {i} in the actual list:\n"
        if not isinstance(schedule, dict):
            msg += f"Schedules should be dictionaries, not {type(schedule)}."
            pytest.fail(msg + recreate_msg)

        if not look_for_schedule_in_list(schedule, expected):
            msg += f"Schedule {schedule} from the actual result is not in the expected result\n\n"
            msg += f"Actual result: [\n"
            msg += ",\n".join("  " + str(s) for s in actual) + "\n]\n\n"
            msg += f"Expected result: [\n"
            msg += ",\n".join("  " + str(s) for s in expected) + "\n]\n"
            pytest.fail(msg + recreate_msg)

    # Order of the results is not relevant
    # Look for an expected value without a mate in the actual result
    for i, schedule in enumerate(expected):
        msg = f"Checking list of schedules.  Problem found at index {i} of the expected list:\n"
        if not look_for_schedule_in_list(schedule, actual):
            msg += f"Schedule {schedule} from the expected result is not in the actual result\n"
            msg += f"Expected result: [\n"
            msg += ",\n".join("  " + str(s) for s in expected) + "\n]\n\n"
            msg += f"Actual result: [\n"
            msg += ",\n".join("  " + str(s) for s in actual) + "\n]\n"
            pytest.fail(msg + recreate_msg)
            
