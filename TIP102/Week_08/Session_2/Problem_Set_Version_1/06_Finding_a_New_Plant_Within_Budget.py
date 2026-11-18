r"""
TIP102 | Week 8 | Session 2 | Problem Set Version 1 | Problem 6
Finding a New Plant Within Budget

Source: statement reconstructed from the CodePath solution guide and written in our own words.
The original course page is behind a login, so wording and details may differ slightly.
Solution guide (only after you have tried!): https://github.com/codepath/compsci_guides/wiki/Finding-a-New-Plant-Within-Budget

PROBLEM
-------
Each BST node has a `key` (price) and a `val` (plant name). Write `pick_plant(root, budget)` that returns the name of the most expensive plant whose price is strictly less than `budget`, or None if none qualifies.

EXAMPLES (test cases from the solution guide)
---------------------------------------------
HAPPY CASE
Input: [(50, "FiddleLeafFig"), (25, "Monstera"), (40, "Pothos"), (70, "SnakePlant"), (60, "Fern"), (80, "ZZPlant")], budget = 50
Output: "Pothos"
Explanation: The highest price below 50 is 40, which corresponds to "Pothos".

EDGE CASE
Input: [(50, "FiddleLeafFig"), (25, "Monstera"), (40, "Pothos"), (70, "SnakePlant"), (60, "Fern"), (80, "ZZPlant")], budget = 15
Output: None
Explanation: There is no plant with a price lower than 15, so the output is `None`.
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
        self.key = key      # Plant price
        self.val = val      # Plant name
        self.left = left
        self.right = right


def pick_plant(root, budget):
    pass
