r"""
TIP102 | Week 6 | Session 1 | Problem Set Version 1 | Problem 5
Looped

Source: statement reconstructed from the CodePath solution guide and written in our own words.
The original course page is behind a login, so wording and details may differ slightly.
Solution guide (only after you have tried!): https://github.com/codepath/compsci_guides/wiki/Looped

PROBLEM
-------
Write `loop_length(playlist_head)` that returns the number of nodes in the cycle if the linked list has one, otherwise 0.

EXAMPLES (test cases from the solution guide)
---------------------------------------------
HAPPY CASE
Input: playlist with 4 songs, where the last song points to the second song
Output: 3
Explanation: The linked list contains a cycle of length 3.

EDGE CASE
Input: playlist = None
Output: 0
Explanation: An empty list does not contain a cycle.

EDGE CASE
Input: playlist with 3 songs, no cycle
Output: 0
Explanation: The linked list does not contain a cycle.
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


def loop_length(playlist_head):
    pass
