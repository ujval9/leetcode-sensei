r"""
TIP102 | Week 8 | Session 2 | Problem Set Version 2 | Problem 1
Find Lonely Cichlids

Source: statement reconstructed from the CodePath solution guide and written in our own words.
The original course page is behind a login, so wording and details may differ slightly.
Solution guide (only after you have tried!): https://github.com/codepath/compsci_guides/wiki/Find-Lonely-Cichlids

PROBLEM
-------
A 'lonely' node is the only child of its parent. Write `find_lonely_cichlids(root)` that returns a list of the values of all lonely nodes.

EXAMPLES (test cases from the solution guide)
---------------------------------------------
HAPPY CASE
Input: family_1 = Cichlid('A', Cichlid('B', None, Cichlid('D')), Cichlid('C'))
Output: ['D']
Explanation: 'D' is the only lonely cichlid.

EDGE CASE
Input: family_3 = Cichlid('A', Cichlid('B', Cichlid('D', Cichlid('F', Cichlid('H')))), Cichlid('C', None, Cichlid('E', None, Cichlid('G', None, Cichlid('I')))))
Output: ['D', 'F', 'H', 'E', 'G', 'I']
Explanation: Multiple nodes are lonely in this more complex tree.
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

class Cichlid:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right


def find_lonely_cichlids(root):
    pass
