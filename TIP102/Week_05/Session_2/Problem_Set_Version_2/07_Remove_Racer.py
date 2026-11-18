r"""
TIP102 | Week 5 | Session 2 | Problem Set Version 2 | Problem 7
Remove Racer

Source: statement reconstructed from the CodePath solution guide and written in our own words.
The original course page is behind a login, so wording and details may differ slightly.
Solution guide (only after you have tried!): https://github.com/codepath/compsci_guides/wiki/Remove-Racer

PROBLEM
-------
Write `remove_racer(head, racer)` that removes the first node whose value is `racer` and returns the head. If the racer is not found, return the list unchanged.

EXAMPLES (test cases from the solution guide)
---------------------------------------------
HAPPY CASE
Input: head = Node("Daisy") -> Node("Mario") -> Node("Toad") -> Node("Mario"), racer = "Mario"
Output: head = Node("Daisy") -> Node("Toad") -> Node("Mario")
Explanation: The first node with value "Mario" is removed from the list.

EDGE CASE
Input: head = Node("Daisy") -> Node("Mario") -> Node("Toad"), racer = "Yoshi"
Output: head = Node("Daisy") -> Node("Mario") -> Node("Toad")
Explanation: Since "Yoshi" is not found in the list, the original list is returned unchanged.

EDGE CASE
Input: head = None, racer = "Mario"
Output: None
Explanation: When the linked list is empty, the function returns `None`.
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


def remove_racer(head, racer):
    pass
