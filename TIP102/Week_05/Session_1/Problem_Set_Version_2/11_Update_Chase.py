r"""
TIP102 | Week 5 | Session 1 | Problem Set Version 2 | Problem 11
Update Chase

Source: statement reconstructed from the CodePath solution guide and written in our own words.
The original course page is behind a login, so wording and details may differ slightly.
Solution guide (only after you have tried!): https://github.com/codepath/compsci_guides/wiki/Update-Chase

PROBLEM
-------
Remove the first node ("Spike", the dog) from the chase list so that Tom becomes the head again.

EXAMPLES (test cases from the solution guide)
---------------------------------------------
HAPPY CASE
Input: dog -> cat -> mouse
Output: cat -> mouse -> cheese
Explanation: The `dog` node at the head is disconnected, and a new node `cheese` with value "Gouda" is added to the end of the list.

EDGE CASE
Input: cat -> mouse
Output: cat -> mouse -> cheese
Explanation: The list already does not contain a `dog` node, so just the `cheese` node is added.
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
