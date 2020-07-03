"""
ISCG6426 Lab 3 Semester 1 2020 by Kris Pritchard / @krisrp

Implement a priority queue which uses Python's heapq module

This lab requires you install the following packages:
    pip install pytest pylint pyexpect
"""
import heapq
import random

random_list = [random.randint(0, 9) for i in range(10)]
sorted_list = [i for i in range(10)]


class QueueException(Exception):
    """QueueException which inherits from Exception class"""
    pass


class QueueIsFullException(QueueException):
    """QueueIsFullException which inherits from QueueException class"""
    pass


class QueueIsEmptyException(QueueException):
    """QueueIsEmptyException which inherits from QueueException class"""
    pass


class PriorityQueue:
    """Priority queue using a binary min-heap data structure and Python's heapq module."""

    def __init__(self, queue=None, maxsize=10):
        if queue is None:
            self.queue = []
            self.newQueue = []
        else:
            self.queue = queue
            self.newQueue = queue
        self.maxsize = maxsize
        self.random_list= []
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
        self.value = value
        if self.maxsize <= self.size:
            raise QueueIsFullException("<Priority Queue is Full>")
        print(self.queue)
        heapq.heappush(self.queue, self.value)

    def peek(self):
        """Return the highest priority item, but don't remove it from the queue."""
        print(self.queue)

        if self.size == 0:
            return None

        return self.queue[0]

    def pop(self):
        """Remove the item from the top of the heap."""
        heapq.heapify(self.queue)
        if self.size <= 0:
            raise QueueIsEmptyException("<Priority Queue is empty>")

        return self.queue.pop(0)

    def setList(self, value):
        self.value = value
        if self.value == 0:
            return sorted_list
        elif self.value == 1:
            return random_list
        else:
            print("Error")
            pass

    def runHeapify(self):
        if self.newQueue:
            self.newQueue = []
        if self.queue:
            print(self.queue)
            for i in self.queue:
                self.newQueue.append(i)
                print(self.queue)
                print(self.newQueue)
            heapq.heapify(self.newQueue)
        return self.newQueue

    def changeRandomList(self):
        self.random_list = [random.randint(0, 9) for i in range(10)]
        return self.random_list


'''pq = PriorityQueue()
pq.queue = pq.setList(1)
print(pq.runHeapify())'''
