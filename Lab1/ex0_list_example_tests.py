"""
ISCG 6426 - Data Structures & Algorithms
Semester 1 2020
Kris Pritchard - @krisrp

This code tests the example List class implementation for Lab1.
"""


import random
import pytest
from pyexpect import expect
from ex0_list_example import *


def test_str_method_on_empty_list():
    # Create an empty list.
    my_list = List()

    # Test __str__ method on empty list returns <List __str__: []>
    expect(str(my_list)) == f'<List __str__: []>'


def test_str_method_on_list_with_data():
    # Create an empty list.
    my_list = List()

    # Bypass List.append() and pretend we've already added data to the list.
    my_list.data = [random.randint(1, 10) for i in range(10)]

    # Test __str__ method on empty list returns <List __str__: []>
    expect(str(my_list)) == f'<List __str__: {my_list.data}>'


def test_repr_method_on_empty_list():
    # Create an empty list.
    my_list = List()

    # Test __repr__ method on empty list returns <List __repr__: []>
    expect(repr(my_list)) == f'<List __repr__: []>'


def test_repr_method_on_list_with_data():
    # Create an empty list.
    my_list = List()

    # Bypass List.append() and pretend we've already added data to the list.
    my_list.data = [random.randint(1, 10) for i in range(10)]

    # Test __repr__ method on empty list returns <List __repr__: []>
    expect(repr(my_list)) == f'<List __repr__: {my_list.data}>'


def test_size_on_empty_list():
    # Create an empty list.
    empty_list = List()

    # Test the size property
    expect(empty_list.size) == 0


def test_size_on_list_with_data():
    # Create an empty list.
    my_list = List()

    # Choose a random size.
    random_size = random.randint(50, 100)

    # Bypass List.append() and pretend we've already added data to the list.
    my_list.data = [random.randint(1, 10) for i in range(random_size)]

    # Test the size property
    expect(my_list.size) == random_size


def test_getitem_on_empty_list_raises_listindexexception():
    # Create an empty list.
    my_list = List()

    # Test that a ListIndexException is raised when accessing an empty list.
    with pytest.raises(ListIndexException):
        my_list[100]


def test_getitem_using_subscript_on_list():
    # Create an empty list.
    my_list = List()

    # Bypass List.append() and pretend we've already added data to the list.
    my_list.data = [1, 2, 3, 4]

    # Test that my_list[0] works.
    expect(my_list[0]) == 1

    # Test that my_list[-1] works.
    expect(my_list[-1]) == 4


def test_setitem_using_subscript_on_empty_list():
    # Create an empty list.
    my_list = List()

    # Test that my_list[0] = 123 on empty list raises ListIndexException
    with pytest.raises(ListIndexException):
        my_list[0]


def test_setitem_using_subscript_on_list_with_data():
    # Create an empty list.
    my_list = List()

    # Bypass List.append() and pretend we've already added data to the list.
    my_list.data = [1, 2, 3, 4]

    # Test that my_list[0] = 123 works.
    my_list[0] = 123
    expect(my_list[0]) == 123


def test_add_operator_overloading_on_two_lists():
    # Create empty lists.
    my_list = List()
    other_list = List()

    # Bypass List.append() and pretend we've already added data to the lists.
    my_list.data = [1, 2, 3, 4]
    other_list.data = [10, 9, 8, 7]

    # Test __add__ method aka list1 + list2.
    new_list = my_list + other_list
    expect(new_list.data) == [1, 2, 3, 4, 10, 9, 8, 7]


def test_append_method_on_list():
    # Create an empty list.
    my_list = List()

    # Check the list size.
    expect(len(my_list.data)) == 0

    # Check the list data is empty.
    expect(my_list.data) == []

    # Test the append method.
    my_list.append(1)
    my_list.append(2)
    my_list.append(3)

    # Check the list size again.
    expect(len(my_list.data)) == 3

    # Check the list data again.
    expect(my_list.data) == [1, 2, 3]


def test_pop_method_on_empty_list_raises_listisemptyexception():
    # Create an empty list.
    my_list = List()

    # Test that my_list.pop() on empty list raises ListIndexException
    with pytest.raises(ListIsEmptyException):
        my_list.pop()


def test_pop_method_on_list_with_data():
    # Create an empty list.
    my_list = List()

    # Bypass List.append() and pretend we've already added data to the lists.
    my_list.data = [1, 2, 3, 4]

    # Test pop method.
    expect(my_list.pop()) == 4
    expect(my_list.pop()) == 3
    expect(my_list.pop()) == 2


def test_insert_method_on_list():
    # Create an empty list.
    my_list = List()

    # Bypass List.append() and pretend we've already added data to the lists.
    my_list.data = [1, 2, 3, 4]

    # Test insert method by inserting 100 at index 1.
    my_list.insert(1, 100)
    expect(my_list[1]) == 100


def test_clear_method_on_list():
    # Create an empty list.
    my_list = List()

    # Bypass List.append() and pretend we've already added data to the list.
    my_list.data = [1, 2, 3, 4]

    # Test clear method.
    my_list.clear()
    expect(my_list.data) == []

