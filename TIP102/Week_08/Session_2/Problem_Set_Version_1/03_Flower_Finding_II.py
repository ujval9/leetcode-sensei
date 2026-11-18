r"""
TIP102 | Week 8 | Session 2 | Problem Set Version 1 | Problem 3
Flower Finding II

Source: statement reconstructed from the CodePath solution guide and written in our own words.
The original course page is behind a login, so wording and details may differ slightly.
Solution guide (only after you have tried!): https://github.com/codepath/compsci_guides/wiki/Flower-Finding-II

PROBLEM
-------
Same search as Flower Finding, but the tree is a normal binary tree, not a BST. Write `non_bst_find_flower(root, name)` that returns True if any node has value `name`.

EXAMPLES (test cases from the solution guide)
---------------------------------------------
HAPPY CASE
Input: ["Daisy", "Lily", "Tulip", "Rose", "Violet", "Lilac"], "Lilac"
Output: True
Explanation: "Lilac" exists in the tree as a node.

EDGE CASE
Input: ["Daisy", "Lily", "Tulip", "Rose", "Violet", "Lilac"], "Sunflower"
Output: False
Explanation: "Sunflower" does not exist in the tree, so the output is `False`.
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


def non_bst_find_flower(root, name):
    pass
