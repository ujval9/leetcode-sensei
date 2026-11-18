r"""
TIP102 | Week 5 | Session 2 | Problem Set Version 1 | Problem 4
Halve List

Source: statement reconstructed from the CodePath solution guide and written in our own words.
The original course page is behind a login, so wording and details may differ slightly.
Solution guide (only after you have tried!): https://github.com/codepath/compsci_guides/wiki/Halve-List

PROBLEM
-------
Write `halve_list(head)` that divides every value in the linked list by 2 in place and returns the head.

EXAMPLES (test cases from the solution guide)
---------------------------------------------
HAPPY CASE
Input: head = Node(4) -> Node(8) -> Node(12)
Output: Node(2.0) -> Node(4.0) -> Node(6.0)
Explanation: Each value in the linked list is divided by two. Python 3's `/` operator returns a float even when dividing integers exactly, so the resulting values are floats.

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


def halve_list(head):
    pass
