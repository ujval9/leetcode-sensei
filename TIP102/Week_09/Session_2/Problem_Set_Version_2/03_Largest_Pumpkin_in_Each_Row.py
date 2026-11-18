r"""
TIP102 | Week 9 | Session 2 | Problem Set Version 2 | Problem 3
Largest Pumpkin in Each Row

Source: statement reconstructed from the CodePath solution guide and written in our own words.
The original course page is behind a login, so wording and details may differ slightly.
Solution guide (only after you have tried!): https://github.com/codepath/compsci_guides/wiki/Largest-Pumpkin-in-Each-Row

PROBLEM
-------
Write `largest_pumpkins(pumpkin_patch)` that returns a list of the largest value on each level of the tree, top to bottom.

EXAMPLES (test cases from the solution guide)
---------------------------------------------
HAPPY CASE
Input: 
    pumpkin_sizes = [1, 3, 2, 5, 3, None, 9]
    pumpkin_patch = build_tree(pumpkin_sizes)
Output: 
    [1, 3, 9]
Explanation: 
    The largest pumpkins in each row are 1, 3, and 9, respectively.

EDGE CASE
Input: 
    pumpkin_sizes = [7]
    pumpkin_patch = build_tree(pumpkin_sizes)
Output: 
    [7]
Explanation: 
    There is only one row with a single pumpkin of size 7.
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
    def __init__(self, val=0, left=None, right=None):
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


def largest_pumpkins(pumpkin_patch):
    pass


if __name__ == "__main__":
    # Example Usage:
    pumpkin_sizes = [1, 3, 2, 5, 3, None, 9]
    pumpkin_patch = build_tree(pumpkin_sizes)

    print(largest_pumpkins(pumpkin_patch))  # [1, 3, 9]
