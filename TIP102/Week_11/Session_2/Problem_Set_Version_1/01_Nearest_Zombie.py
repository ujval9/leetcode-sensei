r"""
TIP102 | Week 11 | Session 2 | Problem Set Version 1 | Problem 1
Nearest Zombie

Source: statement reconstructed from the CodePath solution guide and written in our own words.
The original course page is behind a login, so wording and details may differ slightly.
Solution guide (only after you have tried!): https://github.com/codepath/compsci_guides/wiki/Nearest-Zombie

PROBLEM
-------
In `grid`, 0 is a zombie and 1 is a human. Write `nearest_zombie(grid)` that returns a grid where each cell holds the distance to the nearest zombie (moving up, down, left, right).

EXAMPLES (test cases from the solution guide)
---------------------------------------------
HAPPY CASE
Input: grid = [
    [0,0,0],
    [0,1,0],
    [0,0,0]
]
Output: [
    [0,0,0],
    [0,1,0],
    [0,0,0]
]
Explanation: The nearest zombie for the human at (1, 1) is at distance 1.

EDGE CASE
Input: grid = [
    [0,0,0],
    [0,1,0],
    [1,1,1]
]
Output: [
    [0,0,0],
    [0,1,0],
    [1,2,1]
]
Explanation: The humans at the bottom are at distances 1 and 2 from the nearest zombies.
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


def nearest_zombie(grid):
    pass
