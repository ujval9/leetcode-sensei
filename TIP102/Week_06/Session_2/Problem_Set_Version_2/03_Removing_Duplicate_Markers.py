r"""
TIP102 | Week 6 | Session 2 | Problem Set Version 2 | Problem 3
Removing Duplicate Markers

Source: statement reconstructed from the CodePath solution guide and written in our own words.
The original course page is behind a login, so wording and details may differ slightly.
Solution guide (only after you have tried!): https://github.com/codepath/compsci_guides/wiki/Removing-Duplicate-Markers

PROBLEM
-------
Given a sorted linked list, write `remove_duplicate_markers(trailhead)` that removes every node whose value appears more than once, keeping only values that appear exactly once. Return the head.

EXAMPLES (test cases from the solution guide)
---------------------------------------------
HAPPY CASE
Input: trailhead = Node(1, Node(2, Node(3, Node(3, Node(4)))))
Output: 1 -> 2 -> 4
Explanation: The node with value 3 appears twice, so it is removed.

EDGE CASE
Input: trailhead = Node(1, Node(1, Node(1)))
Output: (empty list)
Explanation: All nodes have the same value and are duplicates, so the list becomes empty.
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


def remove_duplicate_markers(trailhead):
    pass
