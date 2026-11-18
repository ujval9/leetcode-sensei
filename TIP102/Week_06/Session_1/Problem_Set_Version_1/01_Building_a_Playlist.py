r"""
TIP102 | Week 6 | Session 1 | Problem Set Version 1 | Problem 1
Building a Playlist

Source: statement reconstructed from the CodePath solution guide and written in our own words.
The original course page is behind a login, so wording and details may differ slightly.
Solution guide (only after you have tried!): https://github.com/codepath/compsci_guides/wiki/Building-a-Playlist

PROBLEM
-------
Rewrite the given one-line nested `SongNode(...)` constructor as several separate statements that create each node and then link them, producing the same playlist.

EXAMPLES (test cases from the solution guide)
---------------------------------------------
HAPPY CASE
Input: top_hits_2010s = SongNode("Uptown Funk", SongNode("Party Rock Anthem", SongNode("Telephone")))
Output: Uptown Funk -> Party Rock Anthem -> Telephone
Explanation: The output is the linked list where each node points to the next in sequence.

EDGE CASE
Input: top_hits_2010s = None
Output: (no output)
Explanation: An empty list (no nodes) should simply print nothing.
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

class SongNode:
    def __init__(self, song, next=None):
        self.song = song
        self.next = next
