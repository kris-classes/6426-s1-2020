"""
ISCG6426 Lab 1 Semester 1 2020 by Kris Pritchard / @krisrp

Tests used to check correctness of Lab1 answers.
This file requires 'pytest' and 'pyexpect' to run.
Install them with the following command:
    pip install pytest pyexpect

Then run the file with:
    pytest -xv ex5_dictionary_tests.py

You need to implement this code so that all of the tests pass.
Feel free to comment out specific tests, but only submit your answers files.
When checking your answers I will use the test files from this repository.


Naive Dictionary (Interface):
    For this introductory lab you need to implement functionality for a basic dictionary/hashmap data structure.
    Performance doesn't matter for this.
    None of the method implementations require more than 6 lines of code.
"""


# IMPLEMENT a DictionaryException.


# IMPLEMENT a DictionaryKeyNotFoundException which inherits from DictionaryException.


class Dictionary:
    """
    Basic silly implementation of a dictionary/hashtable.
    This is more to demonstrate how the interface of a dictionary behaves.
    """
    def __init__(self, initial_data=None):
        if initial_data:
            self.data = initial_data
        else:
            self.data = {}

    def __str__(self):
        # Used when you print(my_dictionary)
        # e.g. print(my_dictionary) returns <Dictionary __str__: [1, 2, 3]>
        return f'dictionary __str__(). Implement me.'

    def __repr__(self):
        # Used when you type my_dictionary into the shell.
        # e.g. Typing my_dictionary in shell displays <Dictionary __repr__: [1, 2, 3]>
        return f'dictionary __repr__(). Implement me.'

    def __getitem__(self, key):
        # Return an item from the dictionary using my_dictionary['some_key']
        # NOTE: Raise DictionaryKeyNotFoundException if key doesn't exist.
        print('dictionary __getitem__(). Implement me.')

    def __setitem__(self, key, value):
        # Set an item in the dictionary using my_dictionary['key'] = value
        print('dictionary __setitem__(). Implement me.')

    def get(self, key, default=None):
        # IMPLEMENT: Try to get my_dictionary['key'] and return default if it doesn't exist.
        # NOTE: This has different behaviour from __getitem__, which raises
        # DictionaryKeyNotFoundException if the key doesn't exist.
        print('dictionary get(). Implement me.')

    def keys(self):
        # Return the dictionary's keys
        print('dictionary keys(). Implement me.')

    def values(self):
        # Return the dictionary's values
        print('dictionary values(). Implement me.')

    def items(self):
        # Return the dictionary's items
        print('dictionary items(). Implement me.')

