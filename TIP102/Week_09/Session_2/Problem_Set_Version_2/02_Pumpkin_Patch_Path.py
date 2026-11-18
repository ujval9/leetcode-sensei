r"""
TIP102 | Week 9 | Session 2 | Problem Set Version 2 | Problem 2
Pumpkin Patch Path

Source: statement reconstructed from the CodePath solution guide and written in our own words.
The original course page is behind a login, so wording and details may differ slightly.
Solution guide (only after you have tried!): https://github.com/codepath/compsci_guides/wiki/Pumpkin-Patch-Path

PROBLEM
-------
Each node holds a number of pumpkins. Write `max_pumpkins_path(root)` that returns the list of values along the root-to-leaf path with the largest total.

EXAMPLES (test cases from the solution guide)
---------------------------------------------
HAPPY CASE
Input: 
    pumpkin_quantities = [7, 3, 10, 1, None, 5, 15]
    root1 = build_tree(pumpkin_quantities)
Output: 
    [7, 10, 15]
Explanation: 
    The path from the root (7) through 10 to 15 yields the highest number of pumpkins.

EDGE CASE
Input: 
    pumpkin_quantities = [12, 3, 8, 4, 50, None, 10]
    root2 = build_tree(pumpkin_quantities)
Output: 
    [12, 3, 50]
Explanation: 
    The path from the root (12) through 3 to 50 yields the highest number of pumpkins.
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


def max_pumpkins_path(root):
    pass


if __name__ == "__main__":
    # Example Usage:
    pumpkin_quantities = [7, 3, 10, 1, None, 5, 15]
    root1 = build_tree(pumpkin_quantities)

    pumpkin_quantities = [12, 3, 8, 4, 50, None, 10]
    root2 = build_tree(pumpkin_quantities)

    print(max_pumpkins_path(root1))  # [7, 10, 15]
    print(max_pumpkins_path(root2))  # [12, 3, 50]
