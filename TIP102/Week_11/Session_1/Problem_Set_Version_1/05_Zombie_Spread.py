r"""
TIP102 | Week 11 | Session 1 | Problem Set Version 1 | Problem 5
Zombie Spread

Source: statement reconstructed from the CodePath solution guide and written in our own words.
The original course page is behind a login, so wording and details may differ slightly.
Solution guide (only after you have tried!): https://github.com/codepath/compsci_guides/wiki/Zombie-Spread

PROBLEM
-------
In `grid`, 2 is an infected zone, 1 is safe, and 0 is empty. Every hour, infection spreads from each infected cell to adjacent safe cells. Write `time_to_infect(grid)` that returns the hours until every safe zone is infected, or -1 if some can never be infected.

EXAMPLES (test cases from the solution guide)
---------------------------------------------
HAPPY CASE
Input: grid = [
    [2,1,1],
    [1,1,0],
    [0,1,1]
]
Output: 4
Explanation: The infection spreads through the entire city in 4 hours.

EDGE CASE
Input: grid = [
    [2,1,1],
    [0,1,1],
    [1,0,1]
]
Output: -1
Explanation: The safe zone at (2, 0) cannot be infected as it is blocked by obstacles.
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


def time_to_infect(grid):
    pass
