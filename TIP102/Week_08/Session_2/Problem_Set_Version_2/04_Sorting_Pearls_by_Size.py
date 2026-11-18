r"""
TIP102 | Week 8 | Session 2 | Problem Set Version 2 | Problem 4
Sorting Pearls by Size

Source: statement reconstructed from the CodePath solution guide and written in our own words.
The original course page is behind a login, so wording and details may differ slightly.
Solution guide (only after you have tried!): https://github.com/codepath/compsci_guides/wiki/Sorting-Pearls-by-Size

PROBLEM
-------
Each BST node holds a pearl size. Write `smallest_to_largest_iterative(pearls)` that returns all sizes in ascending order, using an iterative inorder traversal (no recursion).

EXAMPLES (test cases from the solution guide)
---------------------------------------------
HAPPY CASE
Input: pearls = Pearl(3, Pearl(1, None, Pearl(2)), Pearl(5, Pearl(4), Pearl(8)))
Output: [1, 2, 3, 4, 5, 8]
Explanation: The pearls are sorted in ascending order using an inorder traversal.

EDGE CASE
Input: pearls = None
Output: []
Explanation: An empty tree should return an empty list.
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


def smallest_to_largest_iterative(pearls):
    pass
