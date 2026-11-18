r"""
TIP102 | Week 9 | Session 2 | Problem Set Version 2 | Problem 5
Purging Unwanted Guests

Source: statement reconstructed from the CodePath solution guide and written in our own words.
The original course page is behind a login, so wording and details may differ slightly.
Solution guide (only after you have tried!): https://github.com/codepath/compsci_guides/wiki/Purging-Unwanted-Guests

PROBLEM
-------
Write `purge_hotel(hotel)` that repeatedly removes all current leaves, recording each round's leaf values, until the tree is empty. Return the list of values in the order they were removed.

EXAMPLES (test cases from the solution guide)
---------------------------------------------
HAPPY CASE
Input: 
hotel = Room("👻", Room("😱", Room("💀"), Room("😈")), Room("🧛🏾‍♀️"))
Output: [['💀', '😈', '🧛🏾‍♀️'], ['😱'], ['👻']]
Explanation: 
* The tree is purged level by level, with the leaf nodes being collected and removed first.

Input: 
hotel = Room("👻", Room("😱"), Room("🧛🏾‍♀️"))
Output: [['😱', '🧛🏾‍♀️'], ['👻']]
Explanation: 
* The tree is purged, and the leaf nodes "😱" and "🧛🏾‍♀️" are collected first, followed by the root "👻".

EDGE CASE
Input: hotel = None
Output: []
Explanation: The tree is empty, so return an empty list.

Input: hotel = Room("👻")
Output: [['👻']]
Explanation: The tree has only one node, so collect the single leaf node "👻" and return it.
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

class Room:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right


def purge_hotel(hotel):
    pass
