"""
ISCG6426 Lab 1 Semester 1 2020 by Kris Pritchard / @krisrp

Tests used to check correctness of Lab1 answers.
This file requires 'pytest' and 'pyexpect' to run.
Install them with the following command:
    pip install pytest pyexpect

Then run the file with:
    pytest -xv ex6_set_tests.py

You need to implement this code so that all of the tests pass.
Feel free to comment out specific tests, but only submit your answers files.
When checking your answers I will use the test files from this repository.

Set (No Duplicates / Unique Items Only / Mathematical Set):
    For this introductory lab you need to implement functionality for a basic set data structure.
    Performance doesn't matter for this.
    None of the method implementations require more than 7 lines of code.
"""


# IMPLEMENT a SetException.


# IMPLEMENT a SetElementNotFoundException which inherits from SetException.


class Set:
    """
    Basic implementation of a set.
    Set must NOT contain duplicates.
    NOTE: You're not allowed to use Python's built-in set() for this. Sorry!
    If you use set() you will get 0 marks for this question.
    Hint: Use 'in' and 'not in' a lot.
    """
    def __iter__(self):
        # NOTE: You don't need to change this method.
        # It's here so you can type: for element in other_set: instead of other_set.data.
        self.n = 0
        return self

    def __next__(self):
        # NOTE: You don't need to change this method.
        # It's here so you can type: for element in other_set: instead of other_set.data.
        if self.n < len(self.data):
            result = self.data[self.n]
            self.n += 1
            return result
        else:
            raise StopIteration

    def __init__(self, initial_data=None):
        # NOTE: You don't need to change this method.
        # I've implemented it to show how it's done.
        # self.data MUST remain a list throughout this class.
        if initial_data is None:
            initial_data = []

        unique_only = []
        for element in initial_data:
            if element not in unique_only:
                unique_only.append(element)

        self.data = unique_only

    def __str__(self):
        # Used when you print(my_set)
        # NOTE: Use the trick from List's __str__ method.
        return f'set __str__(). Implement me.'

    def __repr__(self):
        # Used when you type my_set into the shell.
        return f'set __repr__(). Implement me.'

    def __contains__(self, element):
        # Used when you type element in my_set.
        # e.g. 3 in my_set.
        print('set __contains__(). Implement me.')

    def add(self, element):
        # Add an element to a set, making sure there are no duplicates.
        # Hint: If element not in self.data, add it.
        print('set add(). Implement me.')

    def remove(self, element):
        # Remove an element from a set.
        # Hint: If element not in self.data, raise SetElementNotFoundException.
        print('set remove(). Implement me.')

    def isdisjoint(self, other_set):
        # Return False if either set has the same item. Otherwise return True.
        return False  # IMPLEMENT ME and add logic.

    def union(self, other_set):
        # Combine this set with other_set and remove any duplicates.
        # Return a NEW Set but don't modify this one.
        # NOTE: Remember to use lists here instead of set.union.
        # IMPLEMENT THIS.
        return Set()  # You'll need to change this line too.

    def intersection(self, other_set):
        # Return a new Set with ONLY elements in both sets.
        # NOTE: Remember to use lists here instead of set.intersection.
        # IMPLEMENT THIS.
        return Set()  # You'll need to change this line.

    def difference(self, other_set):
        # Return a new Set with elements in this set but NOT in other_set.
        # IMPLEMENT THIS.
        return Set()  # You'll need to change this line too.

    def symmetric_difference(self, other_set):
        # Return a new Set with elements ONLY in either this set or other_set, but not both sets.
        # Hint: Start with a copy of our data and compare it to elements in other_set.
        return Set()  # You'll need to change this line too.

