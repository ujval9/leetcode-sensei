r"""
TIP102 | Week 11 | Session 1 | Problem Set Version 2 | Problem 2
Castle Path

Source: statement reconstructed from the CodePath solution guide and written in our own words.
The original course page is behind a login, so wording and details may differ slightly.
Solution guide (only after you have tried!): https://github.com/codepath/compsci_guides/wiki/Castle-Path

PROBLEM
-------
`kingdom` is a grid where 'X' is a safe town and 'O' is a bandit town you cannot enter. Write `path_to_castle(kingdom, town, castle)` that returns a list of cells forming a path from `town` to `castle`, or None if there is no path.

EXAMPLES (test cases from the solution guide)
---------------------------------------------
HAPPY CASE
Input: kingdom = [
    ['X', 'O', 'X', 'X', 'O'],
    ['X', 'X', 'X', 'X', 'O'],
    ['O', 'O', 'X', 'X', 'O'],
    ['X', 'O', 'X', 'X', 'X']
], town = (0, 0), castle = (3, 4)
Output: [(0, 0), (1, 0), (1, 1), (1, 2), (2, 2), (3, 2), (3, 3), (3, 4)]
Explanation: This is one valid path from the starting town to the castle.

EDGE CASE
Input: kingdom = [
    ['X', 'O', 'X', 'X', 'O'],
    ['X', 'X', 'X', 'X', 'O'],
    ['O', 'O', 'X', 'X', 'O'],
    ['X', 'O', 'X', 'X', 'X']
], town = (0, 4), castle = (3, 4)
Output: None
Explanation: There is no path from the starting position (0, 4) to the castle (3, 4) because the path is blocked by bandits.
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


def path_to_castle(kingdom, town, castle):
    pass
