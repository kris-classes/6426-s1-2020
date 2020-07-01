"""
ISCG6426 Lab 3 Semester 1 2020 by Kris Pritchard / @krisrp

Implement a priority queue which uses Python's heapq module

This lab requires you install the following packages:
    pip install pytest pylint pyexpect
"""
import heapq


class QueueException(Exception):
    """QueueException which inherits from Exception class"""


class QueueIsFullException(QueueException):
    """QueueIsFullException which inherits from QueueException class"""


class QueueIsEmptyException(QueueException):
    """QueueIsEmptyException which inherits from QueueException class"""


class PriorityQueue:
    """Priority queue using a binary min-heap data structure and Python's heapq module."""

    def __init__(self, queue=None, maxsize=7):
        if queue is None:
            self.queue = []
        else:
            self.queue = queue

        heapq.heapify(self.queue)

        self.maxsize = maxsize

    def __str__(self):
        return f'<PriorityQueue __str__: {self.queue}>'

    def __repr__(self):
        return f'<PriorityQueue __repr__: {self.queue}>'

    @property
    def size(self):
        """ Return the size of the queue."""
        return len(self.queue)

    def is_empty(self):
        """ Return whether or not the queue is empty."""
        if self.size == 0:
            return True

        return False

    def is_full(self):
        """ Return whether or not the queue is full."""
        if self.maxsize <= self.size:
            return True

        return False

    def push(self, value):
        """ Add a value to the queue and maintain heap condition."""
        if self.maxsize <= self.size:
            raise QueueIsFullException("<Priority Queue is Full>")

        self.queue.append(value)
        heapq.heapify(self.queue)

    def peek(self):
        """Return the highest priority item, but don't remove it from the queue."""
        if self.size == 0:
            return None

        return self.queue[0]

    def pop(self):
        """Remove the item from the top of the heap."""
        heapq.heapify(self.queue)
        if self.size <= 0:
            raise QueueIsEmptyException("<Priority Queue is empty>")

        return self.queue.pop(0)
