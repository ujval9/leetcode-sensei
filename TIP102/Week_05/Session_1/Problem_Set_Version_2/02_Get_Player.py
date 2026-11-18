r"""
TIP102 | Week 5 | Session 1 | Problem Set Version 2 | Problem 2
Get Player (TIP102)

Source: statement reconstructed from the CodePath solution guide and written in our own words.
The original course page is behind a login, so wording and details may differ slightly.
Solution guide (only after you have tried!): https://github.com/codepath/compsci_guides/wiki/Get-Player-(TIP102)

PROBLEM
-------
Add a method `get_player()` to `Player` that returns a formatted string describing the player (character and kart). Create two players and print their details.

EXAMPLES (test cases from the solution guide)
---------------------------------------------
HAPPY CASE
Input: Create Player with "Yoshi" and "Super Blooper", another with "Bowser" and "Pirahna Prowler"
Output: "Match: Yoshi driving the Super Blooper vs Bowser driving the Pirahna Prowler"
Explanation: The `get_player()` method correctly formats the details of each player, and these details are used in the final print statement.

EDGE CASE
Input: Create Player with empty strings for character and kart
Output: "Match:  driving the  vs  driving the "
Explanation: The `get_player()` method handles cases with empty strings gracefully, producing an empty output for character and kart.
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

class Player():

    def __init__(self, character, kart):
            self.character = character
            self.kart = kart
            self.items = []

    def get_player(self):
        pass
