r"""
TIP102 | Week 6 | Session 2 | Problem Set Version 2 | Problem 5
Geocaching

Source: statement reconstructed from the CodePath solution guide and written in our own words.
The original course page is behind a login, so wording and details may differ slightly.
Solution guide (only after you have tried!): https://github.com/codepath/compsci_guides/wiki/Geocaching

PROBLEM
-------
Each node holds a 0 or 1, and together they form a binary number (head is the most significant bit). Write `locate_cache(cache_labels)` that returns its decimal value.

EXAMPLES (test cases from the solution guide)
---------------------------------------------
HAPPY CASE
Input: cache_labels = Node(1, Node(0, Node(1)))  # Binary: 101
Output: 5
Explanation: The binary number 101 corresponds to the decimal value 5.

EDGE CASE
Input: cache_labels = Node(0)  # Binary: 0
Output: 0
Explanation: The binary number 0 corresponds to the decimal value 0.

EDGE CASE
Input: cache_labels = Node(1)  # Binary: 1
Output: 1
Explanation: The binary number 1 corresponds to the decimal value 1.
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


def locate_cache(cache_labels):
    pass
