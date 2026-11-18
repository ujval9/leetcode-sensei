r"""
TIP102 | Week 5 | Session 2 | Problem Set Version 2 | Problem 1
Calculate Tournament Placement

Source: statement reconstructed from the CodePath solution guide and written in our own words.
The original course page is behind a login, so wording and details may differ slightly.
Solution guide (only after you have tried!): https://github.com/codepath/compsci_guides/wiki/Calculate-Tournament-Placement

PROBLEM
-------
Each `Player` has a list of opponents and finishing times. Add a method that returns this player's placement (1 for first place) based on how many opponents finished faster. A player with no opponents is 1st.

EXAMPLES (test cases from the solution guide)
---------------------------------------------
HAPPY CASE
Input: player1 = Player("Mario", "Standard", [1, 2, 1, 1, 3]), opponents = [Player("Luigi", "Standard", [2, 1, 3, 2, 2]), Player("Peach", "Standard", [3, 3, 2, 3, 1])]
Output: 1
Explanation: Mario's average race outcome is 1.6, which is lower than Luigi's 2.0 and Peach's 2.4, so Mario gets 1st place.

EDGE CASE
Input: player1 = Player("Mario", "Standard", [2, 2, 2, 2, 2]), opponents = [Player("Luigi", "Standard", [2, 2, 2, 2, 2])]
Output: 1
Explanation: Both players have the same average race outcome, so Mario gets 1st place because the function counts the player itself as 1st.

EDGE CASE
Input: player1 = Player("Mario", "Standard", [1, 1, 1, 1, 1]), opponents = []
Output: 1
Explanation: Without any opponents, Mario automatically gets 1st place.
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

class Player:

    def __init__(self, character, kart, outcomes):
        self.character = character
        self.kart = kart
        self.items = []
        self.race_outcomes = outcomes

    def get_tournament_place(self, opponents):
        pass
