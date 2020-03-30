"""
Implement the following data structures.
List has been implemented to show how to do it.
"""
import unittest
import collections


# An example ListException
class ListException(Exception):
    pass

# IMPLEMENT a TupleException

# IMPLEMENT a DictionaryException

# IMPLEMENT a SetException

# IMPLEMENT a StackException

# IMPLEMENT a QueueException


class List:
    """
    Basic List Data Structure
    """
    def __init__(self):
        self.data = []

    def __str__(self):
        # Used when you print(my_list)
        return f'List data __str__: {data}'

    def __repr__(self):
        # Used when you type my_list into the shell.
        return f'List data __repr__: {data}'

    def append(self, item):
        # Adds an item to the end of the list.
        self.data.append(item)

    def pop(self):
        # Remove and return an item from the end of the list.
        if len(self.data) == 0:
            raise ListException('Tried to pop() from empty list.')
        else:
            return self.data.pop()

    def insert(self, index, item):
        # Insert an item at index
        self.item.insert(index, item)

    def clear(self):
        self.data = []



class Tuple:
    """
    A tuple is an immutable data structure which only supports simple operations.
    """
    def __init__(self):
        self.data = []  # MUST USE A LIST. DON'T CHANGE THIS.

    def __str__(self):
        # Used when you print(my_tuple)
        print('tuple __str__(). Implement me.')

    def __repr__(self):
        # Used when you type my_tuple into the shell.
        print('tuple __repr__(). Implement me.')

    def count(self, value):
        # Return number of occurrences of value.
        print('tuple count(). Implement me.')

    def index(self, value):
        # Return the index of value in self.data.
        print('tuple index(). Implement me.')


class Dictionary:
    """
    Basic implementation of a dictionary/hashtable.
    """
    def __init__(self):
        self.data = {}

    def __str__(self):
        # Used when you print(my_dictionary)
        print('dictionary __str__(). Implement me.')

    def __repr__(self):
        # Used when you type my_dictionary into the shell.
        print('dictionary __repr__(). Implement me.')

    def __getitem__(self, key):
        # Return an item from the dictionary using my_dictionary['some_key']
        print('dictionary __getitem__(). Implement me.')

    def __setitem__(self, key, item):
        # Set an item in the dictionary using my_dictionary['some_key'] = some_item
        print('dictionary __setitem__(). Implement me.')

    def keys(self):
        # Return the dictionary's keys
        print('dictionary keys(). Implement me.')

    def values(self):
        # Return the dictionary's values
        print('dictionary values(). Implement me.')

    def items(self):
        # Return the dictionary's items
        print('dictionary items(). Implement me.')


class Set:
    """
    Basic implementation of a set.
    Set must NOT contain duplicates.
    NOTE: You're not allowed to use Python's built-in set() for this.
    """
    def __init__(self):
        self.data = []  # DON'T CHANGE THIS FROM A LIST.

    def __str__(self):
        # Used when you print(my_set)
        print('set __str__(). Implement me.')

    def __repr__(self):
        # Used when you type my_set into the shell.
        print('set __repr__(). Implement me.')

    def add(self, element):
        # Add an element to a set, making sure there are no duplicates.
        print('set add(). Implement me.')

    def remove(self, element):
        # Remove an element from a set. Raise a SetException if the item does not exist.
        print('set remove(). Implement me.')

    def union(self, other_set):
        # Combine this set with other_set and remove any duplicates.
        print('set union(). Implement me.')

    def intersection(self, other_set):
        # Return a new list with ONLY elements in both sets.
        print('set intersection(). Implement me.')


class Stack:
    """
    Basic implementation of a stack using a deque data structure.
    """
    def __init__(self):
        self.data = collections.deque()  # DON'T CHANGE THIS FROM A Double-Ended Queue (DEQUE).

    def __str__(self):
        # Used when you print(my_set)
        print('stack __str__(). Implement me.')

    def __repr__(self):
        # Used when you type my_set into the shell.
        print('stack __repr__(). Implement me.')

    def push(self, item):
        # Push an item onto the stack
        print('stack push(). Implement me.')

    def pop(self):
        # Pop an item off the stack. Raise a StackException if the stack is empty.
        print('stack pop(). Implement me.')


class Queue:
    """
    Basic implementation of a queue using a deque data structure.
    """
    def __init__(self):
        self.data = collections.deque()  # DON'T CHANGE THIS FROM A Double-Ended Queue (DEQUE).

    def __str__(self):
        # Used when you print(my_set)
        print('queue __str__(). Implement me.')

    def __repr__(self):
        # Used when you type my_set into the shell.
        print('queue __repr__(). Implement me.')

    def enqueue(self, item):
        # Add an item to the start of the queue.
        print('queue push(). Implement me.')

    def dequeue(self):
        # Remove an item to the end of the queue. Raise a QueueException if the queue is empty.
        print('queue pop(). Implement me.')


def recursion_example(n):
    print(f'Recursion level: {n}')

    # IMPLEMENT: Add a base-case here to stop and return n when n is 10.

    recursion_example(n - 1)




# DON'T CHANGE CODE BELOW THIS LINE



recursion_example(15)
