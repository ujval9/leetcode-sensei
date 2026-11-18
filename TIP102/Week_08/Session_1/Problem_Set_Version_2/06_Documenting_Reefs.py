r"""
TIP102 | Week 8 | Session 1 | Problem Set Version 2 | Problem 6
Documenting Reefs

Source: statement reconstructed from the CodePath solution guide and written in our own words.
The original course page is behind a login, so wording and details may differ slightly.
Solution guide (only after you have tried!): https://github.com/codepath/compsci_guides/wiki/Documenting-Reefs

PROBLEM
-------
Write `explore_reef(root)` that returns the node values in preorder (root, left, right).

EXAMPLES (test cases from the solution guide)
---------------------------------------------
HAPPY CASE
Input: Binary tree with nodes ["CoralA", "CoralB", "CoralD", "CoralE", "CoralC"]
Output: ["CoralA", "CoralB", "CoralD", "CoralE", "CoralC"]
Explanation: The preorder traversal visits the nodes in the correct order.

EDGE CASE
Input: Binary tree with only one node ["CoralA"]
Output: ["CoralA"]
Explanation: The tree only has a root, so the output is just the root's value.
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


def explore_reef(root):
    pass
