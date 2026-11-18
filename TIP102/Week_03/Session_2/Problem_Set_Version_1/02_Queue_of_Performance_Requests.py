r"""
TIP102 | Week 3 | Session 2 | Problem Set Version 1 | Problem 2
Queue of Performance Requests

Source: statement reconstructed from the CodePath solution guide and written in our own words.
The original course page is behind a login, so wording and details may differ slightly.
Solution guide (only after you have tried!): https://github.com/codepath/compsci_guides/wiki/Queue-of-Performance-Requests

PROBLEM
-------
Each request is a (priority, performance_name) tuple. Return the performance names in processing order, with higher priority first.
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

from collections import deque


def process_performance_requests(requests):
    pass


if __name__ == "__main__":
    # Example usage
    print(process_performance_requests([(3, 'Dance'), (5, 'Music'), (1, 'Drama')]))
    # Output: ['Music', 'Dance', 'Drama']

    print(process_performance_requests([(2, 'Poetry'), (1, 'Magic Show'), (4, 'Concert'), (3, 'Stand-up Comedy')]))
    # Output: ['Concert', 'Stand-up Comedy', 'Poetry', 'Magic Show']

    print(process_performance_requests([(1, 'Art Exhibition'), (3, 'Film Screening'), (2, 'Workshop'), (5, 'Keynote Speech'), (4, 'Panel Discussion')]))
    # Output: ['Keynote Speech', 'Panel Discussion', 'Film Screening', 'Workshop', 'Art Exhibition']
