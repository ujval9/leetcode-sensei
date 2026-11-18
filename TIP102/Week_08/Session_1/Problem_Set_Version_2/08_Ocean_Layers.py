r"""
TIP102 | Week 8 | Session 1 | Problem Set Version 2 | Problem 8
Ocean Layers

Source: statement reconstructed from the CodePath solution guide and written in our own words.
The original course page is behind a login, so wording and details may differ slightly.
Solution guide (only after you have tried!): https://github.com/codepath/compsci_guides/wiki/Ocean-Layers

PROBLEM
-------
Write `ocean_depth(root)` that returns the maximum depth of the tree: the number of nodes on the longest root-to-leaf path (0 if empty).

EXAMPLES (test cases from the solution guide)
---------------------------------------------
HAPPY CASE
Input: Binary tree with nodes ["Sunlight", "Twilight", "Abyss", "Trenches", "Anglerfish", "Squid", "Giant Squid"]
Output: 4
Explanation: The longest path is ["Sunlight", "Twilight", "Abyss", "Trenches"], so the depth is 4.

EDGE CASE
Input: Binary tree with only one node ["Sunlight"]
Output: 1
Explanation: The tree has only the root, so the depth is 1.
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


def ocean_depth(root):
    pass
