r"""
TIP102 | Week 6 | Session 2 | Problem Set Version 2 | Problem 2
Clearing the Path

Source: statement reconstructed from the CodePath solution guide and written in our own words.
The original course page is behind a login, so wording and details may differ slightly.
Solution guide (only after you have tried!): https://github.com/codepath/compsci_guides/wiki/Clearing-the-Path

PROBLEM
-------
Write `clear_trail(trailhead)` that breaks any cycle in the linked list (so the last node points to None) and returns the head.

EXAMPLES (test cases from the solution guide)
---------------------------------------------
HAPPY CASE
Input: marker1 = Node("Trailhead")
       marker2 = Node("Trail Fork")
       marker3 = Node("The Falls")
       marker4 = Node("Peak")
       marker1.next = marker2
       marker2.next = marker3
       marker3.next = marker4
       marker4.next = marker2  # Cycle here
Output: Trailhead -> Trail Fork -> The Falls -> Peak
Explanation: The cycle is removed, resulting in a straightforward linked list.

EDGE CASE
Input: marker1 = Node("Trailhead")
       marker1.next = marker1  # Self-loop
Output: Trailhead
Explanation: The self-loop is removed, leaving a single node.
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


def clear_trail(trailhead):
    pass
