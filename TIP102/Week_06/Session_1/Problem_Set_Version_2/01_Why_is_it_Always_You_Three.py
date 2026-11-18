r"""
TIP102 | Week 6 | Session 1 | Problem Set Version 2 | Problem 1
Why is it Always You Three

Source: statement reconstructed from the CodePath solution guide and written in our own words.
The original course page is behind a login, so wording and details may differ slightly.
Solution guide (only after you have tried!): https://github.com/codepath/compsci_guides/wiki/Why-is-it-Always-You-Three

PROBLEM
-------
Build a linked list Harry -> Ron -> Hermione using a single assignment statement.

EXAMPLES (test cases from the solution guide)
---------------------------------------------
HAPPY CASE
Input: None (assignment statement)
Output: Harry -> Ron -> Hermione
Explanation: The linked list is correctly formed using a single nested constructor statement.

EDGE CASE
Input: None
Output: Harry -> Ron -> Hermione
Explanation: As this problem doesn't involve dynamic inputs, edge cases might involve incorrect or incomplete list formation.
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
