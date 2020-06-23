"""
ISCG6426 Lab 3 Semester 1 2020 by Kris Pritchard / @krisrp

Implement a priority queue which uses Python's heapq module

This lab requires you install the following packages:
    pip install pytest pylint pyexpect
"""
import heapq


# TODO: Create 3 exceptions here.
#
# QueueException which inherits from Exception class
# QueueIsFullException which inherits from QueueException class
# QueueIsEmptyException which inherits from QueueException class

# TODO: Remember to periodically run pylint on your code
# pylint heap_priority_queue.py
# Fix your code until you get a 10.00/10 rating.

class PriorityQueue:
    """
    Implementation of a priority queue using a binary min-heap data structure and Python's heapq module.
    NOTE: For simplicity in this lab we'll just use unique integers and A-Z names to represent priorities, with no tuple items like in Lab1.
    """
    def __init__(self, queue=None, maxsize=15):
        # TODO: If queue is None create a new one from a list, otherwise use it.

        # TODO: Remember to heapify the queue. NOTE: that heapify() changes the list in-place, and doesn't return any value.

        # TODO: Remember to set the maxsize.
        pass

    def __str__(self):
        # Used when you print(my_priorityqueue)
        # This is also how you access class metadata, in case your class name ever changes.

        # TODO: Implement __str__()
        return f'IMPLEMENT ME'

    def __repr__(self):
        # Used when you type my_priorityqueue into the shell.

        # TODO: Implement __repr__()
        return f'IMPLEMENT ME'

    @property
    def size(self):
        # Return the size of the queue.
        # NOTE: The @property decorator lets you use self.size instead of self.size()

        # TODO: Implement size()
        return 'IMPLEMENT ME'

    def is_empty(self):
        # Return whether or not the queue is empty.
        # Hint: Use self.size from earlier.

        # TODO: Implement is_empty()
        return 'IMPLEMENT ME'

    def is_full(self):
        # Return whether or not the queue is full.

        # TODO: Implement is_full()
        return 'IMPLEMENT ME'

    def push(self, value):
        # Add a value to the queue and maintain heap condition.

        # TODO: Implement push()
        print('IMPLEMENT ME')

    def peek(self):
        # Return the highest priority item, but don't remove it from the queue.
        # Return None if queue is empty.

        # TODO: Implement peek()
        return 'IMPLEMENT ME'

    def pop(self):
        # Remove the item from the top of the heap.
        # Raise a QueueIsEmptyException if the queue is empty.

        # TODO: Implement pop()
        return 'IMPLEMENT ME'

