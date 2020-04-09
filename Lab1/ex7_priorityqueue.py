"""
ISCG6426 Lab 1 Semester 1 2020 by Kris Pritchard / @krisrp

Tests used to check correctness of Lab1 answers.
This file requires 'pytest' and 'pyexpect' to run.
Install them with the following command:
    pip install pytest pyexpect

Then run the file with:
    pytest -xv ex7_priorityqueue_tests.py

You need to implement this code so that all of the tests pass.
Feel free to comment out specific tests, but only submit your answers files.
When checking your answers I will use the test files from this repository.

PriorityQueue (FIFO with Priority):
    For this introductory lab you need to implement functionality for a naive priorityqueue data structure.
    Performance doesn't matter for this.
    None of the method implementations require more than 7 lines of code.
"""
"""
This is a naive priority queue implementation.
Tasks required:
    - Implement the __str__ method so that:
        q = PriorityQueue()
        str(q)  # Returns
    - Implement __repr__

"""
# Import QueueIsFullException and QueueIsEmptYException from earlier.
from ex3_queue import *


class PriorityQueue:
    """
    Basic implementation of a naive priority queue using a deque data structure.

    Insertion is O(1) but lookup is O(n).
    """
    def __init__(self, maxsize=5):
        self.queue = []
        self.maxsize = maxsize

    def __str__(self):
        # Used when you print(my_priorityqueue)
        # Where ??? is the queue data.
        # Hint: Create a new queue object and use print(my_queue) to test it.
        # TODO: This method needs to return <PriorityQueue __str__: ???>
        return f'priorityqueue __str__(). Implement me.'

    def __repr__(self):
        # Used when you type my_priorityqueue into the shell.
        # Where ??? is the queue data.
        # Hint: Create a new queue object and use repr(my_queue) to test it.
        # TODO: This method needs to return <PriorityQueue __repr__: ???>
        return f'priorityqueue __repr__(). Implement me.'

    @property
    def size(self):
        # Return the size of the queue.
        # NOTE: The @property decorator lets you use self.size instead of self.size()
        # TODO: This method needs to return the current queue size.
        return 'Implement Me'

    @property
    def is_empty(self):
        # Return whether or not the queue is empty.
        # Hint: Use self.size from earlier.
        # NOTE: The @property decorator lets you use self.is_empty instead of self.is_empty()
        # TODO: This method needs to return True or False if the queue is empty.
        return 'Implement Me'

    @property
    def is_full(self):
        # Return True or False if the queue is full.
        # NOTE: The @property decorator lets you use self.is_full instead of self.is_full()
        # TODO: This method needs to return True or False if the queue is full.
        return 'Implement Me'

    def put(self, item, priority='normal'):
        # NOTE: Insertion order of two items with the same priority must be maintained.
        # TODO: Add a tuple with (item, priority) to the start of the queue.
        print('priorityqueue put(). Implement me.')


    def front(self):
        # NOTE: Requires that you search the list for the highest priority item.
        # Hint: Learn how enumerate() works to simplify your code.
        # TODO: Return the POSITION/index of the highest priority item but DO NOT modify the queue.
        print('priorityqueue front(). Implement me.')
        return 'Implement Me'

    def peek(self):
        # Return the highest priority item, but don't remove it from the queue.
        # Return None if the queue is empty.
        # NOTE: Remember to just return the item itself, not the priority too.
        print('priorityqueue peek(). Implement me.')
        return 'Implement Me'

    def get(self):
        # Remove the item with the highest priority from the queue.
        # Raise a QueueException if the queue is empty.
        # NOTE: Remember to just return the item itself, not the priority too.
        print('priorityqueue get(). Implement me.')
        return 'Implement Me'

