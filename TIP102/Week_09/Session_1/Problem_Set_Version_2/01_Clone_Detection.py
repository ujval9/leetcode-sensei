r"""
TIP102 | Week 9 | Session 1 | Problem Set Version 2 | Problem 1
Clone Detection

Source: statement reconstructed from the CodePath solution guide and written in our own words.
The original course page is behind a login, so wording and details may differ slightly.
Solution guide (only after you have tried!): https://github.com/codepath/compsci_guides/wiki/Clone-Detection

PROBLEM
-------
Write `is_clone(guest1, guest2)` that returns True if the two binary trees have exactly the same structure and values, otherwise False.

EXAMPLES (test cases from the solution guide)
---------------------------------------------
HAPPY CASE
Input: guest1 = TreeNode("John Doe", TreeNode("6 ft"), TreeNode("Brown Eyes")), 
       guest2 = TreeNode("John Doe", TreeNode("6 ft"), TreeNode("Brown Eyes"))
Output: True
Explanation: The trees have identical structure and values.

Input: guest3 = TreeNode("John Doe", TreeNode("6 ft")),
       guest4 = TreeNode("John Doe", None, TreeNode("6 ft"))
Output: False
Explanation: The trees have the same values but different structures, so they are not clones.

EDGE CASE
Input: guest1 = None, guest2 = None
Output: True
Explanation: Both trees are empty, so they are clones.

Input: guest1 = TreeNode("John Doe"), guest2 = None
Output: False
Explanation: One tree is empty, and the other is not, so they are not clones.
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


def is_clone(guest1, guest2):
    pass
