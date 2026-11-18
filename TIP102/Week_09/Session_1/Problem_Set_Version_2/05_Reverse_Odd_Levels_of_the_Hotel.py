r"""
TIP102 | Week 9 | Session 1 | Problem Set Version 2 | Problem 5
Reverse Odd Levels of the Hotel

Source: statement reconstructed from the CodePath solution guide and written in our own words.
The original course page is behind a login, so wording and details may differ slightly.
Solution guide (only after you have tried!): https://github.com/codepath/compsci_guides/wiki/Reverse-Odd-Levels-of-the-Hotel

PROBLEM
-------
The hotel is a perfect binary tree. Write `reverse_odd_levels(root)` that reverses the order of the node values on every odd level (the root is level 0) and returns the root.

EXAMPLES (test cases from the solution guide)
---------------------------------------------
HAPPY CASE
Input: Perfect binary tree with level order values [2, 3, 5, 8, 13, 21, 34]
Output: Tree with level order values [2, 5, 3, 8, 13, 21, 34]
Explanation: Level 1 holds [3, 5], which reverses to [5, 3]. Level 2 is even, so it is unchanged.

Input: Perfect binary tree with level order values [7, 13, 11]
Output: Tree with level order values [7, 11, 13]
Explanation: Level 1 holds [13, 11], which reverses to [11, 13].

EDGE CASE
Input: Tree with a single room [5]
Output: Tree with a single room [5]
Explanation: There are no odd levels, so nothing changes.
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

from collections import deque


class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right


def reverse_odd_levels(root):
    pass
