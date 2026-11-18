r"""
TIP102 | Week 9 | Session 1 | Problem Set Version 2 | Problem 6
Kth Spookiest Room in the Hotel

Source: statement reconstructed from the CodePath solution guide and written in our own words.
The original course page is behind a login, so wording and details may differ slightly.
Solution guide (only after you have tried!): https://github.com/codepath/compsci_guides/wiki/Kth-Spookiest-Room-in-the-Hotel

PROBLEM
-------
The hotel is a BST of room spookiness values. Write `kth_spookiest(root, k)` that returns the k-th smallest value (1-indexed).

EXAMPLES (test cases from the solution guide)
---------------------------------------------
HAPPY CASE
Input: 
hotel1 = build_tree([(3, "Lobby"), (1, 101), (4, 102), None, (2, 201)]), k = 1
Output: 101
Explanation: The room with key 1 (spookiest) is room 101.

Input: 
hotel2 = build_tree([(5, 'Lobby'), (3, 101), (6, 102), (2, 201), (4, 202), None, None, (1, 301)]), k = 3
Output: 101
Explanation: The room with key 3 (third spookiest) is room 101.

EDGE CASE
Input: root = None, k = 1
Output: None
Explanation: The tree is empty, so there is no such room.

Input: root = build_tree([(3, "Lobby"), (1, 101), (4, 102)]), k = 5
Output: None
Explanation: k is greater than the number of nodes, so return None.
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
    def __init__(self, key, value, left=None, right=None):
        self.key = key
        self.val = value
        self.left = left
        self.right = right


def kth_spookiest(root, k):
    pass
