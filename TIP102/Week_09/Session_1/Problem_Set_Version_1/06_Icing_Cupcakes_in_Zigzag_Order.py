r"""
TIP102 | Week 9 | Session 1 | Problem Set Version 1 | Problem 6
Icing Cupcakes in Zigzag Order

Source: statement reconstructed from the CodePath solution guide and written in our own words.
The original course page is behind a login, so wording and details may differ slightly.
Solution guide (only after you have tried!): https://github.com/codepath/compsci_guides/wiki/Icing-Cupcakes-in-Zigzag-Order

PROBLEM
-------
Write `zigzag_icing_order(cupcakes)` that returns the node values level by level, alternating direction each level (left to right, then right to left, and so on), as a single list.

EXAMPLES (test cases from the solution guide)
---------------------------------------------
HAPPY CASE
Input: flavors = ["Chocolate", "Vanilla", "Lemon", "Strawberry", None, "Hazelnut", "Red Velvet"]
Output: ['Chocolate', 'Lemon', 'Vanilla', 'Strawberry', 'Hazelnut', 'Red Velvet']
Explanation: The cupcakes are iced in a zigzag order level by level.

Input: flavors = ["Vanilla"]
Output: ['Vanilla']
Explanation: The tree has only one node, so return its flavor.

EDGE CASE
Input: flavors = []
Output: []
Explanation: The tree is empty, so return an empty list.

Input: flavors = ["Chocolate", "Vanilla", None, "Strawberry"]
Output: ['Chocolate', 'Vanilla', 'Strawberry']
Explanation: The cupcakes are iced in a zigzag order level by level.
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


class TreeNode:
    def __init__(self, flavor, left=None, right=None):
        self.val = flavor
        self.left = left
        self.right = right


def zigzag_icing_order(cupcakes):
    pass
