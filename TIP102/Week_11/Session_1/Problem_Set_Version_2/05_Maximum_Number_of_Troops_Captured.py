r"""
TIP102 | Week 11 | Session 1 | Problem Set Version 2 | Problem 5
Maximum Number of Troops Captured

Source: statement reconstructed from the CodePath solution guide and written in our own words.
The original course page is behind a login, so wording and details may differ slightly.
Solution guide (only after you have tried!): https://github.com/codepath/compsci_guides/wiki/Maximum-Number-of-Troops-Captured

PROBLEM
-------
In `battlefield`, 0 is an obstacle and a positive number is that many troops. Starting from any troop cell, you can move up, down, left, or right through non-zero cells and capture all their troops. Write `capture_max_troops(battlefield)` that returns the most troops you can capture from one start.

EXAMPLES (test cases from the solution guide)
---------------------------------------------
HAPPY CASE
Input: battlefield = [
    [0,2,1,0],
    [4,0,0,3],
    [1,0,0,4],
    [0,3,2,0]
]
Output: 7
Explanation: You can start at (1,3), capture 3 troops, move to (2,3), and capture 4 troops, for a total of 7 troops.

EDGE CASE
Input: battlefield = [
    [0,0],
    [0,0]
]
Output: 0
Explanation: There are no troops on the battlefield, so the output is 0.
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

from collections import deque


def capture_max_troops(battlefield):
    pass
