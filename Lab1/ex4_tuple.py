"""
DO NOT MODIFY THIS FILE.

ISCG6426 Lab 1 Semester 1 2020 by Kris Pritchard / @krisrp

Tests used to check correctness of Lab1 answers.
This file requires 'pytest' and 'pyexpect' to run.
Install them with the following command:
    pip install pytest pyexpect

Then run the file with:
    pytest -xv ex4_tuple_tests.py

You need to implement this code so that all of the tests pass.
Feel free to comment out specific tests, but only submit your answers files.
When checking your answers I will use the test files from this repository.


Tuple (Immutable Container):
    For this introductory lab you need to implement functionality for a basic tuple data structure.
    Performance doesn't matter for this.
    None of the method implementations require more than 6 lines of code.
"""

# IMPLEMENT a TupleException.


# IMPLEMENT a TupleIndexException which inherits from TupleException.


# IMPLEMENT a TupleModifyException which inherits from TupleException.



class Tuple:
    """
    A tuple is an immutable data structure which only supports simple operations.
    """
    def __init__(self, initial_data=None):
        # NOTE: Don't change this from a list.
        if initial_data:
            self.data = initial_data
        else:
            self.data = []

    def __str__(self):
        # Print class name and contents of tuple
        # e.g. print(my_tuple) returns <Tuple __str__: [1, 2, 3]>
        return f'tuple __str__(). Implement me.'

    def __repr__(self):
        # Display class name and contents of tuple
        # e.g. Typing my_tuple in shell displays <Tuple __repr__: [1, 2, 3]>
        return f'tuple __repr__(). Implement me.'

    def __getitem__(self, index):
        # Returns item at index 123 when we type my_tuple[123].
        # IMPLEMENT: Raise a TupleIndexException if accessing index that doesn't exist.
        print('tuple __getitem__(). Implement me.')

    def __setitem__(self, index, item):
        # Tuple's don't support item assignment.
        # IMPLEMENT: Immediately raise a TupleModifyException when trying to change an item.
        print('tuple __setitem__(). Implement me.')

    def __add__(self, other):
        # Add two Tuples together and return a new Tuple.
        print('tuple __add__(). Implement me.')

    def count(self, value):
        # Return number of occurrences of value.
        print('tuple count(). Implement me.')

    def index(self, value):
        # Return the index of value in self.data.
        print('tuple index(). Implement me.')

