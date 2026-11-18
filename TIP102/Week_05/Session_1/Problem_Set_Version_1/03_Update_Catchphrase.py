r"""
TIP102 | Week 5 | Session 1 | Problem Set Version 1 | Problem 3
Update Catchphrase

Source: statement reconstructed from the CodePath solution guide and written in our own words.
The original course page is behind a login, so wording and details may differ slightly.
Solution guide (only after you have tried!): https://github.com/codepath/compsci_guides/wiki/Update-Catchphrase

PROBLEM
-------
Create a villager `bones` ("Bones", "Dog", "yip yip"), then change its catchphrase to "ruff it up" by updating the attribute directly, and call `greet_player` to confirm the change.

EXAMPLES (test cases from the solution guide)
---------------------------------------------
HAPPY CASE
Input: 
bones = Villager("Bones", "Dog", "yip yip")
bones.catchphrase = "ruff it up"
print(bones.greet_player("Samia"))

Output: 
"Bones: Hey there, Samia! How's it going, ruff it up?"

Explanation: 
The `catchphrase` attribute of `bones` is successfully updated to `"ruff it up"`, and the `greet_player` method returns the expected greeting.

EDGE CASE
Input: 
villager = Villager("", "", "")
villager.catchphrase = "hello"
print(villager.greet_player(""))

Output: 
": Hey there, ! How's it going, hello?"

Explanation: 
Even with empty string attributes initially, the `catchphrase` attribute can be updated, and the method should handle the output accordingly.
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
