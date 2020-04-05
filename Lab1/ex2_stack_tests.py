import random
import pytest
from pyexpect import expect
from ex2_stack import *
#from ex2_stack_answers import *


def test_str_method_on_empty_stack():
    # Create an empty stack.
    empty_stack = Stack()

    # Test __str__ method on empty stack.
    expect(str(empty_stack)) == f'<Stack __str__: {empty_stack.stack}>'


def test_str_method_on_stack_with_data():
    # Create a stack.
    my_stack = Stack(maxsize=50)

    # Bypass Stack.push() and pretend we've already added data to the stack.
    my_stack.stack = [random.randint(1, 10) for i in range(10)]

    # Test __str__ method on a stack with data.
    expect(str(my_stack)) == f'<Stack __str__: {my_stack.stack}>'


def test_repr_method_on_empty_stack():
    # Create an empty stack.
    empty_stack = Stack()

    # Test __repr__ method on empty stack.
    expect(repr(empty_stack)) == f'<Stack __repr__: {empty_stack.stack}>'


def test_repr_method_on_stack_with_data():
    # Create a stack.
    my_stack = Stack(maxsize=50)

    # Bypass Stack.push() and pretend we've already added data to the stack.
    my_stack.stack = [random.randint(1, 10) for i in range(10)]

    # Test __repr__ method on regular stack.
    expect(repr(my_stack)) == f'<Stack __repr__: {my_stack.stack}>'


def test_size_method_on_empty_stack():
    # Create an empty stack.
    empty_stack = Stack()

    # Test size on empty stack.
    expect(empty_stack.size) == 0


def test_size_method_on_stack_with_data():
    # Choose a random size.
    stack_size = random.randint(5, 30)

    # Create a stack.
    my_stack = Stack(maxsize=50)

    # Bypass Stack.push() and pretend we've already added data to the stack.
    my_stack.stack = [random.randint(1, 10) for i in range(stack_size)]

    # Test size on regular stack.
    expect(my_stack.size) == stack_size


def test_is_empty_method_on_empty_stack():
    # Create an empty stack.
    empty_stack = Stack()

    # Test is_empty on empty stack.
    expect(empty_stack.is_empty) == True


def test_is_empty_method_on_stack_with_data():
    # Create a stack.
    my_stack = Stack()

    # Bypass Stack.push() and pretend we've already added data to the stack.
    my_stack.stack = [random.randint(1, 10) for i in range(4)]

    # Test is_empty method on stack with data.
    expect(my_stack.is_empty) == False


def test_is_full_property_on_empty_stack():
    # Create an empty stack.
    empty_stack = Stack()

    # Test is_empty on empty stack.
    expect(empty_stack.is_full) == False


def test_is_full_property_full_stack():
    # Create a full stack.
    full_stack = Stack(maxsize=0)

    # Test is_full on full stack.
    expect(full_stack.is_full) == True


def test_is_empty_and_is_full_properties_on_stack_that_is_neither_full_or_empty():
    # Create a stack.
    my_stack = Stack(maxsize=5)

    # Bypass Stack.push() and pretend we've already added data to the stack.
    my_stack.stack = [random.randint(1, 10) for i in range(3)]

    # Test is_empty property.
    expect(my_stack.is_empty) == False

    # Test is_full property.
    expect(my_stack.is_full) == False


def test_push_method_increases_size():
    # Create an empty stack.
    my_stack = Stack()

    # Check stack size.
    expect(my_stack.size) == 0

    # Push an item
    my_stack.push(random.randint(1, 10))

    # Check the stack size has increased.
    expect(my_stack.size) == 1


def test_push_method_adds_item_to_existing_stack():
    # Choose a random size.
    stack_size = random.randint(25, 40)

    # Create an empty stack.
    my_stack = Stack(maxsize=50)

    # Bypass Stack.push() and pretend we've already added data to the stack.
    my_stack.stack = [random.randint(1, 10) for i in range(stack_size)]

    # Create an item.
    random_item = random.randint(50, 100)

    # Push the item.
    my_stack.push(random_item)

    # Check the size has increased.
    expect(my_stack.size) == stack_size + 1

    # Check the item is on top of the stack.
    expect(my_stack.stack[-1]) == random_item


def test_push_method_on_full_stack_raises_stackisfullexception():
    # Create a full stack.
    full_stack = Stack(maxsize=0)

    # Pushing an item to a full stack should raise a StackIsFullException.
    with pytest.raises(StackIsFullException):
        full_stack.push(1)


def test_peek_method_on_empty_stack_returns_none():
    # Create an empty stack.
    empty_stack = Stack()

    # Test the peek method on an empty stack returns None.
    expect(empty_stack.peek()) == None


def test_peek_method_on_stack_with_data_returns_correct_data():
    # Choose a random size.
    stack_size = random.randint(25, 40)

    # Create an empty stack.
    my_stack = Stack(maxsize=50)

    # Bypass Stack.push() and pretend we've already added data to the stack.
    my_stack.stack = [random.randint(1, 10) for i in range(stack_size)]

    # Create a random item.
    random_item = random.randint(50, 100)

    # Push the item to the stack.
    my_stack.push(random_item)

    # Check that peek() returns random_item from the top of the stack.
    expect(my_stack.peek()) == random_item


def test_pop_method_on_empty_stack_raises_stackisemptyexception():
    # Create an empty stack.
    empty_stack = Stack()

    # Test pop method on empty stack raises StackIsEmptyException.
    with pytest.raises(StackIsEmptyException):
        empty_stack.pop()


def test_pop_method_on_stack_with_data_returns_correct_item_and_removes_it_from_stack():
    # Choose a random size.
    stack_size = random.randint(25, 40)

    # Create an empty stack.
    my_stack = Stack(maxsize=50)

    # Bypass Stack.push() and pretend we've already added data to the stack.
    my_stack.stack = [random.randint(1, 10) for i in range(stack_size)]

    # Create a random item.
    random_item = random.randint(50, 100)

    # Push the item to the stack.
    my_stack.push(random_item)

    # Check that pop() returns random_item from the top of the stack.
    expect(my_stack.pop()) == random_item

    # Check that the item has been removed from the stack.
    expect(my_stack.peek()) != random_item

