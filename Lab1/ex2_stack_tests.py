"""
DO NOT MODIFY THIS FILE.

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

import random
import pytest
from pyexpect import expect
from ex2_stack import *


"""
Set fixtures

These get recreated every time a test is run.
"""
@pytest.fixture
def empty_stack():
    return Stack()


@pytest.fixture
def large_stack():
    return Stack(maxsize=50)


@pytest.fixture
def random_size_stack():
    # Choose a random stack size
    stack_size = random.randint(5, 30)

    # Create the stack
    random_stack = Stack(maxsize=50)

    # Bypass Stack.push() and pretend we've already added data to the stack.
    random_stack.stack = [random.randint(1, 10) for i in range(stack_size)]

    return random_stack


@pytest.fixture
def my_stack():
    # Create a stack.
    stack_with_data = Stack(maxsize=50)

    # Bypass Stack.push() and pretend we've already added data to the stack.
    stack_with_data.stack = [random.randint(1, 10) for i in range(10)]

    return stack_with_data


@pytest.fixture
def full_stack():
    # Create a stack with maxsize 0.
    return Stack(maxsize=0)


"""
Test __str__
"""
def test_str_method_on_empty_stack(empty_stack):
    # Test __str__ method on empty stack.
    expect(str(empty_stack)) == f'<Stack __str__: {empty_stack.stack}>'


def test_str_method_on_stack_with_data(my_stack):
    # Test __str__ method on a stack with data.
    expect(str(my_stack)) == f'<Stack __str__: {my_stack.stack}>'


"""
Test __repr__
"""
def test_repr_method_on_empty_stack(empty_stack):
    # Test __repr__ method on empty stack.
    expect(repr(empty_stack)) == f'<Stack __repr__: {empty_stack.stack}>'


def test_repr_method_on_stack_with_data(my_stack):
    # Test __repr__ method on regular stack.
    expect(repr(my_stack)) == f'<Stack __repr__: {my_stack.stack}>'


"""
Test size
"""
def test_size_method_on_empty_stack(empty_stack):
    # Test size on empty stack.
    expect(empty_stack.size) == 0


def test_size_method_on_stack_with_data(random_size_stack):
    # Test size on regular stack.
    expect(random_size_stack.size) == len(random_size_stack.stack)


"""
Test is_empty
"""
def test_is_empty_method_on_empty_stack(empty_stack):
    # Test is_empty on empty stack.
    expect(empty_stack.is_empty) == True


def test_is_empty_method_on_stack_with_data(my_stack):
    # Test is_empty method on stack with data.
    expect(my_stack.is_empty) == False


"""
Test is_full
"""
def test_is_full_property_on_empty_stack(empty_stack):
    # Test is_empty on empty stack.
    expect(empty_stack.is_full) == False


def test_is_full_property_full_stack(full_stack):
    # Test is_full on full stack.
    expect(full_stack.is_full) == True


"""
Test push
"""
def test_push_method_increases_size(empty_stack):
    # Push an item
    empty_stack.push(random.randint(1, 10))

    # Check the stack size has increased.
    expect(empty_stack.size) == 1


def test_push_method_adds_item_to_existing_stack(my_stack):
    # Create an item.
    random_item = random.randint(50, 100)

    # Get the current stack size.
    stack_size = len(my_stack.stack)

    # Push the item.
    my_stack.push(random_item)

    # Check the size has increased.
    expect(my_stack.size) == stack_size + 1

    # Check the item is on top of the stack.
    expect(my_stack.stack[-1]) == random_item


def test_push_method_on_full_stack_raises_stackisfullexception(full_stack):
    # Pushing an item to a full stack should raise a StackIsFullException.
    with pytest.raises(StackIsFullException):
        full_stack.push(1)


"""
Test peek
"""
def test_peek_method_on_empty_stack_returns_none(empty_stack):
    # Test the peek method on an empty stack returns None.
    expect(empty_stack.peek()) == None


def test_peek_method_on_stack_with_data_returns_correct_data(my_stack):
    # Create a random item.
    random_item = random.randint(50, 100)

    # Push the item to the stack.
    my_stack.push(random_item)

    # Check that peek() returns random_item from the top of the stack.
    expect(my_stack.peek()) == random_item


"""
Test pop
"""
def test_pop_method_on_empty_stack_raises_stackisemptyexception(empty_stack):
    # Test pop method on empty stack raises StackIsEmptyException.
    with pytest.raises(StackIsEmptyException):
        empty_stack.pop()


def test_pop_method_on_stack_with_data_returns_correct_item_and_removes_it_from_stack(my_stack):
    # Create a random item.
    random_item = random.randint(50, 100)

    # Push the item to the stack.
    my_stack.push(random_item)

    # Check that pop() returns random_item from the top of the stack.
    expect(my_stack.pop()) == random_item

    # Check that the item has been removed from the stack.
    expect(my_stack.peek()) != random_item

