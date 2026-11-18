r"""
TIP102 | Week 8 | Session 2 | Problem Set Version 1 | Problem 4
Adding a New Plant to the Collection

Source: statement reconstructed from the CodePath solution guide and written in our own words.
The original course page is behind a login, so wording and details may differ slightly.
Solution guide (only after you have tried!): https://github.com/codepath/compsci_guides/wiki/Adding-a-New-Plant-to-the-Collection

PROBLEM
-------
The collection is a BST ordered alphabetically by plant name. Write `add_plant(collection, name)` that inserts a new node with `name` in the correct position and returns the root.

EXAMPLES (test cases from the solution guide)
---------------------------------------------
HAPPY CASE
Input: ["Monstera", "FiddleLeafFig", "SnakePlant"], "Aloe"
Output: The updated BST with "Aloe" as the left child of "FiddleLeafFig".
Explanation: The tree is updated to include "Aloe" while maintaining the BST properties.

EDGE CASE
Input: [], "Aloe"
Output: A new tree with "Aloe" as the root.
Explanation: An empty tree should return a new tree with only the "Aloe" node.
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


def add_plant(collection, name):
    pass
