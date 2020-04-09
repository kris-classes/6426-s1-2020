"""
DO NOT MODIFY THIS FILE.

ISCG6426 Lab 1 Semester 1 2020 by Kris Pritchard / @krisrp

Tests used to check correctness of Lab1 answers.
This file requires 'pytest' and 'pyexpect' to run.
Install them with the following command:
    pip install pytest pyexpect

Then run the file with:
    pytest -xv ex3_queue_tests.py

You need to implement this code so that all of the tests pass.
Feel free to comment out specific tests, but only submit your answers files.
When checking your answers I will use the test files from this repository.


Queue (FIFO):
    For this introductory lab you need to implement functionality for a basic queue data structure.
    Performance doesn't matter for this.
    None of the method implementations require more than 4 lines of code.
"""
import collections


# IMPLEMENT a QueueException.


# IMPLEMENT a QueueIsEmptyException which inherits from QueueException.


# IMPLEMENT a QueueIsFullException which inherits from QueueException.



class Queue:
    """
    Basic implementation of a queue using a deque data structure.
    """
    def __init__(self, maxsize=5):
        self.queue = collections.deque()
        self.maxsize = maxsize

    def __str__(self):
        # Used when you print(my_queue)
        return f'queue __str__(). Implement me.'

    def __repr__(self):
        # Used when you type my_queue into the shell.
        return f'queue __repr__(). Implement me.'

    @property
    def size(self):
        # Return the size of the stack.
        # NOTE: The @property decorator lets you use self.size instead of self.size()
        return 0  # IMPLEMENT THIS.

    @property
    def is_empty(self):
        # Return whether or not the queue is empty.
        # NOTE: The @property decorator lets you use self.is_empty instead of self.is_empty()
        # Hint: Use self.size from above.
        return False  # IMPLEMENT THIS.

    @property
    def is_full(self):
        # Return whether or not the queue is full.
        # NOTE: The @property decorator lets you use self.is_full instead of self.is_full()
        # Hint: Use self.size from above.
        return False  # IMPLEMENT THIS.

    def put(self, item):
        # Add an item to the start of the queue.
        # Raise a QueueIsFullException if the queue is full.
        # HINT: help(collections.deque) and self.is_full
        print('queue put(). Implement me.')

    def peek(self):
        # Return the item at the front of the queue but don't pop it.
        # Return None if the queue is empty.
        # Hint: How do you access the first/last item in a list?
        print('queue peek(). Implement me.')
        return 'Implement Me'

    def get(self):
        # Remove an item to the end of the queue. Raise a QueueException if the queue is empty.
        print('queue get(). Implement me.')
        return 'Implement Me'

