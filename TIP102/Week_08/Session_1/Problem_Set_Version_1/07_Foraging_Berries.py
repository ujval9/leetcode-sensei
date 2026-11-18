r"""
TIP102 | Week 8 | Session 1 | Problem Set Version 1 | Problem 7
Foraging Berries

Source: statement reconstructed from the CodePath solution guide and written in our own words.
The original course page is behind a login, so wording and details may differ slightly.
Solution guide (only after you have tried!): https://github.com/codepath/compsci_guides/wiki/Foraging-Berries

PROBLEM
-------
Each node holds a number of berries. Write `harvest_berries(root, threshold)` that returns the sum of berries over all nodes whose count is strictly greater than `threshold`.

EXAMPLES (test cases from the solution guide)
---------------------------------------------
HAPPY CASE
Input: Binary tree with nodes [4, 10, 6, 5, 8, 20] and threshold 6
Output: 38
Explanation: Nodes with values greater than 6 are 8, 10, and 20. Their sum is 38.

EDGE CASE
Input: Binary tree with nodes [4, 10, 6, 5, 8, 20] and threshold 30
Output: 0
Explanation: No nodes have a value greater than 30.
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


def harvest_berries(root, threshold):
    pass
