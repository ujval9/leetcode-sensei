r"""
TIP102 | Week 9 | Session 1 | Problem Set Version 2 | Problem 3
Minimum Depth of Secret Path

Source: statement reconstructed from the CodePath solution guide and written in our own words.
The original course page is behind a login, so wording and details may differ slightly.
Solution guide (only after you have tried!): https://github.com/codepath/compsci_guides/wiki/Minimum-Depth-of-Secret-Path

PROBLEM
-------
Write `min_depth(door)` that returns the number of nodes on the shortest path from the root down to the nearest leaf (0 for an empty tree).

EXAMPLES (test cases from the solution guide)
---------------------------------------------
HAPPY CASE
Input: door = Room("Door", Room("Attic"), Room("Cursed Room", Room("Crypt"), Room("Haunted Cellar")))
Output: 2
Explanation: The shortest path is from "Door" -> "Attic".

Input: door = Room("Door")
Output: 1
Explanation: The tree has only one node, so the minimum depth is 1.

EDGE CASE
Input: door = None
Output: 0
Explanation: The tree is empty, so return 0.

Input: door = Room("Door", Room("Attic"), None)
Output: 2
Explanation: The shortest path is from "Door" -> "Attic".
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

class Room:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right


def min_depth(door):
    pass
