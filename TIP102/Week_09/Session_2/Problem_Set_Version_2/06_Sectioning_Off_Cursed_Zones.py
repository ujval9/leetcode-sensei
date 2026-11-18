r"""
TIP102 | Week 9 | Session 2 | Problem Set Version 2 | Problem 6
Sectioning Off Cursed Zones

Source: statement reconstructed from the CodePath solution guide and written in our own words.
The original course page is behind a login, so wording and details may differ slightly.
Solution guide (only after you have tried!): https://github.com/codepath/compsci_guides/wiki/Sectioning-Off-Cursed-Zones

PROBLEM
-------
Write `smallest_subtree_with_deepest_rooms(hotel)` that returns the root of the smallest subtree that contains every deepest node in the tree.

EXAMPLES (test cases from the solution guide)
---------------------------------------------
HAPPY CASE
Input: 
    rooms = ["Lobby", 101, 102, 201, 202, 203, 204, None, None, "😱", "👻"]
    hotel1 = build_tree(rooms)
Output: 
    [202, '😱', '👻']
Explanation: 
    The subtree rooted at node `202` contains all the deepest nodes "😱" and "👻".

EDGE CASE
Input: 
    rooms = ["Lobby", 101, 102, None, "💀"]
    hotel2 = build_tree(rooms)
Output: 
    ['💀']
Explanation: 
    The deepest node is "💀", so the subtree rooted at "💀" is the smallest subtree containing all deepest nodes.
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


# Helper for testing (added): prints a tree's values in level order, None for gaps
def print_tree(root):
    if not root:
        print([])
        return
    out, queue = [], [root]
    while queue:
        node = queue.pop(0)
        if node:
            out.append(node.val if hasattr(node, "val") else node.value)
            queue.append(node.left)
            queue.append(node.right)
        else:
            out.append(None)
    while out and out[-1] is None:
        out.pop()
    print(out)


def smallest_subtree_with_deepest_rooms(hotel):
    pass


if __name__ == "__main__":
    # Example Usage:
    rooms = ["Lobby", 101, 102, 201, 202, 203, 204, None, None, "😱", "👻"]
    hotel1 = build_tree(rooms)

    rooms = ["Lobby", 101, 102, None, "💀"]
    hotel2 = build_tree(rooms)

    print_tree(smallest_subtree_with_deepest_rooms(hotel1))  # [202, '😱', '👻']
    print_tree(smallest_subtree_with_deepest_rooms(hotel2))  # ['💀']
