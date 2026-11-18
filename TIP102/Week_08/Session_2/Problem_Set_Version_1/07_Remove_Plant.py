r"""
TIP102 | Week 8 | Session 2 | Problem Set Version 1 | Problem 7
Remove Plant

Source: statement reconstructed from the CodePath solution guide and written in our own words.
The original course page is behind a login, so wording and details may differ slightly.
Solution guide (only after you have tried!): https://github.com/codepath/compsci_guides/wiki/Remove-Plant

PROBLEM
-------
The collection is a BST ordered alphabetically. Write `remove_plant(collection, name)` that deletes the node with value `name` while keeping it a valid BST, and returns the root. When the node has two children, replace it with the in-order predecessor (largest value in its left subtree).

EXAMPLES (test cases from the solution guide)
---------------------------------------------
HAPPY CASE
Input: 
      collection = TreeNode("Monstera", 
                  TreeNode("MoneyTree", None, TreeNode("Pothos")),
                  TreeNode("Pilea", TreeNode("Hoya"), TreeNode("Ivy"))),
      name = "Pilea"
Output: Updated BST with "Pilea" removed, replaced by its inorder predecessor.
Explanation: "Pilea" has two children, so it's replaced by the inorder predecessor "Hoya".

EDGE CASE
Input: 
      collection = TreeNode("Monstera", 
                  TreeNode("MoneyTree", None, TreeNode("Pothos")),
                  TreeNode("Pilea", TreeNode("Hoya"), TreeNode("Ivy"))),
      name = "Monstera"
Output: Updated BST with "Monstera" removed, replaced by its inorder predecessor.
Explanation: "Monstera" is the root with two children, so it's replaced by the inorder predecessor "Pothos" (the rightmost node in its left subtree).
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


def remove_plant(collection, name):
    pass
