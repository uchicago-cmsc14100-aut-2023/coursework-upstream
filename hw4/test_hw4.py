"""
CMSC 14100
Autumn 2022

Test code for Homework #4
"""

import hw4
import json
import os
import sys
import pytest
import helpers


# Handle the fact that the test code may not
# be in the same directory as the solution code
sys.path.insert(0, os.getcwd())

# Don't complain about the position of the import
# pylint: disable=wrong-import-position

MODULE = "hw4"

codes = [('L', ('Latte', 4.5)),
         ('C', ('Cortado', 4.0)),
         ('N', ('No Coffee', 0.0))]


@pytest.mark.timeout(60)
@pytest.mark.parametrize("coffee_code, expected", codes)
def test_coffee_name_price(coffee_code, expected):
    """
    Do a single test for the function: coffee_name_price
    """
    recreate_msg = helpers.gen_recreate_msg(MODULE, "coffee_name_price",
                                            coffee_code)
    try:
        actual = hw4.coffee_name_price(coffee_code)

        # Check that the actual result matches the expected result
        err_msg = helpers.check_result(actual, expected, recreate_msg)
        if err_msg is not None:
            pytest.fail(err_msg)
    except Exception as e:
        helpers.fail_and_augment_recreate_unexpected_exception(recreate_msg, e)

coffee_test_cases = [
    [['L', 'L', 'C'], 8, True, ['Latte']],
    [['L', 'L', 'L', 'N', 'C'], 13, True, ['Latte', 'Latte']]]
longer_tests = json.load(open('tests/no_skip_large_coffee_tests.json', 'r',
                              encoding="utf-8"))
coffee_test_cases = coffee_test_cases + longer_tests

@pytest.mark.timeout(60)
@pytest.mark.parametrize("coffee_codes_list, budget, stop_on_budget, expected",
                         coffee_test_cases)
def test_no_skip_how_many_coffees(coffee_codes_list, budget, stop_on_budget, 
                                  expected):
    """
    Do a single test for the function: how_many_coffees
    """

    recreate_msg = helpers.gen_recreate_msg(MODULE, "how_many_coffees",
                                            coffee_codes_list, budget,
                                            stop_on_budget)

    try:
        coffee_codes_list_copy = coffee_codes_list[:]

        actual = hw4.how_many_coffees(
            coffee_codes_list, budget, True)
        
        # Check that the coffee codes list was not modified
        err_msg = helpers.check_list_unmodified("coffee_codes_list", coffee_codes_list, 
                                                coffee_codes_list_copy, recreate_msg)
        if err_msg is not None:
            pytest.fail(err_msg)

        # Check that the actual result matches the expected result
        err_msg = helpers.check_1d_iterable(actual, expected, recreate_msg)
        if err_msg is not None:
            pytest.fail(err_msg)
    except Exception as e:
        helpers.fail_and_augment_recreate_unexpected_exception(recreate_msg, e)


skip_coffee_test_cases = [
    [['L', 'L', 'C'], 8.5, False, ['Latte', 'No Coffee (Skipped)',
                                   'Cortado']],
    [['L', 'L', 'L', 'N', 'C'], 13, False, ['Latte', 'Latte',
                                            'No Coffee (Skipped)',
                                            'No Coffee',
                                            'Cortado']]]
skip_longer_tests = json.load(open('tests/skip_large_coffee_tests.json', 'r',
                              encoding="utf-8"))
skip_coffee_test_cases = skip_coffee_test_cases + skip_longer_tests
@pytest.mark.timeout(60)
@pytest.mark.parametrize("coffee_codes_list, budget, stop_on_budget, expected",
                         skip_coffee_test_cases)
def test_allow_skip_how_many_coffees(coffee_codes_list, budget, stop_on_budget, 
                                  expected):
    """
    Do a single test for the function: how_many_coffees
    """

    recreate_msg = helpers.gen_recreate_msg(MODULE, "how_many_coffees",
                                            coffee_codes_list, budget,
                                            stop_on_budget)

    try:
        coffee_codes_list_copy = coffee_codes_list[:]

        actual = hw4.how_many_coffees(coffee_codes_list, budget, False)
        
        # Check that the coffee codes list was not modified
        err_msg = helpers.check_list_unmodified("coffee_codes_list", coffee_codes_list, 
                                                coffee_codes_list_copy, recreate_msg)
        if err_msg is not None:
            pytest.fail(err_msg)

        # Check that the actual result matches the expected result
        err_msg = helpers.check_1d_iterable(actual, expected, recreate_msg)
        if err_msg is not None:
            pytest.fail(err_msg)
    except Exception as e:
        helpers.fail_and_augment_recreate_unexpected_exception(recreate_msg, e)

small_week_tests = [[1, [['Week 1 - Monday',
  'Week 1 - Tuesday',
  'Week 1 - Wednesday',
  'Week 1 - Thursday',
  'Week 1 - Friday']]],
  [2, [['Week 1 - Monday',
  'Week 1 - Tuesday',
  'Week 1 - Wednesday',
  'Week 1 - Thursday',
  'Week 1 - Friday'],
 ['Week 2 - Monday',
  'Week 2 - Tuesday',
  'Week 2 - Wednesday',
  'Week 2 - Thursday',
  'Week 2 - Friday']]]]
week_test_cases = small_week_tests + json.load(open("tests/week_test_cases.json", "r",
                                 encoding="utf-8"))
@pytest.mark.timeout(60)
@pytest.mark.parametrize("num_weeks, expected", week_test_cases)
def test_generate_days_for_quarter(num_weeks, expected):
    """
    Do a single test for the function: generate_days_for_quarter
    """

    recreate_msg = helpers.gen_recreate_msg(MODULE, "generate_days_for_quarter",
                                            num_weeks)
    try:
        actual = hw4.generate_days_for_quarter(num_weeks)

        # Check that the actual result matches the expected result

        err_msg = helpers.check_2d_iterable(actual, expected, recreate_msg)
        if err_msg is not None:
             pytest.fail(err_msg)
    except Exception as e:
        helpers.fail_and_augment_recreate_unexpected_exception(recreate_msg, e)

small_test_cases = json.load(open("tests/small_quarter_tests.json", "r",
                                  encoding="utf-8"))
quarter_test_cases = small_test_cases + json.load(
    open("tests/long_quarter_tests.json", "r", encoding="utf-8"))
@pytest.mark.timeout(60)
@pytest.mark.parametrize("coffee_codes_list, num_weeks, weekly_budget, expected",
                         quarter_test_cases)
def test_quarter_coffee_schedule(coffee_codes_list, num_weeks, weekly_budget,
                                 expected):
    """
    Do a single test for the function: quarter_coffee_codes_list
    """

    recreate_msg = helpers.gen_recreate_msg(MODULE, "quarter_coffee_schedule",
                                            coffee_codes_list, num_weeks,
                                            weekly_budget)
    try:

        coffee_codes_list_copy = coffee_codes_list[:]

        actual = hw4.quarter_coffee_schedule(coffee_codes_list, num_weeks,
                                             weekly_budget)

        err_msg = helpers.check_list_unmodified("coffee_codes_list", coffee_codes_list, 
                                                coffee_codes_list_copy, recreate_msg)
        if err_msg is not None:
            pytest.fail(err_msg)

        # Check that the actual result matches the expected result

        err_msg = helpers.check_2d_iterable(actual, expected, recreate_msg)
        if err_msg is not None:
            pytest.fail(err_msg)
    except Exception as e:
        helpers.fail_and_augment_recreate_unexpected_exception(recreate_msg, e)
