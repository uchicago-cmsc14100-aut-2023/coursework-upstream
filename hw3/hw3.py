"""
CMSC 14100
Autumn 2023

Homework #3

We will be using anonymous grading, so please do NOT include your name
in this file

People Consulted:
   List anyone (other than the course staff) that you consulted about
   this assignment.

Online resources consulted:
   List the URL of any online resources other than the course text and
   the official Python language documentation that you used to complete
   this assignment.


[RESUBMISSIONS ONLY: Explain how you addressed the grader's comments
 for your original submission.  If you did not submit a solution for the
 initial deadline, please state that this submission is new.]
"""


def check_hit_no_and_or(roll, defense):
    """
    You are helping build a game where characters roll a 20-sided dice to
    try to hit a monster.  Each monster has a defense value. If the roll is
    greater than or equal to the defense it is a hit. A 20 is always a hit
    and a 1 is always a miss.

    For credit your function must NOT use the boolean and/or operators.

    Inputs:
        roll [int]: a value between 1 and 20 inclusive
        defense [int]: a natural number for the defense of a monster

    Returns [bool]: indicating if the hit is successful
    """
    # Verify that the parameters have sensible values
    assert roll >= 1
    assert roll <= 20
    assert defense >= 0

    # Replace pass with your solution
    pass


def check_hit_no_if(roll, defense):
    """
    You are helping build a game where characters roll a 20-sided dice to
    try to hit a monster.  Each monster has a defense value. If the roll is
    greater than or equal to the defense it is a hit. A 20 is always a hit
    and a 1 is always a miss.

    For credit your function must NOT use an if statement

    Inputs:
        roll [int]: a value between 1 and 20 inclusive
        defense [int]: a natural number for the defense of a monster

    Returns [bool]: indicating if the hit is successful
    """
    # Verify that the parameters have sensible values
    assert roll >= 1
    assert roll <= 20
    assert defense >= 0

    # Replace pass with your solution
    pass


def get_grade(midterm, final, hw):
    """
    Your docstring here.
    """
    # Verify that the parameters have sensible values
    assert midterm >= 0
    assert final >= 0
    assert hw >= 0

    # Replace pass with your solution
    pass


def find_sum_greater_than(threshold, values):
    """
    Your docstring here.
    """
    assert len(values) > 0
    assert isinstance(threshold, int)
    assert isinstance(values, list)

    # Replace pass with your solution
    pass


def find_first_idx_greater_than(target, values):
    """
    Your docstring here.
    """
    assert len(values) > 0
    assert isinstance(target, int)
    assert isinstance(values, list)

    # Replace pass with your solution
    pass


def compare_all(threshold, values):
    """
    Your docstring here.
    """
    assert len(values) > 0
    assert isinstance(threshold, int)
    assert isinstance(values, list)

    # Replace pass with your solution
    pass


def find_last_idx_less_than(target, values):
    """
    Your docstring here.
    """
    assert len(values) > 0
    assert isinstance(target, int)
    assert isinstance(values, list)

    # Replace pass with your solution
    pass


def count_matches(list_1, list_2):
    """
    Your docstring here.
    """
    assert isinstance(list_1, list)
    assert isinstance(list_2, list)

    # Replace pass with your solution
    pass
