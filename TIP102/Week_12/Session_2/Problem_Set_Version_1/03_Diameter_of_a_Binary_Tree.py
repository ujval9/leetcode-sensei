r"""
TIP102 | Week 12 | Session 2 | Problem Set Version 1 | Problem 3
Diameter of a Binary Tree

Source: statement reconstructed from the CodePath solution guide and written in our own words.
The original course page is behind a login, so wording and details may differ slightly.
Solution guide (only after you have tried!): https://github.com/codepath/compsci_guides/wiki/Diameter-of-a-Binary-Tree

PROBLEM
-------
Write `tree_diameter(root)` that returns the length (in edges) of the longest path between any two nodes in the binary tree. The path does not have to go through the root.

EXAMPLES (test cases from the solution guide)
---------------------------------------------
HAPPY CASE
Input: 
    1                
   /  \         
  2    3    
 / \        
4   5      

Output: 3
Explanation: Longest path is [4, 2, 1, 3] or [5, 2, 1, 3].

Input: 
   1
  /
 2

Output: 1
Explanation: The longest path is [2, 1].
EDGE CASE
Input: root = None
Output: 0
Explanation: An empty tree has a diameter of 0.

Input: root = TreeNode(1)
Output: 0
Explanation: A single node tree has no edges, so the diameter is 0.
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


def tree_diameter(root):
    pass
