r"""
TIP102 | Week 8 | Session 2 | Problem Set Version 2 | Problem 6
Remove Invasive Species

Source: statement reconstructed from the CodePath solution guide and written in our own words.
The original course page is behind a login, so wording and details may differ slightly.
Solution guide (only after you have tried!): https://github.com/codepath/compsci_guides/wiki/Remove-Invasive-Species

PROBLEM
-------
The ecosystem is a BST ordered alphabetically by species name. Write `remove_species(root, name)` that deletes the node with value `name` while keeping it a valid BST, and returns the root. When the node has two children, replace it with its in-order successor (smallest value in its right subtree).

EXAMPLES (test cases from the solution guide)
---------------------------------------------
HAPPY CASE
Input: 
      ecosystem = TreeNode("Dugong", 
                  TreeNode("BrainCoral", None, TreeNode("Clownfish")),
                  TreeNode("Lionfish", TreeNode("GiantClam"), TreeNode("Seagrass"))), 
      name = "Lionfish"
Output: Updated BST with "Lionfish" removed and replaced by its inorder successor.
Explanation: "Lionfish" has two children, so it's replaced by the inorder successor "Seagrass".

EDGE CASE
Input: 
      ecosystem = TreeNode("Dugong", 
                  TreeNode("BrainCoral", None, TreeNode("Clownfish")),
                  TreeNode("Lionfish", TreeNode("GiantClam"), TreeNode("Seagrass"))), 
      name = "Dugong"
Output: Updated BST with "Dugong" removed and replaced by its inorder successor.
Explanation: "Dugong" is the root with two children, so it's replaced by the inorder successor "GiantClam".
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


def remove_species(ecosystem, name):
    pass
