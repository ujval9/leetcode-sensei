r"""
TIP102 | Week 2 | Session 1 | Problem Set Version 2 | Problem 2
Space Encyclopedia

Source: CodePath TIP102 course page (statement copied word for word from the course PDF).
Note: a few long lines were cut off at the right edge in the PDF; check the solution guide examples if a line looks incomplete.
Solution guide (only after you have tried!): https://github.com/codepath/compsci_guides/wiki/Space-Encyclopedia

PROBLEM
-------
Given a dictionary planets that maps planet names to a dictionary
containing the planet's number of moons and orbital period, write a
function planet_lookup() that accepts a string planet_name and
returns a string in the form
 Planet <planet_name> has an orbital period of <orbital period> Earth d
If planet_name is not a key in planets , return
  "Sorry, I have no data on that planet." .

 def planet_lookup(planet_name):
     pass

Example Usage:

 planetary_info = {
     "Mercury": {
         "Moons": 0,
         "Orbital Period": 88
     },

      "Earth": {
          "Moons": 1,
          "Orbital Period": 365.25
      },
      "Mars": {
          "Moons": 2,
          "Orbital Period": 687
      },
      "Jupiter": {
          "Moons": 79,
          "Orbital Period": 10592
      }
 }

 print(planet_lookup("Jupiter"))
 print(planet_lookup("Pluto"))

Example Output:

 Planet Jupiter has an orbital period of 10592 Earth days and has 79 moo
 Sorry, I have no data on that planet.
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

def planet_lookup(planets, planet_name):
    pass
