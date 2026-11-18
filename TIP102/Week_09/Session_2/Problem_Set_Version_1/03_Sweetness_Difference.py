r"""
TIP102 | Week 9 | Session 2 | Problem Set Version 1 | Problem 3
Sweetness Difference

Source: statement reconstructed from the CodePath solution guide and written in our own words.
The original course page is behind a login, so wording and details may differ slightly.
Solution guide (only after you have tried!): https://github.com/codepath/compsci_guides/wiki/Sweetness-Difference

PROBLEM
-------
Write `sweet_difference(chocolates)` that returns a list where element i is the difference between the largest and smallest values on level i of the tree.

EXAMPLES (test cases from the solution guide)
---------------------------------------------
HAPPY CASE
Input: 
    sweetness_levels = [3, 9, 20, None, None, 15, 7]
    chocolate_box = build_tree(sweetness_levels)
Output: 
    [0, 11, 8]
Explanation: 
    The sweetness differences are [0] for the root, [20 - 9 = 11] for the second level, and [15 - 7 = 8] for the third level.

EDGE CASE
Input: 
    sweetness_levels = [5]
    chocolate_box = build_tree(sweetness_levels)
Output: 
    [0]
Explanation: 
    The tree contains only one node, so the difference is 0.
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
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Helper for testing (added): builds a tree from a level-order list, None = missing child
def build_tree(values):
    if not values or values[0] is None:
        return None
    root = TreeNode(values[0])
    queue = [root]
    i = 1
    while queue and i < len(values):
        node = queue.pop(0)
        if i < len(values) and values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1
        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1
    return root


def sweet_difference(chocolates):
    pass


if __name__ == "__main__":
    # Example Usage:
    sweetness_levels = [3, 9, 20, None, None, 15, 7]
    chocolate_box = build_tree(sweetness_levels)

    print(sweet_difference(chocolate_box))  # [0, 11, 8]
