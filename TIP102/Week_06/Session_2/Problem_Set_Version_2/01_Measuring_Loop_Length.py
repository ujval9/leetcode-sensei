r"""
TIP102 | Week 6 | Session 2 | Problem Set Version 2 | Problem 1
Measuring Loop Length

Source: statement reconstructed from the CodePath solution guide and written in our own words.
The original course page is behind a login, so wording and details may differ slightly.
Solution guide (only after you have tried!): https://github.com/codepath/compsci_guides/wiki/Measuring-Loop-Length

PROBLEM
-------
The trail is a circular linked list where the last node points back to the first. Write `trail_length(trailhead)` that returns the number of nodes in the loop.

EXAMPLES (test cases from the solution guide)
---------------------------------------------
HAPPY CASE
Input: marker1 = Node("Marker 1")
       marker2 = Node("Marker 2")
       marker3 = Node("Marker 3")
       marker1.next = marker2
       marker2.next = marker3
       marker3.next = marker1
Output: 3
Explanation: The linked list has a loop with three markers.

EDGE CASE
Input: marker1 = Node("Marker 1")
       marker1.next = marker1  # Single node loop
Output: 1
Explanation: The linked list has a loop with one marker.
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


def trail_length(trailhead):
    pass
