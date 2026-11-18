r"""
TIP102 | Week 8 | Session 1 | Problem Set Version 2 | Problem 4
Escaping the Sea Caves

Source: statement reconstructed from the CodePath solution guide and written in our own words.
The original course page is behind a login, so wording and details may differ slightly.
Solution guide (only after you have tried!): https://github.com/codepath/compsci_guides/wiki/Escaping-the-Sea-Caves

PROBLEM
-------
Write `leftmost_path(root)` that returns the list of values from the root following left children until there is no left child. Solve it iteratively.

EXAMPLES (test cases from the solution guide)
---------------------------------------------
HAPPY CASE
Input: Binary tree with nodes ["CaveA", "CaveB", "CaveD", "CaveE", "CaveC", "CaveF"]
Output: ["CaveA", "CaveB", "CaveD"]
Explanation: The leftmost path is ["CaveA", "CaveB", "CaveD"].

EDGE CASE
Input: Binary tree with nodes ["CaveA", "CaveB", "CaveC"] where each node has only a right child.
Output: ["CaveA"]
Explanation: The root has no left children, so the path only includes the root.
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


def leftmost_path(root):
    pass
