r"""
TIP102 | Week 9 | Session 2 | Problem Set Version 2 | Problem 1
Haunted Mirror

Source: statement reconstructed from the CodePath solution guide and written in our own words.
The original course page is behind a login, so wording and details may differ slightly.
Solution guide (only after you have tried!): https://github.com/codepath/compsci_guides/wiki/Haunted-Mirror

PROBLEM
-------
Two trees are mirror-equivalent if one can be turned into the other by swapping left and right children at any number of nodes. Write `mirror_tree(order1, order2)` that returns True if they are.

EXAMPLES (test cases from the solution guide)
---------------------------------------------
HAPPY CASE
Input: 
    body_parts = ["🧛‍♂️", "💪🏼", "🤳", "👟", None, None, "👞"]
    vampire = build_tree(body_parts)
Output: 
    ['🧛‍♂️', '🤳', '💪🏼', '👞', None, None, '👟']
Explanation: 
    The tree is mirrored by swapping the left and right children of all nodes.

EDGE CASE
Input: 
    spooky_objects = ["🎃", "😈", "🕸️", None, None, "🧟‍♂️", "👻"]
    spooky_tree = build_tree(spooky_objects)
Output: 
    ['🎃', '🕸️', '😈', '👻', '🧟‍♂️']
Explanation: 
    The tree is mirrored by swapping the left and right children of all nodes.
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

class TreeNode():
    def __init__(self, flavor, left=None, right=None):
        self.val = flavor
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


def mirror_tree(order1, order2):
    pass


if __name__ == "__main__":
    # Example Usage:
    flavors1 = ["Red Velvet", "Vanilla", "Lemon", "Ube", "Almond", "Chai", "Carrot", None, None, None, None, "Chai", "Maple", None, "Smore"]
    flavors2 = ["Red Velvet", "Lemon", "Vanilla", "Carrot", "Chai", "Almond", "Ube", "Smore", None, "Maple", "Chai"]
    order1 = build_tree(flavors1)
    order2 = build_tree(flavors2)

    print(mirror_tree(order1, order2))  # True
