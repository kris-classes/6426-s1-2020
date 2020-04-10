"""
ISCG6426 Lab1 Semester 1 2020. Code by Kris Pritchard / @krisrp
Implement the following data structures.
List has been implemented to show how to do it.

NOTE: Each method only requires 1-7 lines of code. If you have more you're doing it wrong.
"""
import collections  # See help(collections.deque)


# An example ListException
class ListException(Exception):
    # A custom exception just inherits from the Exception class.
    # It does not need any additional code
    pass


class ListIsEmptyException(ListException):
    # Inherits from ListException
    pass


class ListIndexException(ListException):
    # Inherits from ListException
    pass

# IMPLEMENT a TupleException.

# IMPLEMENT a TupleIndexException which inherits from TupleException.

# IMPLEMENT a TupleModifyException which inherits from TupleException.

# IMPLEMENT a StackException.

# IMPLEMENT a StackIsEmptyException which inherits from StackException.

# IMPLEMENT a StackIsFullException which inherits from StackException.

# IMPLEMENT a QueueException.

# IMPLEMENT a QueueIsEmptyException which inherits from QueueException.

# IMPLEMENT a QueueIsFullException which inherits from QueueException.

# IMPLEMENT a DictionaryException.

# IMPLEMENT a DictionaryKeyNotFoundException which inherits from DictionaryException.

# IMPLEMENT a SetException.

# IMPLEMENT a SetElementNotFoundException which inherits from SetException.


def recursion_example(n, stop=10):
    print(f'Recursion level: {n}')

    # IMPLEMENT: Add a base-case here to stop and return n when n == stop.

    return recursion_example(n - 1, stop=stop)


# Sample Implementation of a List data structure.
class List:
    """
    Basic List Data Structure
    """
    def __init__(self, initial_data=[]):
        self.data = initial_data

    def __str__(self):
        # Used when you print(my_list)
        return f'<List __str__: {self.data}>'

    def __repr__(self):
        # Used when you type my_list into the shell.
        return f'<List __repr__: {self.data}>'

    def __getitem__(self, index):
        # Returns item at index 123 when we type my_list[123].
        try:
            item = self.data[index]
        except IndexError:
            raise ListIndexException(f'No item at index: {index}')
        except ZeroDivisionError:
            print('This is how you catch multiple exceptions.')
        else:
            return item
        finally:
            print(f'NOTE: This always runs.')

    def __setitem__(self, index, item):
        # Sets value at self.data[index] = item.
        self.data[index] = item

    def __add__(self, other):
        # Adds two items together and returns a new List.
        return List(self.data + other.data)

    @property  # @property lets you use my_list.size instead of my_list.size()
    def size(self):
        return len(self.data)

    def append(self, item):
        # Adds an item to the end of the list.
        self.data.append(item)

    def pop(self):
        # Remove and return an item from the end of the list.
        if len(self.data) == 0:
            raise ListIsEmptyException('Tried to pop() from empty list.')
        else:
            return self.data.pop()

    def insert(self, index, item):
        # Insert an item at index
        self.data.insert(index, item)

    def clear(self):
        self.data = []


class Stack:
    """
    Basic implementation of a stack using a deque data structure.
    """
    def __init__(self, maxsize=5):
        self.stack = collections.deque()  # DON'T CHANGE THIS FROM A Double-Ended Queue (DEQUE).
        self.maxsize = maxsize

    def __str__(self):
        # Used when you print(my_stack)
        return f'stack __str__(). Implement me.'

    def __repr__(self):
        # Used when you type my_stack into the shell.
        return f'stack __repr__(). Implement me.'

    @property
    def size(self):
        # Return the size of the stack.
        # NOTE: The @property decorator lets you use self.size instead of self.size()
        return 0  # IMPLEMENT THIS.

    @property
    def is_empty(self):
        # Return whether or not the stack is empty.
        # NOTE: The @property decorator lets you use self.is_empty instead of self.is_empty()
        # Hint: Use self.size from above.
        return False  # IMPLEMENT THIS.

    @property
    def is_full(self):
        # Return whether or not the stack is full.
        # NOTE: The @property decorator lets you use self.is_full instead of self.is_full()
        # Hint: Use self.size from above.
        return False  # IMPLEMENT THIS.

    def push(self, item):
        # Push an item onto the stack. Raise a StackIsFullException if the stack exceeds maxsize.
        # NOTE: Use self.is_full() which you implemented earlier.
        print('stack push(). Implement me.')

    def peek(self):
        # Return the current item on top of the stack, but don't pop it.
        # Return None if the stack is empty.
        # Hint: How do you access the last item in a list?
        print('stack peek(). Implement me.')
        return 'Implement Me'

    def pop(self):
        # Pop an item off the stack. Raise a StackIsEmptyException if the stack is empty.
        # NOTE: Use self.is_empty() which you implemented earlier.
        print('stack pop(). Implement me.')
        return 'Implement Me'


class Queue:
    """
    Basic implementation of a queue using a deque data structure.
    """
    def __init__(self, maxsize=5):
        self.queue = collections.deque()  # DON'T CHANGE THIS FROM A Double-Ended Queue (DEQUE).
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


class Tuple:
    """
    A tuple is an immutable data structure which only supports simple operations.
    """
    def __init__(self, initial_data = []):
        # NOTE: Don't change this from a list.
        self.data = initial_data

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


class Dictionary:
    """
    Basic silly implementation of a dictionary/hashtable.
    This is more to demonstrate how the interface of a dictionary behaves.
    """
    def __init__(self, initial_data = {}):
        self.data = initial_data

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
        # NOTE: This has different behaviour from __getitem__, which raises an Exception
        # if the key doesn't exist.
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


class Set:
    """
    Basic implementation of a set.
    Set must NOT contain duplicates.
    NOTE: You're not allowed to use Python's built-in set() for this. Sorry!
    Hint: Use 'in' and 'not in' a lot.
    """
    def __init__(self, initial_data=[]):
        # NOTE: I've done this for you to show how it's done.
        # self.data MUST remain a list throughout.
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
        # Remove an element from a set. Raise a SetException if the item does not exist.
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
        # IMPLEMENT THIS.
        return Set()  # You'll need to change this line too.


class PriorityQueue:
    """
    Basic implementation of a priority queue using a deque data structure.
    """
    def __init__(self):
        self.queue = []

    def __str__(self):
        # Used when you print(my_priorityqueue)
        return f'priorityqueue __str__(). Implement me.'

    def __repr__(self):
        # Used when you type my_priorityqueue into the shell.
        return f'priorityqueue __repr__(). Implement me.'

    @property
    def size(self):
        # Return the size of the queue.
        # NOTE: The @property decorator lets you use self.size instead of self.size()
        return 'Implement Me'

    @property
    def is_empty(self):
        # Return whether or not the queue is empty.
        # Hint: Use self.size from earlier.
        # NOTE: The @property decorator lets you use self.is_empty instead of self.is_empty()
        return 'Implement Me'

    @property
    def is_full(self):
        # Return whether or not the queue is full.
        # NOTE: The @property decorator lets you use self.is_full instead of self.is_full()
        return 'Implement Me'

    def put(self, item, priority='normal'):
        # Add a tuple with (item, priority) to the start of the queue.
        print('priorityqueue put(). Implement me.')


    def front(self):
        # Return the highest priority item but DO NOT modify the queue.
        print('priorityqueue find_max(). Implement me.')
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

