r"""
TIP102 | Week 8 | Session 1 | Problem Set Version 1 | Problem 3
Ivy Cutting

Source: statement reconstructed from the CodePath solution guide and written in our own words.
The original course page is behind a login, so wording and details may differ slightly.
Solution guide (only after you have tried!): https://github.com/codepath/compsci_guides/wiki/Ivy-Cutting

PROBLEM
-------
Write `right_vine(root)` that returns a list of the values on the rightmost path: start at the root and keep following the right child until there is none. Solve it iteratively.

EXAMPLES (test cases from the solution guide)
---------------------------------------------
HAPPY CASE
Input: Binary tree where the rightmost path is ["Root", "Node2", "Leaf3"]
Output: ["Root", "Node2", "Leaf3"]
Explanation: The rightmost path is extracted correctly.

EDGE CASE
Input: Binary tree with no right child at any node
Output: ["Root"]
Explanation: The rightmost path consists only of the root node.
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


def right_vine(root):
    pass
