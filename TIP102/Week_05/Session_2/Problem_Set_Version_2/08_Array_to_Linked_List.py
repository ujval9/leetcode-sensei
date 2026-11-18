r"""
TIP102 | Week 5 | Session 2 | Problem Set Version 2 | Problem 8
Array to Linked List

Source: statement reconstructed from the CodePath solution guide and written in our own words.
The original course page is behind a login, so wording and details may differ slightly.
Solution guide (only after you have tried!): https://github.com/codepath/compsci_guides/wiki/Array-to-Linked-List

PROBLEM
-------
Write `arr_to_ll(arr)` that turns a Python list into a linked list with the same values in order and returns the head (None for an empty list).

EXAMPLES (test cases from the solution guide)
---------------------------------------------
HAPPY CASE
Input: arr = [Player("Mario", "Mushmellow"), Player("Luigi", "Standard LG"), Player("Peach", "Bumble V")]
Output: A linked list with nodes for Mario -> Luigi -> Peach
Explanation: The array is converted into a linked list where each Player instance is a node.

EDGE CASE
Input: arr = []
Output: None
Explanation: When the array is empty, the function returns `None`.
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

class Player:
    def __init__(self, character, kart):
        self.character = character
        self.kart = kart
        self.items = []


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


# Helper for testing (provided)
def print_linked_list(head):
    current = head
    while current:
        print(current.value.character, end=" -> " if current.next else "\n")
        current = current.next


def arr_to_ll(arr):
    pass
