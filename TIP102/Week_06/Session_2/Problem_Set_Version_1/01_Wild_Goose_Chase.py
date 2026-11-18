r"""
TIP102 | Week 6 | Session 2 | Problem Set Version 1 | Problem 1
Wild Goose Chase

Source: statement reconstructed from the CodePath solution guide and written in our own words.
The original course page is behind a login, so wording and details may differ slightly.
Solution guide (only after you have tried!): https://github.com/codepath/compsci_guides/wiki/Wild-Goose-Chase

PROBLEM
-------
Write `is_circular(clues)` that returns True if the tail of the linked list points back to the head, otherwise False.

EXAMPLES (test cases from the solution guide)
---------------------------------------------
HAPPY CASE
Input: clue1 = Node("The stolen goods are at an abandoned warehouse")
       clue2 = Node("The mayor is accepting bribes")
       clue3 = Node("They dumped their disguise in the lake")
       clue1.next = clue2
       clue2.next = clue3
       clue3.next = clue1  # Circular link
Output: True
Explanation: The linked list is circular because the last node points back to the head.

EDGE CASE
Input: clue1 = Node("The stolen goods are at an abandoned warehouse")
       clue2 = Node("The mayor is accepting bribes")
       clue3 = Node("They dumped their disguise in the lake")
       clue1.next = clue2
       clue2.next = clue3
       clue3.next = None  # Not circular
Output: False
Explanation: The linked list is not circular because the last node does not point back to the head.

EDGE CASE
Input: clue1 = Node("The stolen goods are at an abandoned warehouse")
       clue2 = Node("The mayor is accepting bribes")
       clue3 = Node("They dumped their disguise in the lake")
       clue1.next = clue2
       clue2.next = clue3
       clue3.next = clue2  # Tail links back to the middle, not the head
Output: False
Explanation: The list has a cycle (clue2 -> clue3 -> clue2), but the head clue1 is not on it, so the tail does not point back to the head.
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


def is_circular(clues):
    pass
