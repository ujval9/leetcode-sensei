r"""
TIP102 | Week 9 | Session 1 | Problem Set Version 1 | Problem 1
Merging Cookie Orders

Source: statement reconstructed from the CodePath solution guide and written in our own words.
The original course page is behind a login, so wording and details may differ slightly.
Solution guide (only after you have tried!): https://github.com/codepath/compsci_guides/wiki/Merging-Cookie-Orders

PROBLEM
-------
Write `merge_orders(order1, order2)` that merges two binary trees: where both trees have a node, the merged node's value is the sum; where only one has a node, use that node. Return the root of the merged tree.

EXAMPLES (test cases from the solution guide)
---------------------------------------------
HAPPY CASE
Input: order1 = [1, 3, 2, 5], order2 = [2, 1, 3, None, 4, None, 7]
Output: [3, 4, 5, 5, 4, None, 7]
Explanation: The merged tree has summed values where nodes overlap and the non-`None` node where they do not.

Input: order1 = [1, 2], order2 = [3]
Output: [4, 2]
Explanation: The merged tree takes the non-`None` node when there is no overlap.

EDGE CASE
Input: order1 = [], order2 = [1, 2, 3]
Output: [1, 2, 3]
Explanation: Since the first tree is empty, the merged tree is just the second tree.

Input: order1 = [4], order2 = []
Output: [4]
Explanation: Since the second tree is empty, the merged tree is just the first tree.
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

class TreeNode():
     def __init__(self, quantity, left=None, right=None):
        self.val = quantity
        self.left = left
        self.right = right


def merge_orders(order1, order2):
    pass
