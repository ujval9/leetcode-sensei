r"""
TIP102 | Week 9 | Session 1 | Problem Set Version 1 | Problem 3
Maximum Tiers in Cake

Source: statement reconstructed from the CodePath solution guide and written in our own words.
The original course page is behind a login, so wording and details may differ slightly.
Solution guide (only after you have tried!): https://github.com/codepath/compsci_guides/wiki/Maximum-Tiers-in-Cake

PROBLEM
-------
Write `max_tiers(cake)` that returns the number of tiers (levels) in the cake tree, i.e. its maximum depth. Use breadth-first traversal.

EXAMPLES (test cases from the solution guide)
---------------------------------------------
HAPPY CASE
Input: cake_sections = ["Chocolate", "Vanilla", "Strawberry", None, None, "Chocolate", "Coffee"]
Output: 3
Explanation: The longest path is from "Chocolate" -> "Strawberry" -> "Coffee".

Input: cake_sections = ["Vanilla"]
Output: 1
Explanation: The tree has only one node, so the maximum number of tiers is 1.

EDGE CASE
Input: cake_sections = []
Output: 0
Explanation: The tree is empty, so return 0.

Input: cake_sections = ["Chocolate", "Vanilla", "Strawberry", None, "Raspberry"]
Output: 3
Explanation: The longest path is from "Chocolate" -> "Vanilla" -> "Raspberry".
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

class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right


def max_tiers(cake):
    pass
