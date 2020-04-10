"""
Implement a base case for this recursive function.
"""
import sys
from functools import lru_cache


RECURSION_LIMIT = 100 # Default is 1000
sys.setrecursionlimit(RECURSION_LIMIT)


def recursion_base_case(n, stop=10):
    # TODO: Add a recursion base-case here to stop and return n when n == stop.
    # Hint: 2 lines of code.

    return recursion_base_case(n - 1, stop=stop)


def recursive_fibonacci(n):
    """
    Calculates the Fibonacci sequence of N items using recursion.
    e.g. 1 1 2 3 5 8 13 ...
    (1 + 1 == 2), (1 + 2 == 3), (2 + 3 == 5), (3 + 5 == 8), etc.

    NOTE: Notice how fast this slows down after n=35
    """
    if n <= 1:
        return n
    else:
        return recursive_fibonacci(n-1) + recursive_fibonacci(n-2)


@lru_cache  # Uses memoization to cache results of each execution
def recursive_memoization_fibonacci(n):
    """
    The exact same function using 'memoization', which is to keep track of each item as you go.
    NOTE: See how much faster this version is for n=40.
    This is the difference a slight algorithmic change can make.
    Try it with n=90.
    Try change RECURSION_LIMIT back to 1000 and see how high n can go.
    See https://en.wikipedia.org/wiki/Memoization
    """
    if n <= 1:
        return n
    else:
        return recursive_memoization_fibonacci(n-1) + recursive_memoization_fibonacci(n-2)

