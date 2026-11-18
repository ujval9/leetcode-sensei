r"""
TIP102 | Week 5 | Session 2 | Problem Set Version 2 | Problem 6
Making the Cut

Source: statement reconstructed from the CodePath solution guide and written in our own words.
The original course page is behind a login, so wording and details may differ slightly.
Solution guide (only after you have tried!): https://github.com/codepath/compsci_guides/wiki/Making-the-Cut

PROBLEM
-------
The linked list holds racers in finishing order. Write `top_n_finishers(head, n)` that returns a list of the first `n` racers' values (or all of them if there are fewer than `n`).

EXAMPLES (test cases from the solution guide)
---------------------------------------------
HAPPY CASE
Input: head = Node("Daisy") -> Node("Mario") -> Node("Toad") -> Node("Yoshi"), n = 3
Output: ["Daisy", "Mario", "Toad"]
Explanation: The function returns the values of the first 3 nodes.

EDGE CASE
Input: head = Node("Daisy") -> Node("Mario"), n = 5
Output: ["Daisy", "Mario"]
Explanation: Since `n` is greater than the length of the linked list, the function returns the values of all nodes.
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


def top_n_finishers(head, n):
    pass
