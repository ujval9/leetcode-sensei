r"""
TIP102 | Week 9 | Session 1 | Problem Set Version 2 | Problem 4
Minimum Depth of Secret Path II

Source: statement reconstructed from the CodePath solution guide and written in our own words.
The original course page is behind a login, so wording and details may differ slightly.
Solution guide (only after you have tried!): https://github.com/codepath/compsci_guides/wiki/Minimum-Depth-of-Secret-Path-II

PROBLEM
-------
Follow-up to Minimum Depth of Secret Path: solve `min_depth` with the other traversal (BFS if you used DFS, or vice versa) and compare which one finishes sooner in general. Note: the CodePath solution page for this problem appears to contain the code for a different problem, so double-check the requirements with your instructor notes.

EXAMPLES (test cases from the solution guide)
---------------------------------------------
HAPPY CASE
Input: 
hotel = Room("Lobby", 
            Room(102, Room(201), Room(202)), 
            Room(101, Room(203), Room(204)))
Output: ['Lobby', 101, 102, 201, 202, 203, 204]
Explanation: The rooms on level 1 are reversed from 102, 101 to 101, 102.

Input: hotel = Room("Lobby", 
            Room(102), 
            Room(101))
Output: ['Lobby', 101, 102]
Explanation: The rooms on level 1 are reversed from 102, 101 to 101, 102.

EDGE CASE
Input: hotel = None
Output: None
Explanation: The tree is empty, so return None.

Input: hotel = Room("Lobby")
Output: ['Lobby']
Explanation: The tree has only one level, so return the root as-is.
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


class Room:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right


def reverse_odd_levels(hotel):
    pass
