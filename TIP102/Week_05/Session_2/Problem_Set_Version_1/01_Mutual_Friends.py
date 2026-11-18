r"""
TIP102 | Week 5 | Session 2 | Problem Set Version 1 | Problem 1
Mutual Friends

Source: statement reconstructed from the CodePath solution guide and written in our own words.
The original course page is behind a login, so wording and details may differ slightly.
Solution guide (only after you have tried!): https://github.com/codepath/compsci_guides/wiki/Mutual-Friends

PROBLEM
-------
Each `Villager` has a `friends` list. Add a method `get_mutual_friends(self, new_contact)` that returns a list of names of villagers who are friends with both this villager and `new_contact`. Return an empty list if there are none.

EXAMPLES (test cases from the solution guide)
---------------------------------------------
HAPPY CASE
Input: bob.friends = [stitches, raymond, fauna], marshal.friends = [raymond, ankha, fauna]
Output: ["Raymond", "Fauna"]
Explanation: Bob and Marshal have two mutual friends: Raymond and Fauna.

EDGE CASE
Input: bob.friends = [stitches, raymond, fauna], ankha.friends = [marshal]
Output: []
Explanation: Bob and Ankha have no mutual friends.
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

class Villager:

    def __init__(self, name, species, catchphrase):
        self.name = name
        self.species = species
        self.catchphrase = catchphrase
        self.friends = []

    def get_mutuals(self, new_contact):
        pass
