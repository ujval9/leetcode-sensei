r"""
TIP102 | Week 9 | Session 2 | Problem Set Version 1 | Problem 6
Find Next Order to Fulfill Today

Source: statement reconstructed from the CodePath solution guide and written in our own words.
The original course page is behind a login, so wording and details may differ slightly.
Solution guide (only after you have tried!): https://github.com/codepath/compsci_guides/wiki/Find-Next-Order-to-Fulfill-Today

PROBLEM
-------
Write `find_next_order(order_tree, order)` that returns the node immediately to the right of `order` on the same level of the tree, or None if `order` is the last on its level.

EXAMPLES (test cases from the solution guide)
---------------------------------------------
HAPPY CASE
Input: 
cupcakes = TreeNode("Cupcakes")
macaron = TreeNode("Macaron")
cookies = TreeNode("Cookies")
cake = TreeNode("Cake")
eclair = TreeNode("Eclair")
croissant = TreeNode("Croissant")

cupcakes.left, cupcakes.right = macaron, cookies
macaron.right = cake
cookies.left, cookies.right = eclair, croissant

next_order1 = find_next_order(cupcakes, cake)
next_order2 = find_next_order(cupcakes, cookies)

Output: Eclair, None
Explanation: 
* The next order after Cake on the same level is Eclair.
* Cookies is the last order on its level, so return None.

EDGE CASE
Input: order_tree = None, order = None
Output: None
Explanation: The tree is empty, so return None.

Input: order_tree = TreeNode("Cupcakes"), order = TreeNode("Cupcakes")
Output: None
Explanation: There is only one order in the tree, so return None.
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
    def __init__(self, order, left=None, right=None):
        self.val = order
        self.left = left
        self.right = right


def find_next_order(order_tree, order):
    pass
