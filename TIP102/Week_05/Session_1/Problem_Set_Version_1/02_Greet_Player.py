r"""
TIP102 | Week 5 | Session 1 | Problem Set Version 1 | Problem 2
Greet Player

Source: statement reconstructed from the CodePath solution guide and written in our own words.
The original course page is behind a login, so wording and details may differ slightly.
Solution guide (only after you have tried!): https://github.com/codepath/compsci_guides/wiki/Greet-Player

PROBLEM
-------
Add a method `greet_player(self, player_name)` to `Villager` that returns "{name}: Hey there, {player_name}! How's it going, {catchphrase}?".

EXAMPLES (test cases from the solution guide)
---------------------------------------------
HAPPY CASE
Input: 
bones = Villager("Bones", "Dog", "yip yip")
print(bones.greet_player("Tram"))

Output: 
"Bones: Hey there, Tram! How's it going, yip yip?"

Explanation: 
The `Villager` object `bones` is instantiated correctly and the `greet_player` method returns the expected greeting.

EDGE CASE
Input: 
villager = Villager("", "", "")
print(villager.greet_player(""))

Output: 
": Hey there, ! How's it going, ?"

Explanation: 
Even with empty string attributes, the `Villager` object should handle the method call without errors, though the output will be empty as per the input values.
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
        self.furniture = []

    def greet_player(self, player_name):
        pass
