r"""
TIP102 | Week 6 | Session 1 | Problem Set Version 2 | Problem 5
Mirror, Mirror

Source: statement reconstructed from the CodePath solution guide and written in our own words.
The original course page is behind a login, so wording and details may differ slightly.
Solution guide (only after you have tried!): https://github.com/codepath/compsci_guides/wiki/Mirror,-Mirror

PROBLEM
-------
Write `is_mirrored(head)` that returns True if the linked list's values read the same forwards and backwards, otherwise False.

EXAMPLES (test cases from the solution guide)
---------------------------------------------
HAPPY CASE
Input: list1 = Node("Phoenix", Node("Dragon", Node("Phoenix")))
Output: True
Explanation: The linked list reads the same forwards and backwards.

HAPPY CASE
Input: list2 = Node("Werewolf", Node("Vampire", Node("Griffin")))
Output: False
Explanation: The linked list does not read the same forwards and backwards.

EDGE CASE
Input: head = None
Output: True
Explanation: An empty list is considered a palindrome.

EDGE CASE
Input: head = Node("Phoenix")
Output: True
Explanation: A single-node list is considered a palindrome.
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


def is_mirrored(head):
    pass
