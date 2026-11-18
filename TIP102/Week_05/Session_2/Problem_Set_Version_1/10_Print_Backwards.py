r"""
TIP102 | Week 5 | Session 2 | Problem Set Version 1 | Problem 10
Print Backwards

Source: statement reconstructed from the CodePath solution guide and written in our own words.
The original course page is behind a login, so wording and details may differ slightly.
Solution guide (only after you have tried!): https://github.com/codepath/compsci_guides/wiki/Print-Backwards

PROBLEM
-------
Write `print_reverse(tail)` that, given the tail of a doubly linked list, prints the values from tail back to head separated by spaces.

EXAMPLES (test cases from the solution guide)
---------------------------------------------
HAPPY CASE
Input: tail = Node("Saharah", prev=Node("K.K. Slider", prev=Node("Isabelle")))
Output: "Saharah K.K. Slider Isabelle"
Explanation: The function prints the values of the linked list from the tail to the head.

EDGE CASE
Input: tail = None
Output: (No output)
Explanation: When the linked list is empty, the function does not print anything.
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


def print_reverse(tail):
    pass
