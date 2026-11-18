r"""
TIP102 | Week 10 | Session 2 | Problem Set Version 2 | Problem 2
Cast vs Crew

Source: statement reconstructed from the CodePath solution guide and written in our own words.
The original course page is behind a login, so wording and details may differ slightly.
Solution guide (only after you have tried!): https://github.com/codepath/compsci_guides/wiki/Cast-vs-Crew

PROBLEM
-------
`cast_and_crew` is an adjacency dictionary where an edge connects two cast members or two crew members, never a cast member and a crew member. Write `get_groups(cast_and_crew)` that splits everyone into two groups (cast and crew) and returns them.

EXAMPLES (test cases from the solution guide)
---------------------------------------------
HAPPY CASE
Input: 
get_out_movie = {
    "Daniel Kaluuya": ["Allison Williams"],
    "Allison Williams": ["Daniel Kaluuya", "Catherine Keener", "Bradley Whitford"],
    "Bradley Whitford": ["Allison Williams", "Catherine Keener"],
    "Catherine Keener": ["Allison Williams", "Bradley Whitford"],
    "Jordan Peele": ["Jason Blum", "Gregory Plotkin", "Toby Oliver"],
    "Toby Oliver": ["Jordan Peele", "Gregory Plotkin"],
    "Gregory Plotkin": ["Jason Blum", "Toby Oliver", "Jordan Peele"],
    "Jason Blum": ["Jordan Peele", "Gregory Plotkin"]
}

Output:
[
    ['Daniel Kaluuya', 'Allison Williams', 'Catherine Keener', 'Bradley Whitford'],
    ['Jordan Peele', 'Jason Blum', 'Gregory Plotkin', 'Toby Oliver']
]
Explanation: The function correctly separates the cast from the crew into two distinct groups.
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

def get_groups(cast_and_crew):
    pass
