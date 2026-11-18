r"""
TIP102 | Week 10 | Session 1 | Problem Set Version 2 | Problem 1
Hollywood Stars

Source: statement reconstructed from the CodePath solution guide and written in our own words.
The original course page is behind a login, so wording and details may differ slightly.
Solution guide (only after you have tried!): https://github.com/codepath/compsci_guides/wiki/Hollywood-Stars

PROBLEM
-------
Represent the given network of celebrities (an undirected graph showing who has worked with whom) as an adjacency dictionary mapping each celebrity to a list of their connections.

EXAMPLES (test cases from the solution guide)
---------------------------------------------
HAPPY CASE
Input: Create an adjacency dictionary for a graph with nodes representing celebrities (Kevin Bacon, Meryl Streep, Idris Elba, Laverne Cox, Sofia Vergara) and their connections.
Output: {
  'Kevin Bacon': ['Laverne Cox', 'Sofia Vergara'],
  'Meryl Streep': ['Idris Elba', 'Sofia Vergara'],
  'Idris Elba': ['Meryl Streep', 'Laverne Cox'],
  'Laverne Cox': ['Kevin Bacon', 'Idris Elba'],
  'Sofia Vergara': ['Kevin Bacon', 'Meryl Streep']
}
Explanation: Each celebrity is connected to other celebrities based on the graph.

EDGE CASE
Input: A graph with no connections between some celebrities.
Output: The adjacency list should reflect isolated nodes, e.g., `'Kevin Bacon': []` if there are no connections for Kevin Bacon.
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

# Write your code here
