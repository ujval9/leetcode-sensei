r"""
TIP102 | Week 5 | Session 1 | Problem Set Version 1 | Problem 7
Group by Personality

Source: statement reconstructed from the CodePath solution guide and written in our own words.
The original course page is behind a login, so wording and details may differ slightly.
Solution guide (only after you have tried!): https://github.com/codepath/compsci_guides/wiki/Group-by-Personality

PROBLEM
-------
Each `Villager` has a `personality` attribute. Write `of_personality_type(townies, personality_type)` that returns a list of the names of villagers in `townies` whose personality matches `personality_type`.

EXAMPLES (test cases from the solution guide)
---------------------------------------------
HAPPY CASE
Input: 
isabelle = Villager("Isabelle", "Dog", "Normal", "what's up?")
bob = Villager("Bob", "Cat", "Lazy", "pthhhpth")
stitches = Villager("Stitches", "Cub", "Lazy", "stuffin'")
townies = [isabelle, bob, stitches]
personality_type = "Lazy"
result = of_personality_type(townies, personality_type)

Output: 
["Bob", "Stitches"]

Explanation: 
The function iterates through the `townies` list and collects names of villagers with the "Lazy" personality.

EDGE CASE
Input: 
townies = [isabelle, bob, stitches]
personality_type = "Cranky"
result = of_personality_type(townies, personality_type)

Output: 
[]

Explanation: 
No villagers have the "Cranky" personality, so the function returns an empty list.
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
    def __init__(self, name, species, personality, catchphrase):
        self.name = name
        self.species = species
        self.personality = personality
        self.catchphrase = catchphrase
        self.furniture = []


def of_personality_type(townies, personality_type):
    pass
