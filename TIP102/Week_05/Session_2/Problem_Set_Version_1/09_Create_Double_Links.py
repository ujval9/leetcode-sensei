r"""
TIP102 | Week 5 | Session 2 | Problem Set Version 1 | Problem 9
Create Double Links

Source: statement reconstructed from the CodePath solution guide and written in our own words.
The original course page is behind a login, so wording and details may differ slightly.
Solution guide (only after you have tried!): https://github.com/codepath/compsci_guides/wiki/Create-Double-Links

PROBLEM
-------
Update the `Node` class so each node also has a `prev` pointer, then link the given nodes into a doubly linked list (setting both `next` and `prev`).

EXAMPLES (test cases from the solution guide)
---------------------------------------------
HAPPY CASE
Input: head = Node("Isabelle"), tail = Node("K.K. Slider")
Output: head.next = tail, tail.prev = head
Explanation: The `next` pointer of the head points to the tail, and the `prev` pointer of the tail points to the head.

EDGE CASE
Input: head = Node("Isabelle")
Output: head.next = None, head.prev = None
Explanation: If there is only one node, both `next` and `prev` pointers should be `None`.
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
    def __init__(self, value, next=None, prev=None):
        self.value = value
        self.next = next
        self.prev = prev
