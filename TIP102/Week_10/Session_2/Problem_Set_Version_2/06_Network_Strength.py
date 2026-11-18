r"""
TIP102 | Week 10 | Session 2 | Problem Set Version 2 | Problem 6
Network Strength

Source: statement reconstructed from the CodePath solution guide and written in our own words.
The original course page is behind a login, so wording and details may differ slightly.
Solution guide (only after you have tried!): https://github.com/codepath/compsci_guides/wiki/Network-Strength

PROBLEM
-------
In `celebrities`, each celebrity maps to the list of celebrities they like (directed). Write `is_strongly_connected(celebrities)` that returns True if every celebrity can reach every other celebrity by following likes.

EXAMPLES (test cases from the solution guide)
---------------------------------------------
HAPPY CASE
Input: 
celebrities1 = {
    "Dev Patel": ["Meryl Streep", "Viola Davis"],
    "Meryl Streep": ["Dev Patel", "Viola Davis"],
    "Viola Davis": ["Meryl Streep", "Viola Davis"]
}
Output: True
Explanation: Every celebrity can reach every other celebrity directly or indirectly.

EDGE CASE
Input: 
celebrities2 = {
    "John Cho": ["Rami Malek", "Zoe Saldana", "Meryl Streep"],
    "Rami Malek": ["John Cho", "Zoe Saldana", "Meryl Streep"],
    "Zoe Saldana": ["Rami Malek", "John Cho", "Meryl Streep"],
    "Meryl Streep": []
}
Output: False
Explanation: "Meryl Streep" cannot reach anyone (her list is empty), even though every other celebrity can reach her directly, so the network is not strongly connected.
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

def is_strongly_connected(celebrities):
    pass
