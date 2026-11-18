r"""
TIP102 | Week 6 | Session 1 | Problem Set Version 2 | Problem 4
Turn Back Time

Source: statement reconstructed from the CodePath solution guide and written in our own words.
The original course page is behind a login, so wording and details may differ slightly.
Solution guide (only after you have tried!): https://github.com/codepath/compsci_guides/wiki/Turn-Back-Time

PROBLEM
-------
Write `reverse(events)` that reverses a singly linked list and returns the new head.

EXAMPLES (test cases from the solution guide)
---------------------------------------------
HAPPY CASE
Input: events = Node("Potion Brewing", Node("Spell Casting", Node("Wand Making", Node("Dragon Taming", Node("Broomstick Flying")))))
Output: "Broomstick Flying" -> "Dragon Taming" -> "Wand Making" -> "Spell Casting" -> "Potion Brewing"
Explanation: The linked list is reversed correctly.

EDGE CASE
Input: events = Node("Potion Brewing")
Output: "Potion Brewing"
Explanation: A single-node list remains the same after reversal.

EDGE CASE
Input: events = None
Output: None
Explanation: An empty list should return None.
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

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


def reverse(events):
    pass
