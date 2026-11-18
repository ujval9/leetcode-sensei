r"""
TIP102 | Week 6 | Session 2 | Problem Set Version 1 | Problem 4
Puzzling it Out

Source: statement reconstructed from the CodePath solution guide and written in our own words.
The original course page is behind a login, so wording and details may differ slightly.
Solution guide (only after you have tried!): https://github.com/codepath/compsci_guides/wiki/Puzzling-it-Out

PROBLEM
-------
Write `merge_timelines(known_timeline, witness_timeline)` that merges two sorted linked lists into one sorted linked list and returns its head.

EXAMPLES (test cases from the solution guide)
---------------------------------------------
HAPPY CASE
Input: known_timeline = Node(1, Node(2, Node(4)))
       witness_timeline = Node(1, Node(3, Node(4)))
Output: 1 -> 1 -> 2 -> 3 -> 4 -> 4
Explanation: The two linked lists are merged into a single sorted linked list.

EDGE CASE
Input: known_timeline = Node(1, Node(2, Node(4)))
       witness_timeline = None
Output: 1 -> 2 -> 4
Explanation: The witness timeline is empty, so the merged list is just the known timeline.

EDGE CASE
Input: known_timeline = None
       witness_timeline = Node(2, Node(3, Node(4)))
Output: 2 -> 3 -> 4
Explanation: The known timeline is empty, so the merged list is just the witness timeline.
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


def merge_timelines(known_timeline, witness_timeline):
    pass
