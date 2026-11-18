r"""
TIP102 | Week 8 | Session 1 | Problem Set Version 1 | Problem 8
Flower Fields

Source: statement reconstructed from the CodePath solution guide and written in our own words.
The original course page is behind a login, so wording and details may differ slightly.
Solution guide (only after you have tried!): https://github.com/codepath/compsci_guides/wiki/Flower-Fields

PROBLEM
-------
Write `find_flower(root, flower)` that returns True if any node in the binary tree has the value `flower`, otherwise False.

EXAMPLES (test cases from the solution guide)
---------------------------------------------
HAPPY CASE
Input: Binary tree with flowers ["Rose", "Lily", "Daisy", "Orchid", "Lilac", "Dahlia"] and target "Lilac"
Output: True
Explanation: The flower "Lilac" exists in the tree.

EDGE CASE
Input: Binary tree with flowers ["Rose", "Lily", "Daisy", "Orchid", "Lilac", "Dahlia"] and target "Hibiscus"
Output: False
Explanation: The flower "Hibiscus" does not exist in the tree.
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


def find_flower(root, flower):
    pass
