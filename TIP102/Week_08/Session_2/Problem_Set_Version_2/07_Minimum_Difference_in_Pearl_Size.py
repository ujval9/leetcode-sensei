r"""
TIP102 | Week 8 | Session 2 | Problem Set Version 2 | Problem 7
Minimum Difference in Pearl Size

Source: statement reconstructed from the CodePath solution guide and written in our own words.
The original course page is behind a login, so wording and details may differ slightly.
Solution guide (only after you have tried!): https://github.com/codepath/compsci_guides/wiki/Minimum-Difference-in-Pearl-Size

PROBLEM
-------
Write `min_diff_in_pearl_sizes(pearls)` that returns the minimum difference between the values of any two different nodes in a BST.

EXAMPLES (test cases from the solution guide)
---------------------------------------------
HAPPY CASE
Input: pearls = Pearl(4, Pearl(2, Pearl(1), Pearl(3)), Pearl(6, None, Pearl(8)))
Output: 1
Explanation: The smallest difference is between the sizes 3 and 4 or between 2 and 3, both of which have a difference of 1.

EDGE CASE
Input: pearls = Pearl(4)
Output: Infinity or some large value depending on implementation
Explanation: With only one pearl, there is no difference to calculate.
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

class Pearl:
    def __init__(self, size=0, left=None, right=None):
        self.val = size
        self.left = left
        self.right = right


def min_diff_in_pearl_sizes(pearls):
    pass
