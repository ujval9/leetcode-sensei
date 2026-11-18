r"""
TIP102 | Week 5 | Session 2 | Problem Set Version 2 | Problem 9
Convert Singly Linked List to Doubly Linked List

Source: statement reconstructed from the CodePath solution guide and written in our own words.
The original course page is behind a login, so wording and details may differ slightly.
Solution guide (only after you have tried!): https://github.com/codepath/compsci_guides/wiki/Convert-Singly-Linked-List-to-Doubly-Linked-List

PROBLEM
-------
Given a singly linked list whose nodes also have an unused `prev` attribute, set every node's `prev` pointer so the list becomes a doubly linked list.

EXAMPLES (test cases from the solution guide)
---------------------------------------------
HAPPY CASE
Input: koopa_troopa = Node("Koopa Troopa") -> Node("Toadette") -> Node("Waluigi")
Output: koopa_troopa = Node("Koopa Troopa") <-> Node("Toadette") <-> Node("Waluigi")
Explanation: The singly linked list is converted into a doubly linked list by updating the `prev` pointers.

EDGE CASE
Input: koopa_troopa = None
Output: None
Explanation: When the linked list is empty, no changes are made.
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
