r"""
TIP102 | Week 8 | Session 2 | Problem Set Version 1 | Problem 2
Flower Finding

Source: statement reconstructed from the CodePath solution guide and written in our own words.
The original course page is behind a login, so wording and details may differ slightly.
Solution guide (only after you have tried!): https://github.com/codepath/compsci_guides/wiki/Flower-Finding

PROBLEM
-------
The plant inventory is a binary search tree ordered alphabetically by name. Write `find_flower(inventory, name)` that returns True if `name` is in the BST, using the BST property to search efficiently.

EXAMPLES (test cases from the solution guide)
---------------------------------------------
HAPPY CASE
Input: ["Rose", "Lilac", "Tulip", "Daisy", "Lily", None, "Violet"], "Lilac"
Output: True
Explanation: "Lilac" exists in the tree as a node.

EDGE CASE
Input: ["Rose", "Lilac", "Tulip", "Daisy", "Lily", None, "Violet"], "Sunflower"
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

class TreeNode():
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right


def find_flower(inventory, name):
    pass
