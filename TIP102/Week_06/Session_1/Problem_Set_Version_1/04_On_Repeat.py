r"""
TIP102 | Week 6 | Session 1 | Problem Set Version 1 | Problem 4
On Repeat

Source: statement reconstructed from the CodePath solution guide and written in our own words.
The original course page is behind a login, so wording and details may differ slightly.
Solution guide (only after you have tried!): https://github.com/codepath/compsci_guides/wiki/On-Repeat

PROBLEM
-------
Write `on_repeat(playlist_head)` that returns True if the linked list contains a cycle, otherwise False.

EXAMPLES (test cases from the solution guide)
---------------------------------------------
HAPPY CASE
Input: playlist with 4 songs, where the last song points to the second song
Output: True
Explanation: The linked list contains a cycle.

EDGE CASE
Input: playlist = None
Output: False
Explanation: An empty list does not contain a cycle.

EDGE CASE
Input: playlist with 3 songs, no cycle
Output: False
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


def on_repeat(playlist_head):
    pass
