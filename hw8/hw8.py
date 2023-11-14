"""
CMSC 14100, Autumn 2023
Homework #6

We will be using anonymous grading, so please do NOT include your name
in this file

People Consulted:
   List anyone (other than the course staff) that you consulted about
   this assignment.

Online resources consulted:
   List the URLs of any online resources other than the course text and
   the official Python language documentation that you used to complete
   this assignment.
"""

# Exercise 1
def has_path(a, b, c, d):
    """
    Determine whether it is possible to (a, b) to (c, d) using the
    following rewrite rules:

      (a, b) => (a + b, b) or
      (a, b) => (a, a + b)

    Inputs:
        a, b [int]: the staring coordinates
        c, d [int]: the target end coordinates

    Returns [bool]: True if there is a way to get from (a, b) to
      (c, d) using the rewrite rules, possibly repeatedly.
    """
    ### Your code here
    return None

# Exercise 2
DOLLS_EQUAL = -1
DOLL1_PREFIX_OF_DOLL2 = -2
DOLL2_PREFIX_OF_DOLL1 = -3

def doll_first_diff(doll1, doll2):
    """
    Given two m-dolls, determine the index of the first place
    where they differ.  Dolls that are equal or the case where one
    doll is a prefix of the other are handled as special cases. (See
    Returns)

    Inputs:
        doll1 [Tuple(str, Tuple)]: one M-doll
        doll2 [Tuple(str, Tuple)]: another M-doll

    Returns [int]:
      - the first index at which the dolls differ
      - DOLLS_EQUAL if the two dolls are equal
      - DOLL1_PREFIX_OF_DOLL2 if the doll1 is a prefix of doll2
      - DOLL2_PREFIX_OF_DOLL1 if the doll2 is a prefix of doll1
    """
    ### Your code here
    return None


# Exercise 3
def count_leaves(t):
    """
    Count the leaves in the tree.

    Inputs:
        t [Tree]: a non-empty tree

    Returns [int]: the number of leaves in the tree
    """
    ### Your code here
    return None


# Exercise 4
def find_leaf_values(t):
    """
    Construct a list with the values in the leaves in the tree.

    Inputs:
        t [Tree]: a non-empty tree

    Returns [List[int]]: a list the values from the leaves in the tree
    """
    ### Your code here
    return None


# Exercise 5
def characterize_values(t):
    """
    Characterize the values in the tree,

    Inputs:
        t [Tree]: a non-empty tree

    Returns [Tuple(int, int, int)]: a tuple with
      - the number of negative values in the tree,
      - the number of zeros in the tree, and
      - the number of positive values in the tree.
    in that order
    """
    ### Your code here
    return None


# Exercise 6
def count_monotonic_paths(t):
    """
    Count the number of root-to-leaf paths that have
    monotonically increasing values.

    Inputs:
        t [Tree]: a tree

    Returns [int]: the number of root-to-leaf paths in the
      tree with monotonically increasing values
    """
    assert t is not None
    ### Your code here
    return None


# Exercise 7
def find_monotonic_paths(t):
    """
    Find the root-to-leaf paths that have monotonically increasing
    values.

    Inputs:
        t [Tree]: a tree

    Returns [List[List[int]]: a list of the monotonically increasing
      paths in the tree.  A path contains a list of the nodes in the
      path, in the order that they appear from root to leaf.
    """
    assert t is not None
    ### Your code here
    return None


# Exercise 8
def is_k_balanced(t, k):
    """
    Does a tree fit the definition of k-balanced?

    Inputs:
        t (Tree): a tree
        k (int): maximum difference in the number of nodes between
          siblings.

    Returns: True if t is k-balanced and False otherwise.
    """
    assert t is not None
    ### Your code here
    return None


def find_schedules(instructors, constraints, max_per_day):
    """
    This function computes all the class schedules that meet the
    instructors' constraints and the maximum number of instructors
    that can teach on any give day.

    Inputs:
        instructors [List[str]]: a list of the instructors' names
        constraints [Dict[str, List[int]]: The scheduling constraints of the
          instructors. The keys are the instructors names.  For each instructor,
          the associatedvalue is a list of the days (represented as integers)
          that the instructor is available.  Every instructor will have at least
          one day that they are available.
        max_per_day: The maximum number of instructors that can teach on any
          given day

    Returns [List[Dict[int, List[str]]]]: a list of the schedules that meet the
      constraints. Each schedule is represented by a dictionary that maps a day
      to the list of instructors who would teach on that day.  Days that have
      no instructors assigned can be omitted or represented with the empty list.
    """
    ### Your code here
    return None
