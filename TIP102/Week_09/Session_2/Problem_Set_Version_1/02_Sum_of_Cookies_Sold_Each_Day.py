r"""
TIP102 | Week 9 | Session 2 | Problem Set Version 1 | Problem 2
Sum of Cookies Sold Each Day

Source: statement reconstructed from the CodePath solution guide and written in our own words.
The original course page is behind a login, so wording and details may differ slightly.
Solution guide (only after you have tried!): https://github.com/codepath/compsci_guides/wiki/Sum-of-Cookies-Sold-Each-Day

PROBLEM
-------
Write `sum_each_days_orders(orders)` that returns a list where element i is the sum of all node values on level i of the tree.

EXAMPLES (test cases from the solution guide)
---------------------------------------------
HAPPY CASE
Input: 
    order_sizes = [4, 2, 6, 1, 3]
    orders = build_tree(order_sizes)
Output: 
    [4, 8, 4]
Explanation: 
    The sum of cookies ordered on each day (level) is [4] on day 1, [2 + 6] on day 2, and [1 + 3] on day 3.

EDGE CASE
Input: 
    order_sizes = [5]
    orders = build_tree(order_sizes)
Output: 
    [5]
Explanation: 
    The tree contains only one node, so the sum is just the value of that node.
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


def sum_each_days_orders(orders):
    pass


if __name__ == "__main__":
    # Example Usage:
    order_sizes = [4, 2, 6, 1, 3]
    orders = build_tree(order_sizes)

    print(sum_each_days_orders(orders))  # [4, 8, 4]
