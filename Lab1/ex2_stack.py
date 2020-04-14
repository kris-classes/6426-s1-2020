"""
ISCG6426 Lab 1 Semester 1 2020 by Kris Pritchard / @krisrp

Tests used to check correctness of Lab1 answers.
This file requires 'pytest' and 'pyexpect' to run.
Install them with the following command:
    pip install pytest pyexpect

Then run the file with:
    pytest -xv ex2_stack_tests.py

You need to implement this code so that all of the tests pass.
Feel free to comment out specific tests, but only submit your answers files.
When checking your answers I will use the test files from this repository.


Stack (LIFO):
    For this introductory lab you need to implement functionality for a basic stack data structure.
    Performance doesn't matter for this.
    None of the method implementations require more than 4 lines of code.
"""


# IMPLEMENT a StackException.


# IMPLEMENT a StackIsEmptyException which inherits from StackException.


# IMPLEMENT a StackIsFullException which inherits from StackException.



class Stack:
    """
    Basic implementation of a stack
    """
    def __init__(self, maxsize=5):
        self.stack = []
        self.maxsize = maxsize

    def __str__(self):
        # Used when you print(my_stack)
        return 'Stack __str__(): FIX ME'

    def __repr__(self):
        # Used when you type my_stack into the shell.
        return 'Stack __repr__(): FIX ME'

    @property
    def size(self):
        # Return the size of the stack.
        # NOTE: The @property decorator lets you use self.size instead of self.size()
        return 'Stack size(): FIX ME'

    @property
    def is_empty(self):
        # Return whether or not the stack is empty.
        # NOTE: The @property decorator lets you use self.is_empty instead of self.is_empty()
        # Hint: Use self.size from above.
        return 'Stack is_empty: FIX ME'

    @property
    def is_full(self):
        # Return whether or not the stack is full.
        # NOTE: The @property decorator lets you use self.is_full instead of self.is_full()
        # Hint: Use self.size from above.
        return 'Stack is_full: FIX ME'

    def push(self, item):
        # Push an item onto the stack. Raise a StackIsFullException if the stack exceeds maxsize.
        # NOTE: Use self.is_full which you implemented earlier.
        print('Stack push(). FIX ME')

    def peek(self):
        # Return the current item on top of the stack, but don't pop it.
        # Return None if the stack is empty.
        # Hint: How do you access the last item in a list?
        return 'Stack peek(). FIX ME'

    def pop(self):
        # Pop an item off the stack. Raise a StackIsEmptyException if the stack is empty.
        # NOTE: Use self.is_empty which you implemented earlier.
        return 'Stack pop(). FIX ME'

