r"""
TIP102 | Week 5 | Session 2 | Problem Set Version 1 | Problem 7
Remove From Inventory

Source: statement reconstructed from the CodePath solution guide and written in our own words.
The original course page is behind a login, so wording and details may differ slightly.
Solution guide (only after you have tried!): https://github.com/codepath/compsci_guides/wiki/Remove-From-Inventory

PROBLEM
-------
Write `delete_item(head, item)` that removes the first node whose value is `item` and returns the (possibly new) head. If the item is not found, return the list unchanged.

EXAMPLES (test cases from the solution guide)
---------------------------------------------
HAPPY CASE
Input: head = Node("Slingshot") -> Node("Peaches") -> Node("Scarab Beetle"), item = "Peaches"
Output: Node("Slingshot") -> Node("Scarab Beetle")
Explanation: The node with value "Peaches" is removed from the linked list.

EDGE CASE
Input: head = Node("Slingshot") -> Node("Peaches") -> Node("Scarab Beetle"), item = "Triceratops Torso"
Output: Node("Slingshot") -> Node("Peaches") -> Node("Scarab Beetle")
Explanation: The item is not found, so the list remains unchanged.

EDGE CASE
Input: head = None, item = "Peaches"
Output: None
Explanation: The linked list is empty, so the function returns None.
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


def delete_item(head, item):
    pass
