r"""
TIP102 | Week 11 | Session 2 | Problem Set Version 2 | Problem 1
Number of Protected Towns

Source: statement reconstructed from the CodePath solution guide and written in our own words.
The original course page is behind a login, so wording and details may differ slightly.
Solution guide (only after you have tried!): https://github.com/codepath/compsci_guides/wiki/Number-of-Protected-Towns

PROBLEM
-------
In `kingdom`, 0 is town land and 1 is wall. A protected town is a group of connected 0s (up, down, left, right) that never touches the border. Write `count_protected(kingdom)` that returns how many protected towns there are.

EXAMPLES (test cases from the solution guide)
---------------------------------------------
HAPPY CASE
Input: kingdom = [
    [1,1,1,1,1,1,1,0],
    [1,0,0,0,0,1,1,0],
    [1,0,1,0,1,1,1,0],
    [1,0,0,0,0,1,0,1],
    [1,1,1,1,1,1,1,0]
]
Output: 2
Explanation: There are two protected towns in the grid that are completely surrounded by `1`s.

EDGE CASE
Input: kingdom = [
    [0,0,1,0,0],
    [0,1,0,1,0],
    [0,1,1,1,0]
]
Output: 1
Explanation: The only protected town is the single `0` at row 1, column 2 — every other `0` in the grid touches the border and is therefore unprotected.
"""

# STATUS: not started    (not started | in progress | solved | solved with help)

"""
UNDERSTAND:
    * Input:
    * Output:

    * questions about the problem?

    * edge cases?


MATCH:    * similar problems?

PLAN
1.

IMPLEMENT:
-

REVIEW:


EVALUATE:
    * runtime and complexity?


"""

def count_protected(kingdom):
    pass
