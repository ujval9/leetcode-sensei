r"""
TIP102 | Week 10 | Session 1 | Problem Set Version 2 | Problem 3
Closest Friends

Source: statement reconstructed from the CodePath solution guide and written in our own words.
The original course page is behind a login, so wording and details may differ slightly.
Solution guide (only after you have tried!): https://github.com/codepath/compsci_guides/wiki/Closest-Friends

PROBLEM
-------
Each item in `contacts` is a pair [a, b] meaning a and b are friends (undirected). Write `get_close_friends(contacts, celeb)` that returns a list of everyone directly connected to `celeb`.

EXAMPLES (test cases from the solution guide)
---------------------------------------------
HAPPY CASE
Input: contacts = [
                    ["Lupita Nyong'o", "Jordan Peele"],
                    ["Meryl Streep", "Jordan Peele"],
                    ["Meryl Streep", "Lupita Nyong'o"],
                    ["Greta Gerwig", "Meryl Streep"],
                    ["Ali Wong", "Greta Gerwig"]
                  ]
celebrity = "Lupita Nyong'o"
Output: ['Jordan Peele', 'Meryl Streep']
Explanation: Lupita Nyong'o is directly connected to Jordan Peele and Meryl Streep, so they are her closest friends.

EDGE CASE
Input: contacts = []
celebrity = "Lupita Nyong'o"
Output: []
Explanation: There are no connections, so the result is an empty list.
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

def get_close_friends(contacts, celeb):
    pass
