r"""
TIP102 | Week 6 | Session 1 | Problem Set Version 1 | Problem 2
Top Artists

Source: statement reconstructed from the CodePath solution guide and written in our own words.
The original course page is behind a login, so wording and details may differ slightly.
Solution guide (only after you have tried!): https://github.com/codepath/compsci_guides/wiki/Top-Artists

PROBLEM
-------
Each node in the playlist holds a song, its artist, and `next`. Write `get_artist_frequency(playlist)` that returns a dict mapping each artist to how many songs of theirs appear.

EXAMPLES (test cases from the solution guide)
---------------------------------------------
HAPPY CASE
Input: playlist = SongNode("Saturn", "SZA", SongNode("Who", "Jimin", SongNode("Espresso", "Sabrina Carpenter", SongNode("Snooze", "SZA"))))
Output: {"SZA": 2, "Jimin": 1, "Sabrina Carpenter": 1}
Explanation: The artist "SZA" appears twice, while "Jimin" and "Sabrina Carpenter" appear once.

EDGE CASE
Input: playlist = None
Output: {}
Explanation: An empty linked list should return an empty dictionary.
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
    def __init__(self, song, artist, next=None):
        self.song = song
        self.artist = artist
        self.next = next


# Helper for testing (provided)
def print_linked_list(node):
    current = node
    while current:
        print((current.song, current.artist), end=" -> " if current.next else "")
        current = current.next
    print()


def get_artist_frequency(playlist):
    pass
