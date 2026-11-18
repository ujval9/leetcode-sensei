r"""
TIP102 | Week 11 | Session 2 | Problem Set Version 2 | Problem 5
Reinforce the Kingdom Walls

Source: statement reconstructed from the CodePath solution guide and written in our own words.
The original course page is behind a login, so wording and details may differ slightly.
Solution guide (only after you have tried!): https://github.com/codepath/compsci_guides/wiki/Reinforce-the-Kingdom-Walls

PROBLEM
-------
`kingdom_grid` holds defensive strengths. The section containing (row, col) is all cells connected to it with the same strength. Write `reinforce_walls(kingdom_grid, row, col, new_strength)` that recolors only the border cells of that section (cells on the grid edge or next to a different strength) to `new_strength`, and returns the grid.

EXAMPLES (test cases from the solution guide)
---------------------------------------------
HAPPY CASE
Input: kingdom_grid = [
    [1, 1, 1, 2],
    [1, 3, 1, 2],
    [1, 1, 1, 2]
], row = 1, col = 1, new_strength = 4
Output: [
    [1, 1, 1, 2],
    [1, 4, 1, 2],
    [1, 1, 1, 2]
]
Explanation: The square (1, 1) is a border square, and it gets updated to the new strength.

EDGE CASE
Input: kingdom_grid = [
    [1, 1],
    [1, 1]
], row = 0, col = 0, new_strength = 2
Output: [
    [2, 2],
    [2, 2]
]
Explanation: Since the entire section is a border, the whole section gets updated.
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

def reinforce_walls(kingdom_grid, row, col, new_strength):
    pass
