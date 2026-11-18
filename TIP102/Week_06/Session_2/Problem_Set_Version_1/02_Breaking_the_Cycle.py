r"""
TIP102 | Week 6 | Session 2 | Problem Set Version 1 | Problem 2
Breaking the Cycle

Source: statement reconstructed from the CodePath solution guide and written in our own words.
The original course page is behind a login, so wording and details may differ slightly.
Solution guide (only after you have tried!): https://github.com/codepath/compsci_guides/wiki/Breaking-the-Cycle

PROBLEM
-------
Write `collect_false_evidence(evidence)` that returns a list of the values of every node that is part of a cycle in the linked list (empty list if there is no cycle).

EXAMPLES (test cases from the solution guide)
---------------------------------------------
HAPPY CASE
Input: clue1 = Node("Unmarked sedan seen near the crime scene")
       clue2 = Node("The stolen goods are at an abandoned warehouse")
       clue3 = Node("The mayor is accepting bribes")
       clue4 = Node("They dumped their disguise in the lake")
       clue1.next = clue2
       clue2.next = clue3
       clue3.next = clue4
       clue4.next = clue2  # Creates a cycle
Output: ["The stolen goods are at an abandoned warehouse", "The mayor is accepting bribes", "They dumped their disguise in the lake"]
Explanation: These are the values of the nodes that form a cycle in the linked list.

HAPPY CASE
Input: clue5 = Node("A masked figure was seen fleeing the scene")
       clue6 = Node("Footprints lead to the nearby woods")
       clue7 = Node("A broken window was found at the back")
       clue5.next = clue6
       clue6.next = clue7
       clue7.next = None  # No cycle
Output: []
Explanation: No cycle detected, so the function returns an empty list.

EDGE CASE
Input: clue1 = Node("Unmarked sedan seen near the crime scene")
       clue1.next = clue1  # Self-loop
Output: ["Unmarked sedan seen near the crime scene"]
Explanation: The node points to itself, forming a cycle.
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


def collect_false_evidence(evidence):
    pass
