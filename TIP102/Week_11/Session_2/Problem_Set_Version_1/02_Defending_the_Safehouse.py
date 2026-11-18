r"""
TIP102 | Week 11 | Session 2 | Problem Set Version 1 | Problem 2
Defending the Safehouse

Source: statement reconstructed from the CodePath solution guide and written in our own words.
The original course page is behind a login, so wording and details may differ slightly.
Solution guide (only after you have tried!): https://github.com/codepath/compsci_guides/wiki/Defending-the-Safehouse

PROBLEM
-------
`city` is a grid where 1 is passable and 0 is blocked. You may flip at most one passable cell (not the entrance at the top-left or the safehouse at the bottom-right) to 0. Write `can_disconnect_safehouse(city)` that returns True if this can leave no path from the entrance to the safehouse.

EXAMPLES (test cases from the solution guide)
---------------------------------------------
HAPPY CASE
Input: city = [
    [1, 1, 1],
    [0, 0, 1],
    [1, 1, 1]
]
Output: False
Explanation: No single flip can disconnect the path from (0,0) to (m-1,n-1).

EDGE CASE
Input: city = [
    [1, 0, 0],
    [1, 1, 0],
    [0, 1, 1]
]
Output: True
Explanation: Flipping the cell at (1, 1) disconnects the path between the entrance and the safehouse.
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


def can_disconnect_safehouse(city):
    pass
