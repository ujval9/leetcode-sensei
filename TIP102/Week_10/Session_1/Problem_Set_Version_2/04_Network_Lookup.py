r"""
TIP102 | Week 10 | Session 1 | Problem Set Version 2 | Problem 4
Network Lookup

Source: statement reconstructed from the CodePath solution guide and written in our own words.
The original course page is behind a login, so wording and details may differ slightly.
Solution guide (only after you have tried!): https://github.com/codepath/compsci_guides/wiki/Network-Lookup

PROBLEM
-------
Each item in `clients` is a pair of celebrities who have worked together. Write `get_adj_matrix(clients)` that assigns each celebrity a unique integer ID and returns both the ID dictionary and an adjacency matrix of the collaborations.

EXAMPLES (test cases from the solution guide)
---------------------------------------------
HAPPY CASE
Input: clients = [
                    ["Yalitza Aparicio", "Julio Torres"], 
                    ["Julio Torres", "Fred Armisen"], 
                    ["Bowen Yang", "Julio Torres"],
                    ["Bowen Yang", "Margaret Cho"],
                    ["Margaret Cho", "Ali Wong"],
                    ["Ali Wong", "Fred Armisen"], 
                    ["Ali Wong", "Bowen Yang"]
                 ]
Output:
id_map = {
  'Ali Wong': 0,
  'Bowen Yang': 1,
  'Fred Armisen': 2,
  'Julio Torres': 3,
  'Margaret Cho': 4,
  'Yalitza Aparicio': 5
}
adj_matrix = [
  [0, 1, 1, 0, 1, 0],  # Ali Wong
  [1, 0, 0, 1, 1, 0],  # Bowen Yang
  [1, 0, 0, 1, 0, 0],  # Fred Armisen
  [0, 1, 1, 0, 0, 1],  # Julio Torres
  [1, 1, 0, 0, 0, 0],  # Margaret Cho
  [0, 0, 0, 1, 0, 0]   # Yalitza Aparicio
]
Explanation: The dictionary maps celebrities (in sorted order) to IDs and the adjacency matrix shows their connections.

EDGE CASE
Input: clients = []
Output: {}, []
Explanation: No relationships exist, so the result is an empty dictionary and an empty matrix.
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

def get_adj_matrix(clients):
    pass
