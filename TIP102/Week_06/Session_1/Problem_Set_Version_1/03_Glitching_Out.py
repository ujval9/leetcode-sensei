r"""
TIP102 | Week 6 | Session 1 | Problem Set Version 1 | Problem 3
Glitching Out

Source: statement reconstructed from the CodePath solution guide and written in our own words.
The original course page is behind a login, so wording and details may differ slightly.
Solution guide (only after you have tried!): https://github.com/codepath/compsci_guides/wiki/Glitching-Out

PROBLEM
-------
Write `remove_song(playlist_head, song)` that removes the first node whose song matches `song` and returns the head of the playlist.

EXAMPLES (test cases from the solution guide)
---------------------------------------------
HAPPY CASE
Input: playlist = SongNode("SOS", "ABBA", SongNode("Dreams", "Fleetwood Mac", SongNode("Lovely Day", "Bill Withers"))), song = "Dreams"
Output: ("SOS", "ABBA") -> ("Lovely Day", "Bill Withers")
Explanation: "Dreams" is correctly removed from the list.

EDGE CASE
Input: playlist = None, song = "Dreams"
Output: None
Explanation: An empty list remains empty.

EDGE CASE
Input: playlist = SongNode("SOS", "ABBA"), song = "Dreams"
Output: ("SOS", "ABBA")
Explanation: Since "Dreams" is not present, the list remains unchanged.
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


def remove_song(playlist_head, song):
    pass
