r"""
TIP102 | Week 9 | Session 2 | Problem Set Version 1 | Problem 5
Larger Order Tree

Source: statement reconstructed from the CodePath solution guide and written in our own words.
The original course page is behind a login, so wording and details may differ slightly.
Solution guide (only after you have tried!): https://github.com/codepath/compsci_guides/wiki/Larger-Order-Tree

PROBLEM
-------
The orders form a BST. Write `larger_order_tree(orders)` that replaces each node's value with itself plus the sum of all values greater than it in the tree, and returns the root.

EXAMPLES (test cases from the solution guide)
---------------------------------------------
HAPPY CASE
Input: 
orders = build_tree([4,1,6,0,2,5,7,None,None,None,3,None,None,None,8])
Output: [30,36,21,36,35,26,15,None,None,None,33,None,None,None,8]
Explanation: The tree is traversed in reverse inorder, updating each node's value to include the sum of all greater nodes.

Input: 
orders = build_tree([2,1,3])
Output: [5,6,3]
Explanation: The tree is updated such that each node's value includes the sum of all greater nodes.

EDGE CASE
Input: orders = None
Output: None
Explanation: The tree is empty, so return None.

Input: orders = build_tree([1])
Output: [1]
Explanation: The tree has only one node, so return the node as-is.
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
    def __init__(self, order_size, left=None, right=None):
        self.val = order_size
        self.left = left
        self.right = right


def larger_order_tree(orders):
    pass
