r"""
TIP102 | Week 6 | Session 2 | Problem Set Version 1 | Problem 5
A New Perspective

Source: statement reconstructed from the CodePath solution guide and written in our own words.
The original course page is behind a login, so wording and details may differ slightly.
Solution guide (only after you have tried!): https://github.com/codepath/compsci_guides/wiki/A-New-Perspective

PROBLEM
-------
Write `rotate_right(head, k)` that rotates a linked list to the right by `k` places (the last k nodes move to the front) and returns the new head.

EXAMPLES (test cases from the solution guide)
---------------------------------------------
HAPPY CASE
Input: evidence_list1 = Node(1, Node(2, Node(3, Node(4, Node(5)))))
       k = 2
Output: 4 -> 5 -> 1 -> 2 -> 3
Explanation: The list is rotated to the right by 2 places.

HAPPY CASE
Input: evidence_list2 = Node(0, Node(1, Node(2)))
       k = 4
Output: 2 -> 0 -> 1
Explanation: The list is rotated to the right by 4 places. Since 4 % 3 = 1, it's equivalent to rotating by 1 place.

EDGE CASE
Input: evidence_list = Node(1)
       k = 10
Output: 1
Explanation: A single-node list remains unchanged regardless of the value of `k`.
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


def rotate_right(head, k):
    pass
