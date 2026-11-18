r"""
TIP102 | Week 6 | Session 1 | Problem Set Version 2 | Problem 2
200 Points for Gryffindor

Source: statement reconstructed from the CodePath solution guide and written in our own words.
The original course page is behind a login, so wording and details may differ slightly.
Solution guide (only after you have tried!): https://github.com/codepath/compsci_guides/wiki/200-Points-for-Gryffindor

PROBLEM
-------
Each node holds a house name and a score. Write `count_element(house_points, score)` that returns how many nodes have that score.

EXAMPLES (test cases from the solution guide)
---------------------------------------------
HAPPY CASE
Input: house_points = Node("Gryffindor", 600, Node("Ravenclaw", 300, Node("Slytherin", 500, Node("Hufflepuff", 600)))), score = 600
Output: 2
Explanation: The score 600 appears twice in the linked list.

EDGE CASE
Input: house_points = None, score = 500
Output: 0
Explanation: An empty list does not contain any elements, so the output is 0.

EDGE CASE
Input: house_points = Node("Gryffindor", 600), score = 400
Output: 0
Explanation: The score 400 does not appear in the list.
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
    def __init__(self, house, score, next=None):
        self.house = house
        self.value = score
        self.next = next


def count_element(house_points, score):
    pass
