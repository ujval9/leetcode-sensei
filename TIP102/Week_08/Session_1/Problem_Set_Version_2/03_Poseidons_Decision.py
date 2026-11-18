r"""
TIP102 | Week 8 | Session 1 | Problem Set Version 2 | Problem 3
Poseidon's Decision

Source: statement reconstructed from the CodePath solution guide and written in our own words.
The original course page is behind a login, so wording and details may differ slightly.
Solution guide (only after you have tried!): https://github.com/codepath/compsci_guides/wiki/Poseidon's-Decision

PROBLEM
-------
The tree is a full binary tree: leaves hold True or False and internal nodes hold "AND" or "OR". Write `get_decision(root)` that evaluates the tree and returns the resulting boolean.

EXAMPLES (test cases from the solution guide)
---------------------------------------------
HAPPY CASE
Input: Binary tree with root "OR" and children "True", "False"
Output: True
Explanation: The evaluation of "OR" with "True" and "False" is `True`.

EDGE CASE
Input: Binary tree with root "False" and no children
Output: False
Explanation: The root is a leaf node with value `False`, so it directly returns `False`.
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


def get_decision(root):
    pass
