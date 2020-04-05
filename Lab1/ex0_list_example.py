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


# Sample Implementation of a List data structure.
class List:
    """
    Basic List Data Structure
    """
    def __init__(self, initial_data=None):
        if initial_data:
            self.data = initial_data
        else:
            self.data = []

    def __str__(self):
        # Used when you print(my_list)
        return f'<List __str__: {self.data}>'

    def __repr__(self):
        # Used when you type my_list into the shell.
        return f'<List __repr__: {self.data}>'

    @property  # @property lets you use my_list.size instead of my_list.size()
    def size(self):
        return len(self.data)

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

    def append(self, item):
        # Adds an item to the end of the list.
        self.data.append(item)

    def pop(self):
        # Remove and return an item from the end of the list.
        if self.size == 0:
            raise ListIsEmptyException('Tried to pop() from empty list.')
        else:
            return self.data.pop()

    def insert(self, index, item):
        # Insert an item at index
        self.data.insert(index, item)

    def clear(self):
        self.data = []


