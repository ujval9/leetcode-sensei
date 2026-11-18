r"""
TIP102 | Week 5 | Session 2 | Problem Set Version 1 | Problem 8
Move Tail to Front of Linked List

Source: statement reconstructed from the CodePath solution guide and written in our own words.
The original course page is behind a login, so wording and details may differ slightly.
Solution guide (only after you have tried!): https://github.com/codepath/compsci_guides/wiki/Move-Tail-to-Front-of-Linked-List

PROBLEM
-------
Write `tail_to_head(head)` that moves the last node of a linked list to the front and returns the new head.

EXAMPLES (test cases from the solution guide)
---------------------------------------------
HAPPY CASE
Input: head = Node("Daisy") -> Node("Mario") -> Node("Toad") -> Node("Peach")
Output: Node("Peach") -> Node("Daisy") -> Node("Mario") -> Node("Toad")
Explanation: The tail of the linked list "Peach" is moved to the front.

EDGE CASE
Input: head = Node("Daisy")
Output: Node("Daisy")
Explanation: When the linked list has only one node, it remains unchanged.

EDGE CASE
Input: head = None
Output: None
Explanation: When the linked list is empty, the function returns None.
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


# Helper for testing (provided)
def print_linked_list(head):
    current = head
    while current:
        print(current.value, end=" -> " if current.next else "\n")
        current = current.next


def tail_to_head(head):
    pass
