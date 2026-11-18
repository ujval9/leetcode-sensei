r"""
TIP102 | Week 5 | Session 2 | Problem Set Version 1 | Problem 6
Find Minimum in Linked List

Source: statement reconstructed from the CodePath solution guide and written in our own words.
The original course page is behind a login, so wording and details may differ slightly.
Solution guide (only after you have tried!): https://github.com/codepath/compsci_guides/wiki/Find-Minimum-in-Linked-List

PROBLEM
-------
Write `find_min(head)` that returns the smallest value in a linked list of numbers, or None if the list is empty.

EXAMPLES (test cases from the solution guide)
---------------------------------------------
HAPPY CASE
Input: head = Node(5) -> Node(6) -> Node(7) -> Node(8)
Output: 5
Explanation: The smallest value in the linked list is 5.

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


def find_min(head):
    pass
