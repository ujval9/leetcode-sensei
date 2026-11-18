r"""
TIP102 | Week 9 | Session 1 | Problem Set Version 2 | Problem 2
Mapping a Haunted Hotel

Source: statement reconstructed from the CodePath solution guide and written in our own words.
The original course page is behind a login, so wording and details may differ slightly.
Solution guide (only after you have tried!): https://github.com/codepath/compsci_guides/wiki/Mapping-a-Haunted-Hotel

PROBLEM
-------
Write `map_hotel(hotel)` that returns a list of room values in level order (top floor to bottom, left to right).

EXAMPLES (test cases from the solution guide)
---------------------------------------------
HAPPY CASE
Input: 
hotel = Room("Lobby", 
                Room(101, Room(201, Room(301)), Room(202)),
                Room(102, Room(203), Room(204, None, Room(302))))
Output: ['Lobby', 101, 102, 201, 202, 203, 204, 301, 302]
Explanation: The rooms are explored level by level from left to right.

Input: hotel = Room("Lobby")
Output: ['Lobby']
Explanation: The tree has only one node, so return its value.

EDGE CASE
Input: hotel = None
Output: []
Explanation: The tree is empty, so return an empty list.

Input: hotel = Room("Lobby", Room(101))
Output: ['Lobby', 101]
Explanation: The tree has only two nodes, with one child on the left.
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


def map_hotel(hotel):
    pass
