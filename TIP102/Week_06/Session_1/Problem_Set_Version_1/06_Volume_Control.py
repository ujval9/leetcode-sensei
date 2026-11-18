r"""
TIP102 | Week 6 | Session 1 | Problem Set Version 1 | Problem 6
Volume Control

Source: statement reconstructed from the CodePath solution guide and written in our own words.
The original course page is behind a login, so wording and details may differ slightly.
Solution guide (only after you have tried!): https://github.com/codepath/compsci_guides/wiki/Volume-Control

PROBLEM
-------
Each node holds a volume level. A critical point is a node (not the first or last) whose value is strictly greater than both neighbors or strictly less than both. Write `count_critical_points(song_audio)` that returns how many critical points there are.

EXAMPLES (test cases from the solution guide)
---------------------------------------------
HAPPY CASE
Input: song_audio = Node(5, Node(3, Node(1, Node(2, Node(5, Node(1, Node(2)))))))
Output: 3
Explanation: There are three critical points:
- The third node is a local minima because 1 is less than 3 and 2.
- The fifth node is a local maxima because 5 is greater than 2 and 1.
- The sixth node is a local minima because 1 is less than 5 and 2.

EDGE CASE
Input: song_audio = Node(5)
Output: 0
Explanation: A single node can't be a critical point.

EDGE CASE
Input: song_audio = Node(5, Node(5, Node(5)))
Output: 0
Explanation: All nodes have the same value, so no critical points exist.
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


def count_critical_points(song_audio):
    pass
