r"""
TIP102 | Week 8 | Session 2 | Problem Set Version 2 | Problem 2
Searching Ariel's Treasures

Source: statement reconstructed from the CodePath solution guide and written in our own words.
The original course page is behind a login, so wording and details may differ slightly.
Solution guide (only after you have tried!): https://github.com/codepath/compsci_guides/wiki/Searching-Ariel's-Treasures

PROBLEM
-------
Ariel's collection is a BST of item names. Write `locate_treasure(grotto, treasure)` that returns True if `treasure` is in the BST, otherwise False.

EXAMPLES (test cases from the solution guide)
---------------------------------------------
HAPPY CASE
Input: grotto = TreeNode("Snarfblat", TreeNode("Gadget", TreeNode("Dinglehopper"), TreeNode("Gizmo")), TreeNode("Whatzit", None, TreeNode("Whozit"))), treasure = "Dinglehopper"
Output: True
Explanation: "Dinglehopper" is present in the tree.

EDGE CASE
Input: grotto = TreeNode("Snarfblat", TreeNode("Gadget", TreeNode("Dinglehopper"), TreeNode("Gizmo")), TreeNode("Whatzit", None, TreeNode("Whozit"))), treasure = "Thingamabob"
Output: False
Explanation: "Thingamabob" is not present in the tree.
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


def locate_treasure(grotto, treasure):
    pass
