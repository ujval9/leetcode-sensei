r"""
TIP102 | Week 11 | Session 1 | Problem Set Version 2 | Problem 1
Battle Moves

Source: statement reconstructed from the CodePath solution guide and written in our own words.
The original course page is behind a login, so wording and details may differ slightly.
Solution guide (only after you have tried!): https://github.com/codepath/compsci_guides/wiki/Battle-Moves

PROBLEM
-------
Write `next_moves(battle, row, column, past_moves)` that returns the valid adjacent cells (up, down, left, right) you can move to from (row, column), excluding cells already in `past_moves` and any blocked cells.

EXAMPLES (test cases from the solution guide)
---------------------------------------------
HAPPY CASE
Input: battle = [
    ['X', 'O', 'O', 'X', 'X'],
    ['O', 'O', 'O', 'X', 'X'],
    ['X', 'X', 'X', 'O', 'O'],
    ['X', 'X', 'X', 'X', 'O'],
    ['O', 'O', 'O', 'X', 'O']
], row = 3, column = 2, past_moves = []
Output: [(2, 2), (3, 3), (3, 1)]
Explanation: The valid adjacent cells (2, 2), (3, 3), and (3, 1) all belong to your territory.

EDGE CASE
Input: battle = [
    ['X', 'O', 'O', 'X', 'X'],
    ['O', 'O', 'O', 'X', 'X'],
    ['X', 'X', 'X', 'O', 'O'],
    ['X', 'X', 'X', 'X', 'O'],
    ['O', 'O', 'O', 'X', 'O']
], row = 0, column = 0, past_moves = []
Output: []
Explanation: All possible moves from this position are out of bounds or in enemy territory.
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

def next_moves(battle, row, column, past_moves):
    pass
