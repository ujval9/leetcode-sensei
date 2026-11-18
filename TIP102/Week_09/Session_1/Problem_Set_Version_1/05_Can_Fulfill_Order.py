r"""
TIP102 | Week 9 | Session 1 | Problem Set Version 1 | Problem 5
Can Fulfill Order

Source: statement reconstructed from the CodePath solution guide and written in our own words.
The original course page is behind a login, so wording and details may differ slightly.
Solution guide (only after you have tried!): https://github.com/codepath/compsci_guides/wiki/Can-Fulfill-Order

PROBLEM
-------
Write `can_fulfill_order(inventory, order_size)` that returns True if there is a root-to-leaf path in the tree whose values add up to exactly `order_size`, otherwise False.

EXAMPLES (test cases from the solution guide)
---------------------------------------------
HAPPY CASE
Input: quantities = [5,4,8,11,None,13,4,7,2,None,None,None,1], order_size = 22
Output: True
Explanation: The path 5 -> 4 -> 11 -> 2 sums to 22, so the order can be fulfilled.

Input: quantities = [5,4,8,11,None,13,4,7,2,None,None,None,1], order_size = 2
Output: False
Explanation: No root-to-leaf path sums to 2, so the order cannot be fulfilled.

EDGE CASE
Input: quantities = [], order_size = 10
Output: False
Explanation: The tree is empty, so return False.

Input: quantities = [5], order_size = 5
Output: True
Explanation: The tree has only one node with value 5, which matches the order size.
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


def can_fulfill_order(inventory, order_size):
    pass
