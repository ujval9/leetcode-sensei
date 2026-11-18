r"""
TIP102 | Week 12 | Session 2 | Problem Set Version 2 | Problem 6
Split Linked List in Parts

Source: statement reconstructed from the CodePath solution guide and written in our own words.
The original course page is behind a login, so wording and details may differ slightly.
Solution guide (only after you have tried!): https://github.com/codepath/compsci_guides/wiki/Split-Linked-List-in-Parts

PROBLEM
-------
Write `split_list(head, k)` that splits a linked list into `k` consecutive parts whose sizes differ by at most one, with earlier parts larger. Return a list of the `k` part heads, using None for empty parts.

EXAMPLES (test cases from the solution guide)
---------------------------------------------
HAPPY CASE
Input: list_1 = [1, 2, 3], k = 5
Output: [[1], [2], [3], None, None]
Explanation: The input is divided into 5 parts, with the extra parts being empty.

Input: list_2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], k = 3
Output: [[1, 2, 3, 4], [5, 6, 7], [8, 9, 10]]
Explanation: The list is split into 3 parts with size difference at most 1.
EDGE CASE
Input: list = [], k = 3
Output: [None, None, None]
Explanation: The input list is empty, so all parts are None.

Input: list = [1, 2, 3], k = 1
Output: [[1, 2, 3]]
Explanation: The whole list is returned as one part.
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
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next


def split_list(head, k):
    pass
