r"""
TIP102 | Week 8 | Session 2 | Problem Set Version 2 | Problem 3
Add New Treasure to Collection

Source: statement reconstructed from the CodePath solution guide and written in our own words.
The original course page is behind a login, so wording and details may differ slightly.
Solution guide (only after you have tried!): https://github.com/codepath/compsci_guides/wiki/Add-New-Treasure-to-Collection

PROBLEM
-------
Write `add_treasure(grotto, new_item)` that inserts `new_item` into the BST in the correct position and returns the root. If the item already exists, leave the tree unchanged.

EXAMPLES (test cases from the solution guide)
---------------------------------------------
HAPPY CASE
Input: 
      grotto = TreeNode("Snarfblat", TreeNode("Gadget", TreeNode("Dinglehopper"), TreeNode("Gizmo")), TreeNode("Whatzit", None, TreeNode("Whozit"))), 
      new_item = "Thingamabob"
Output: Updated BST with "Thingamabob" added in the correct position.
Explanation: "Thingamabob" is added as the left child of "Whatzit".

EDGE CASE
Input: 
      grotto = TreeNode("Snarfblat", TreeNode("Gadget", TreeNode("Dinglehopper"), TreeNode("Gizmo")), TreeNode("Whatzit", None, TreeNode("Whozit"))), 
      new_item = "Gizmo"
Output: The original BST since "Gizmo" already exists in the tree.
Explanation: No changes are made because "Gizmo" is already in the tree.
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


def add_treasure(grotto, new_item):
    pass
