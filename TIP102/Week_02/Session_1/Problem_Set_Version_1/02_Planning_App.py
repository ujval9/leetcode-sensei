r"""
TIP102 | Week 2 | Session 1 | Problem Set Version 1 | Problem 2
Planning App

Source: CodePath TIP102 course page (statement copied word for word from the course PDF).
Note: a few long lines were cut off at the right edge in the PDF; check the solution guide examples if a line looks incomplete.
Solution guide (only after you have tried!): https://github.com/codepath/compsci_guides/wiki/Planning-App

PROBLEM
-------
You are designing an app for your festival to help attendees have the
best experience possible! As part of the application, users will be able
to easily search their favorite artist and find out the day, time, and
stage the artist is playing at. Write a function get_artist_info()
that accepts a string artist and a dictionary festival_schedule
mapping artist's names to dictionaries containing the day, time, and
stage they are playing on. Return the dictionary containing the

information about the given artist .

If the artist searched for does not exist in festival_schedule ,
return the dictionary {"message": "Artist not found"} .

 def get_artist_info(artist, festival_schedule):
     pass

Example Usage:

 festival_schedule = {
     "Blood Orange": {"day": "Friday", "time": "9:00 PM", "stage": "Main
     "Metallica": {"day": "Saturday", "time": "8:00 PM", "stage": "Main
     "Kali Uchis": {"day": "Sunday", "time": "7:00 PM", "stage": "Second
     "Lawrence": {"day": "Friday", "time": "6:00 PM", "stage": "Main Sta
 }

 print(get_artist_info("Blood Orange", festival_schedule))
 print(get_artist_info("Taylor Swift", festival_schedule))

Example Output:

 {'day': 'Friday', 'time': '9:00 PM', 'stage': 'Main Stage'}
 {'message': 'Artist not found'}
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

def get_artist_info(artist, festival_schedule):
    pass
