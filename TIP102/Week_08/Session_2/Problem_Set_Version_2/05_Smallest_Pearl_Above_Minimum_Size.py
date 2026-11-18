r"""
TIP102 | Week 8 | Session 2 | Problem Set Version 2 | Problem 5
Smallest Pearl Above Minimum Size

Source: statement reconstructed from the CodePath solution guide and written in our own words.
The original course page is behind a login, so wording and details may differ slightly.
Solution guide (only after you have tried!): https://github.com/codepath/compsci_guides/wiki/Smallest-Pearl-Above-Minimum-Size

PROBLEM
-------
Write `pick_pearl(pearls, min_size)` that returns the smallest pearl size in the BST that is strictly greater than `min_size`, or None if there is none.

EXAMPLES (test cases from the solution guide)
---------------------------------------------
HAPPY CASE
Input: pearls = Pearl(3, Pearl(1, None, Pearl(2)), Pearl(5, Pearl(4), Pearl(8))), min_size = 3
Output: 4
Explanation: The smallest pearl greater than 3 is 4.

EDGE CASE
Input: pearls = Pearl(3, Pearl(1, None, Pearl(2)), Pearl(5, Pearl(4), Pearl(8))), min_size = 8
Output: None
Explanation: There is no pearl larger than 8, so the output is `None`.
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
    def __init__(self, size, left=None, right=None):
        self.val = size
        self.left = left
        self.right = right


def pick_pearl(pearls, min_size):
    pass
