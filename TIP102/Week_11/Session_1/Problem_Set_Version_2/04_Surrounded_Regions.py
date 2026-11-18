r"""
TIP102 | Week 11 | Session 1 | Problem Set Version 2 | Problem 4
Surrounded Regions

Source: statement reconstructed from the CodePath solution guide and written in our own words.
The original course page is behind a login, so wording and details may differ slightly.
Solution guide (only after you have tried!): https://github.com/codepath/compsci_guides/wiki/Surrounded-Regions

PROBLEM
-------
`map` is a grid of 'X' and 'O'. Capture every region of 'O's that is completely surrounded by 'X' (does not touch the border) by flipping those 'O's to 'X', in place.

EXAMPLES (test cases from the solution guide)
---------------------------------------------
HAPPY CASE
Input: map = [
    ['X', 'X', 'X', 'X'],
    ['X', 'O', 'O', 'X'],
    ['X', 'X', 'O', 'X'],
    ['X', 'O', 'X', 'X']
]
Output: [
    ['X', 'X', 'X', 'X'],
    ['X', 'X', 'X', 'X'],
    ['X', 'X', 'X', 'X'],
    ['X', 'O', 'X', 'X']
]
Explanation: The region in the middle is surrounded by 'X's and is therefore captured, while the region at the bottom is connected to the edge and cannot be captured.

EDGE CASE
Input: map = [
    ['X', 'X', 'X'],
    ['O', 'O', 'O'],
    ['X', 'X', 'X']
]
Output: [
    ['X', 'X', 'X'],
    ['O', 'O', 'O'],
    ['X', 'X', 'X']
]
Explanation: The middle region is connected to the left and right edges and thus cannot be captured.
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

def capture(map):
    pass
