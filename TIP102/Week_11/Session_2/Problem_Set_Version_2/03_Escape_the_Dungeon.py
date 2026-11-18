r"""
TIP102 | Week 11 | Session 2 | Problem Set Version 2 | Problem 3
Escape the Dungeon

Source: statement reconstructed from the CodePath solution guide and written in our own words.
The original course page is behind a login, so wording and details may differ slightly.
Solution guide (only after you have tried!): https://github.com/codepath/compsci_guides/wiki/Escape-the-Dungeon

PROBLEM
-------
`dungeon` is a grid of 0 (open) and 1 (wall). From `position` you roll in one direction until you hit a wall, then you can choose a new direction. Write `can_escape_dungeon(dungeon, position, exit)` that returns True if you can stop exactly on `exit`.

EXAMPLES (test cases from the solution guide)
---------------------------------------------
HAPPY CASE
Input: dungeon = [
    [0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0],
    [1, 1, 0, 1, 1],
    [0, 0, 0, 0, 0]
], position = (0, 4), exit = (4, 4)
Output: True
Explanation: One valid sequence rolls left from (0,4) to (0,3) (blocked by the wall at (0,2)), down to (1,3) (blocked by (2,3)), left to (1,0), down to (2,0) (blocked by (3,0)), right to (2,2) (blocked by (2,3)), down to (4,2), then right to (4,4).

EDGE CASE
Input: dungeon = [
    [0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0],
    [1, 1, 0, 1, 1],
    [0, 0, 0, 0, 0]
], position = (0, 4), exit = (3, 2)
Output: False
Explanation: No way to stop at the exit.
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


def can_escape_dungeon(dungeon, position, exit):
    pass
