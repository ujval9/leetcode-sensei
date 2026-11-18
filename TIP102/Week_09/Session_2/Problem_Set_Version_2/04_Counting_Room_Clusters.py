r"""
TIP102 | Week 9 | Session 2 | Problem Set Version 2 | Problem 4
Counting Room Clusters

Source: statement reconstructed from the CodePath solution guide and written in our own words.
The original course page is behind a login, so wording and details may differ slightly.
Solution guide (only after you have tried!): https://github.com/codepath/compsci_guides/wiki/Counting-Room-Clusters

PROBLEM
-------
Each node holds a room theme. A cluster is a group of connected nodes (parent and child) that share the same theme. Write `count_clusters(hotel)` that returns the number of clusters.

EXAMPLES (test cases from the solution guide)
---------------------------------------------
HAPPY CASE
Input: 
    themes = ["👻", "👻", "🧛🏾", "👻", "🧛🏾", None, "🧛🏾"]
    hotel = build_tree(themes)
Output: 
    3
Explanation: 
    There are three distinct clusters: one cluster of "👻" and two clusters of "🧛🏾".

EDGE CASE
Input: 
    themes = ["👻", "👻", "👻", "👻", "👻"]
    hotel = build_tree(themes)
Output: 
    1
Explanation: 
    There is only one distinct cluster, as all rooms have the same theme.
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


def count_clusters(hotel):
    pass


if __name__ == "__main__":
    # Example Usage:
    themes = ["👻", "👻", "🧛🏾", "👻", "🧛🏾", None, "🧛🏾"]
    hotel = build_tree(themes)

    print(count_clusters(hotel))  # 3
