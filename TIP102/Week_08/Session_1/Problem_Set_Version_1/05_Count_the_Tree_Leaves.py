r"""
TIP102 | Week 8 | Session 1 | Problem Set Version 1 | Problem 5
Count the Tree Leaves

Source: statement reconstructed from the CodePath solution guide and written in our own words.
The original course page is behind a login, so wording and details may differ slightly.
Solution guide (only after you have tried!): https://github.com/codepath/compsci_guides/wiki/Count-the-Tree-Leaves

PROBLEM
-------
Write `count_leaves(root)` that returns the number of leaf nodes (nodes with no children) in a binary tree. Return 0 for an empty tree.

EXAMPLES (test cases from the solution guide)
---------------------------------------------
HAPPY CASE
Input: A binary tree with three leaf nodes
Output: 3
Explanation: The function correctly counts the number of leaf nodes.

EDGE CASE
Input: A binary tree consisting of only the root node
Output: 1
Explanation: The root itself is counted as a leaf node since it has no children.
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


def count_leaves(root):
    pass
