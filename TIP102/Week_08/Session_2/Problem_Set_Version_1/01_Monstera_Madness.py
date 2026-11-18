r"""
TIP102 | Week 8 | Session 2 | Problem Set Version 1 | Problem 1
Monstera Madness

Source: statement reconstructed from the CodePath solution guide and written in our own words.
The original course page is behind a login, so wording and details may differ slightly.
Solution guide (only after you have tried!): https://github.com/codepath/compsci_guides/wiki/Monstera-Madness

PROBLEM
-------
Each node holds the number of splits in a Monstera leaf. Write `count_odd_splits(root)` that returns how many nodes have an odd value.

EXAMPLES (test cases from the solution guide)
---------------------------------------------
HAPPY CASE
Input: [2, 3, 5, 6, 7, None, 12]
Output: 3
Explanation: Nodes with odd values are 3, 5, and 7. Hence, 3 leaves have odd splits.

EDGE CASE
Input: None
Output: 0
Explanation: An empty tree should return 0 since there are no leaves to count.
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

class TreeNode():
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right


def count_odd_splits(root):
    pass
