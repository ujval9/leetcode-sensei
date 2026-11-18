r"""
TIP102 | Week 8 | Session 2 | Problem Set Version 1 | Problem 5
Sorting Plants by Rarity

Source: statement reconstructed from the CodePath solution guide and written in our own words.
The original course page is behind a login, so wording and details may differ slightly.
Solution guide (only after you have tried!): https://github.com/codepath/compsci_guides/wiki/Sorting-Plants-by-Rarity

PROBLEM
-------
Each BST node has a `key` (rarity) and a `val` (plant name). Write `sort_plants(collection)` that returns a list of (key, val) tuples sorted from least to most rare.

EXAMPLES (test cases from the solution guide)
---------------------------------------------
HAPPY CASE
Input: [(3, "Monstera"), (1, "Pothos"), (2, "Spider Plant"), (5, "Witchcraft Orchid"), (4, "Hoya Motoskei")]
Output: [(1, "Pothos"), (2, "Spider Plant"), (3, "Monstera"), (4, "Hoya Motoskei"), (5, "Witchcraft Orchid")]
Explanation: The plants are sorted by rarity in ascending order.

EDGE CASE
Input: None
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

class TreeNode:
    def __init__(self, key, val, left=None, right=None):
        self.key = key    # Plant's rarity (BST ordering key)
        self.val = val    # Plant's name
        self.left = left
        self.right = right


def sort_plants(collection):
    pass
