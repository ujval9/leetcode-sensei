r"""
TIP102 | Week 11 | Session 1 | Problem Set Version 1 | Problem 1
Seeking Safety

Source: statement reconstructed from the CodePath solution guide and written in our own words.
The original course page is behind a login, so wording and details may differ slightly.
Solution guide (only after you have tried!): https://github.com/codepath/compsci_guides/wiki/Seeking-Safety

PROBLEM
-------
`grid` is a matrix where 1 is a safe zone and 0 is infected. Write `next_moves(position, grid)` that returns the list of safe cells you can move to from `position` in one step (up, down, left, right only).

EXAMPLES (test cases from the solution guide)
---------------------------------------------
HAPPY CASE
Input: position = (3, 2), grid = [
    [0, 0, 0, 1, 1],
    [0, 0, 0, 1, 1],
    [1, 1, 1, 0, 0],
    [1, 1, 1, 1, 0],
    [0, 0, 0, 1, 0]
]
Output: [(2, 2), (3, 1), (3, 3)]
Explanation: The cell above, to the left, and to the right of (3, 2) are safe. The one below is not safe.

EDGE CASE
Input: position = (0, 1), grid = [
    [0, 0, 0, 1, 1],
    [0, 0, 0, 1, 1],
    [1, 1, 1, 0, 0],
    [1, 1, 1, 1, 0],
    [0, 0, 0, 1, 0]
]
Output: []
Explanation: All the cells adjacent to (0, 1) are unsafe or out of bounds.
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

def next_moves(position, grid):
    pass
