"""
CMSC 14100
Autumn 2022

Test code for Homework #6
"""


import hw6
import json
import os
import sys
import pytest
import helpers
import line_helpers


# Handle the fact that the test code may not
# be in the same directory as the solution code
sys.path.insert(0, os.getcwd())

# Don't complain about the position of the import
# pylint: disable=wrong-import-position

MODULE = "hw6"


filter_tests = json.load(open('tests/filter_tests.json','r',encoding="utf-8"))
@pytest.mark.timeout(60)
@pytest.mark.parametrize("filename, category, value, expected", filter_tests)
def test_filter_by_category(filename, category, value, expected):
    """
    Do a single test for the function: filter_by_category
    """

    steps = [
        "import line_helpers",
        f"lines = line_helpers.load_sample('{filename}')",
        f'hw6.filter_by_category(lines, "{category}", "{value}")'
    ]

    recreate_msg = helpers.gen_recreate_commands(MODULE, steps)
    try:
        lines = line_helpers.load_sample(filename)
        actual = hw6.filter_by_category(lines, category, value)

        # Check that the actual result matches the expected result
        err_msg = helpers.check_1d_iterable(actual, expected, recreate_msg)
        if err_msg is not None:
            pytest.fail(err_msg)
    except Exception as e:
        helpers.fail_and_augment_recreate_unexpected_exception(recreate_msg, e)


count_tests = json.load(open('tests/count_tests.json','r',encoding="utf-8"))
@pytest.mark.timeout(60)
@pytest.mark.parametrize("filename, category, expected", count_tests)
def test_count_lines_by_category(filename, category, expected):
    """
    Do a single test for the function: count_lines_by_category
    """
    steps = [
        "import line_helpers",
        f"lines = line_helpers.load_sample('{filename}')",
        f'hw6.count_lines_by_category(lines, "{category}")'
    ]

    recreate_msg = helpers.gen_recreate_commands(MODULE, steps)
    try:
        lines = line_helpers.load_sample(filename)
        actual = hw6.count_lines_by_category(lines, category)

        # Check that the actual result matches the expected result
        err_msg = helpers.check_result(actual, expected, recreate_msg)
        if err_msg is not None:
            pytest.fail(err_msg)
    except Exception as e:
        helpers.fail_and_augment_recreate_unexpected_exception(recreate_msg, e)


generate_n_grams_tests = json.load(open('tests/generate_n_grams_tests.json', 'r', encoding="utf-8"))
@pytest.mark.timeout(60)
@pytest.mark.parametrize("sentence, n, expected", generate_n_grams_tests)
def test_generate_n_grams(sentence, n, expected):
    """
    Do a single test for the function: generate_n_grams
    """
    recreate_msg = helpers.gen_recreate_msg(MODULE, "generate_n_grams",
                                            sentence, n)
    try:
        # Convert the expected result to a List of Tuples
        expected = [tuple(l) for l in expected]

        actual = hw6.generate_n_grams(sentence, n)

        # Check that the actual result matches the expected result
        err_msg = helpers.check_1d_iterable(actual, expected, recreate_msg)
        if err_msg is not None:
            pytest.fail(err_msg)
    except Exception as e:
        helpers.fail_and_augment_recreate_unexpected_exception(recreate_msg, e)



count_n_grams_tests = helpers.load_json_safe_test('tests/count_n_grams_tests.json')
@pytest.mark.timeout(60)
@pytest.mark.parametrize("filename, n, expected", count_n_grams_tests)
def test_count_n_grams(filename, n, expected):
    """
    Do a single test for the function: count_n_grams
    """
    steps = [
        "import line_helpers",
        f"lines = line_helpers.load_sample('{filename}')",
        f'hw6.count_n_grams(lines, {n})'
    ]

    recreate_msg = helpers.gen_recreate_commands(MODULE, steps)
    try:
        lines = line_helpers.load_sample(filename)
        actual = hw6.count_n_grams(lines, n)

        # Check that the actual result matches the expected result
        err_msg = helpers.check_result(actual, expected, recreate_msg)
        if err_msg is not None:
            pytest.fail(err_msg)
    except Exception as e:
        helpers.fail_and_augment_recreate_unexpected_exception(recreate_msg, e)


lm_tests = helpers.load_json_safe_test('tests/language_model_tests.json')
@pytest.mark.timeout(60)
@pytest.mark.parametrize("filename, expected", lm_tests)
def test_generate_language_model(filename, expected):
    """
    Do a single test for the function: generate_language_model
    """
    steps = [
        "import line_helpers",
        f"lines = line_helpers.load_sample('{filename}')",
        "hw6.generate_language_model(lines)"
    ]

    recreate_msg = helpers.gen_recreate_commands(MODULE, steps)
    try:
        lines = line_helpers.load_sample(filename)
        actual = hw6.generate_language_model(lines)

        # Check that the actual result matches the expected result
        err_msg = helpers.check_result(actual, expected, recreate_msg)
        if err_msg is not None:
            pytest.fail(err_msg)
    except Exception as e:
        helpers.fail_and_augment_recreate_unexpected_exception(recreate_msg, e)