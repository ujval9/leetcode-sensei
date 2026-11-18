r"""
TIP102 | Week 6 | Session 2 | Problem Set Version 1 | Problem 6
Adding Up the Evidence

Source: statement reconstructed from the CodePath solution guide and written in our own words.
The original course page is behind a login, so wording and details may differ slightly.
Solution guide (only after you have tried!): https://github.com/codepath/compsci_guides/wiki/Adding-Up-the-Evidence

PROBLEM
-------
Two non-negative numbers are stored as linked lists with digits in reverse order (ones digit first). Write `add_two_numbers(head_a, head_b)` that returns their sum as a linked list in the same reverse format.

EXAMPLES (test cases from the solution guide)
---------------------------------------------
HAPPY CASE
Input: head_a = Node(2, Node(4, Node(3)))  # 342
       head_b = Node(5, Node(6, Node(4)))  # 465
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807. The result is represented as 7 -> 0 -> 8.

EDGE CASE
Input: head_a = Node(9, Node(9, Node(9)))  # 999
       head_b = Node(1)                    # 1
Output: 0 -> 0 -> 0 -> 1
Explanation: 999 + 1 = 1000. The result is represented as 0 -> 0 -> 0 -> 1.
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


def add_two_numbers(head_a, head_b):
    pass
