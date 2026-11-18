r"""
TIP102 | Week 9 | Session 2 | Problem Set Version 1 | Problem 1
Balanced Baked Goods Display

Source: statement reconstructed from the CodePath solution guide and written in our own words.
The original course page is behind a login, so wording and details may differ slightly.
Solution guide (only after you have tried!): https://github.com/codepath/compsci_guides/wiki/Balanced-Baked-Goods-Display

PROBLEM
-------
Write `is_balanced(display)` that returns True if, for every node, the heights of its left and right subtrees differ by at most 1.

EXAMPLES (test cases from the solution guide)
---------------------------------------------
HAPPY CASE
Input: 
    baked_goods = ["🎂", "🥮", "🍩", "🥖", "🧁"]
    display1 = build_tree(baked_goods)
Output: 
    True
Explanation: 
    The tree is balanced because the difference in height between the left and right subtrees for every node does not exceed 1.

EDGE CASE
Input: 
    baked_goods = ["🥖", "🧁", "🧁", "🍪", None, None, "🍪", "🥐", None, None, "🥐"]
    display2 = build_tree(baked_goods)
Output: 
    False
Explanation: 
    The tree is not balanced because the height difference between the left and right subtrees at some nodes exceeds 1.
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


def is_balanced(display):
    pass


if __name__ == "__main__":
    # Example Usage:
    baked_goods = ["🎂", "🥮", "🍩", "🥖", "🧁"]
    display1 = build_tree(baked_goods)

    baked_goods = ["🥖", "🧁", "🧁", "🍪", None, None, "🍪", "🥐", None, None, "🥐"]
    display2 = build_tree(baked_goods)

    print(is_balanced(display1))  # True
    print(is_balanced(display2))  # False
