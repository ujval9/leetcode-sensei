r"""
TIP102 | Week 9 | Session 1 | Problem Set Version 1 | Problem 2
Croquembouche

Source: statement reconstructed from the CodePath solution guide and written in our own words.
The original course page is behind a login, so wording and details may differ slightly.
Solution guide (only after you have tried!): https://github.com/codepath/compsci_guides/wiki/Croquembouche

PROBLEM
-------
Each `Puff` node holds a flavor. Write `print_design(design)` that returns a list of flavors in level order (top to bottom, left to right).

EXAMPLES (test cases from the solution guide)
---------------------------------------------
HAPPY CASE
Input: croquembouche = Puff("Vanilla", Puff("Chocolate", Puff("Vanilla"), Puff("Matcha")), Puff("Strawberry"))
Output: ['Vanilla', 'Chocolate', 'Strawberry', 'Vanilla', 'Matcha']
Explanation: The flavors are printed level by level, starting from the root.

Input: croquembouche = Puff("Chocolate")
Output: ['Chocolate']
Explanation: The tree has only one node, so return its flavor.

EDGE CASE
Input: croquembouche = None
Output: []
Explanation: The tree is empty, so return an empty list.

Input: croquembouche = Puff("Vanilla", Puff("Chocolate"), None)
Output: ['Vanilla', 'Chocolate']
Explanation: The tree has only two nodes, and the second node is on the left.
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


class Puff:
    def __init__(self, flavor, left=None, right=None):
        self.val = flavor
        self.left = left
        self.right = right


def print_design(design):
    pass
