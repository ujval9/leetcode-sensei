r"""
TIP102 | Week 10 | Session 2 | Problem Set Version 2 | Problem 7
Maximizing Star Power

Source: statement reconstructed from the CodePath solution guide and written in our own words.
The original course page is behind a login, so wording and details may differ slightly.
Solution guide (only after you have tried!): https://github.com/codepath/compsci_guides/wiki/Maximizing-Star-Power

PROBLEM
-------
The graph connects pairs of celebrities, and each edge has a star power and a hiring cost. Write `find_max_star_power(collaboration_map, costar_a, costar_b)` that returns the maximum total star power achievable on a path from `costar_a` to `costar_b`.

EXAMPLES (test cases from the solution guide)
---------------------------------------------
HAPPY CASE
Input: 
```python
collaboration_map = {
    "Leonardo DiCaprio": [("Brad Pitt", 40), ("Robert De Niro", 30)],
    "Brad Pitt": [("Leonardo DiCaprio", 40), ("Scarlett Johansson", 20)],
    "Robert De Niro": [("Leonardo DiCaprio", 30), ("Chris Hemsworth", 50)],
    "Scarlett Johansson": [("Brad Pitt", 20), ("Chris Hemsworth", 30)],
    "Chris Hemsworth": [("Robert De Niro", 50), ("Scarlett Johansson", 30)]
}

print(find_max_star_power(collaboration_map, "Leonardo DiCaprio", "Chris Hemsworth"))
```
Output:
```markdown
90
Explanation: The maximum star power path is from Leonardo DiCaprio -> Brad Pitt -> Scarlett Johansson -> Chris Hemsworth with a total star power of 90 (40 + 20 + 30).
```

EDGE CASE
Input: 
```python
collaboration_map = {
    "Leonardo DiCaprio": [("Brad Pitt", 40)],
    "Brad Pitt": [("Leonardo DiCaprio", 40)]
}

print(find_max_star_power(collaboration_map, "Leonardo DiCaprio", "Brad Pitt"))
```
Output:
```markdown
40
Explanation: The only path is Leonardo DiCaprio -> Brad Pitt, with a star power of 40.
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

def find_max_star_power(collaboration_map, costar_a, costar_b):
    pass
