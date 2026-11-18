r"""
TIP102 | Week 8 | Session 1 | Problem Set Version 1 | Problem 6
Pruning Plans

Source: statement reconstructed from the CodePath solution guide and written in our own words.
The original course page is behind a login, so wording and details may differ slightly.
Solution guide (only after you have tried!): https://github.com/codepath/compsci_guides/wiki/Pruning-Plans

PROBLEM
-------
Write `survey_tree(root)` that returns a list of node values in postorder (left, right, root). Return an empty list for an empty tree.

EXAMPLES (test cases from the solution guide)
---------------------------------------------
HAPPY CASE
Input: Binary tree with nodes ["Leaf1", "Node1", "Leaf2", "Leaf3", "Node2", "Root"]
Output: ["Leaf1", "Node1", "Leaf2", "Leaf3", "Node2", "Root"]
Explanation: The postorder traversal visits the nodes in the correct order.

EDGE CASE
Input: Binary tree with only one node
Output: ["Root"]
Explanation: The single node is the root and is returned as the only element.
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


def survey_tree(root):
    pass
