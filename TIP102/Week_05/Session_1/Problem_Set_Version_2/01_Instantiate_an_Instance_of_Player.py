r"""
TIP102 | Week 5 | Session 1 | Problem Set Version 2 | Problem 1
Instantiate an Instance of Player

Source: statement reconstructed from the CodePath solution guide and written in our own words.
The original course page is behind a login, so wording and details may differ slightly.
Solution guide (only after you have tried!): https://github.com/codepath/compsci_guides/wiki/Instantiate-an-Instance-of-Player

PROBLEM
-------
Create an instance of the `Player` class with the given character and kart, and check that its attributes are set correctly.

EXAMPLES (test cases from the solution guide)
---------------------------------------------
HAPPY CASE
Input: Instantiate Player with "Yoshi" as character and "Super Blooper" as kart
Output: Player's character is "Yoshi", kart is "Super Blooper", and items list is empty.
Explanation: We correctly initialize the Player object with the provided values and an empty items list.

EDGE CASE
Input: Instantiate Player with an empty string for character and kart
Output: Player's character is ", kart is ", and items list is empty.
Explanation: We check if the object initializes correctly with empty strings.
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
