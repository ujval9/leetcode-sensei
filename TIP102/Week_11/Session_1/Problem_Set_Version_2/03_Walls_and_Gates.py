r"""
TIP102 | Week 11 | Session 1 | Problem Set Version 2 | Problem 3
Walls and Gates

Source: statement reconstructed from the CodePath solution guide and written in our own words.
The original course page is behind a login, so wording and details may differ slightly.
Solution guide (only after you have tried!): https://github.com/codepath/compsci_guides/wiki/Walls-and-Gates

PROBLEM
-------
In `castle`, -1 is a wall, 0 is a gate, and float('inf') is an empty room. Fill each empty room in place with the distance to its nearest gate (moving up, down, left, right). Rooms that cannot reach a gate stay inf.

EXAMPLES (test cases from the solution guide)
---------------------------------------------
HAPPY CASE
Input: castle = [
    [float('inf'), -1, 0, float('inf')],
    [float('inf'), float('inf'), float('inf'), -1],
    [float('inf'), -1, float('inf'), -1],
    [0, -1, float('inf'), float('inf')]
]
Output: [
    [3, -1, 0, 1],
    [2, 2, 1, -1],
    [1, -1, 2, -1],
    [0, -1, 3, 4]
]
Explanation: The empty rooms are updated with their distances to the nearest gates.

EDGE CASE
Input: castle = [
    [1, -1],
    [-1, 1]
]
Output: [
    [1, -1],
    [-1, 1]
]
Explanation: There are no gates in the grid, so the grid remains unchanged.
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


def walls_and_gates(castle):
    pass
