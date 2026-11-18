r"""
TIP102 | Week 11 | Session 1 | Problem Set Version 1 | Problem 3
List All Escape Routes

Source: statement reconstructed from the CodePath solution guide and written in our own words.
The original course page is behind a login, so wording and details may differ slightly.
Solution guide (only after you have tried!): https://github.com/codepath/compsci_guides/wiki/List-All-Escape-Routes

PROBLEM
-------
Write `list_all_escape_routes(grid)` that returns every starting cell from which there is a path of safe cells (1s) to the bottom-right corner of the grid.

EXAMPLES (test cases from the solution guide)
---------------------------------------------
HAPPY CASE
Input: grid = [
    [1, 0, 1, 0, 1],
    [1, 1, 1, 1, 0],
    [0, 0, 1, 0, 0],
    [1, 0, 1, 1, 1]
]
Output: [(0, 0), (0, 2), (1, 0), (1, 1), (1, 2), (1, 3), (2, 2), (3, 2), (3, 3), (3, 4)]
Explanation: These positions can all reach the bottom-right corner of the grid through safe zones.

EDGE CASE
Input: grid = [
    [1, 0],
    [0, 1]
]
Output: [(1, 1)]
Explanation: Only the bottom-right corner itself can reach the safe haven; the top-left cell is sealed off by infected zones.
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

def list_all_escape_routes(grid):
    pass
