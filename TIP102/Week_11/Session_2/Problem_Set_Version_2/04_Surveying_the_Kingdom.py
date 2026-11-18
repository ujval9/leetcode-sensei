r"""
TIP102 | Week 11 | Session 2 | Problem Set Version 2 | Problem 4
Surveying the Kingdom

Source: statement reconstructed from the CodePath solution guide and written in our own words.
The original course page is behind a login, so wording and details may differ slightly.
Solution guide (only after you have tried!): https://github.com/codepath/compsci_guides/wiki/Surveying-the-Kingdom

PROBLEM
-------
`land` is a grid of 0s and 1s where the 1s form rectangular farmland groups that never touch each other. Write `find_farmland_groups(land)` that returns a list of [top_row, left_col, bottom_row, right_col] for each group.

EXAMPLES (test cases from the solution guide)
---------------------------------------------
HAPPY CASE
Input: land = [
    [1, 0, 0],
    [1, 0, 1],
    [1, 0, 1]
]
Output: [
    [0, 0, 2, 0],
    [1, 2, 2, 2]
]
Explanation: There are two farmland groups:
- The first group starts at (0,0) and ends at (2,0).
- The second group starts at (1,2) and ends at (2,2).

EDGE CASE
Input: land = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]
Output: []
Explanation: There are no farmland groups in this case.
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

def find_farmland_groups(land):
    pass
