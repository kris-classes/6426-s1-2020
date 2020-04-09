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

Set (No Duplicates / Unique Items Only / Mathematical Set):
    For this introductory lab you need to implement functionality for a basic set data structure.
    Performance doesn't matter for this.
    None of the method implementations require more than 7 lines of code.
"""
import pytest
from pyexpect import expect
from ex7_priorityqueue import *


@pytest.fixture
def empty_priority_queue():
    return PriorityQueue()


@pytest.fixture
def full_priority_queue():
    return PriorityQueue(maxsize=0)


@pytest.fixture
def priority_queue_with_data():
    priority_queue = PriorityQueue()
    priority_queue.put('Bob', 'normal')
    priority_queue.put('Alice', 'high')
    priority_queue.put('Eve')  # Default to 'normal'
    return priority_queue


"""
Test __str__
"""
def test_str_method_on_empty_priority_queue(empty_priority_queue):
    expect(str(empty_priority_queue)) == f'<PriorityQueue __str__: {empty_priority_queue.queue}>'


def test_str_method_on_full_priority_queue(full_priority_queue):
    expect(str(full_priority_queue)) == f'<PriorityQueue __str__: {full_priority_queue.queue}>'


def test_str_method_on_priority_queue_with_data(priority_queue_with_data):
    expect(str(priority_queue_with_data)) == f'<PriorityQueue __str__: {priority_queue_with_data.queue}>'


"""
Test __repr__
"""

def test_repr_method_on_empty_priority_queue(empty_priority_queue):
    expect(repr(empty_priority_queue)) == f'<PriorityQueue __repr__: {empty_priority_queue.queue}>'


def test_repr_method_on_full_priority_queue(full_priority_queue):
    expect(repr(full_priority_queue)) == f'<PriorityQueue __repr__: {full_priority_queue.queue}>'


def test_repr_method_on_priority_queue_with_data(priority_queue_with_data):
    expect(repr(priority_queue_with_data)) == f'<PriorityQueue __repr__: {priority_queue_with_data.queue}>'


"""
Test size
"""
def test_size_on_empty_priority_queue(empty_priority_queue):
    expect(empty_priority_queue.size) == 0


def test_size_on_priority_queue_with_data(priority_queue_with_data):
    expect(priority_queue_with_data.size) == 3


"""
Test is_empty
"""
def test_is_empty_on_empty_priority_queue(empty_priority_queue):
    expect(empty_priority_queue.is_empty) == True


def test_is_empty_on_priority_queue_with_data(priority_queue_with_data):
    expect(priority_queue_with_data.is_empty) == False


"""
Test is_full
"""
def test_is_full_on_empty_priority_queue(empty_priority_queue):
    expect(empty_priority_queue.is_full) == False


def test_is_full_on_priority_queue_with_data(priority_queue_with_data):
    expect(priority_queue_with_data.is_full) == False


def test_is_full_on_full_priority_queue(full_priority_queue):
    expect(full_priority_queue.is_full) == True

"""
Test put
"""
def test_put_on_priority_queue_with_data(priority_queue_with_data):
    expect(priority_queue_with_data.size) == 3
    priority_queue_with_data.put('Mallory', 'high')
    expect(priority_queue_with_data.size) == 4


def test_put_on_full_queue_raises_queueisfullexception(full_priority_queue):
    with pytest.raises(QueueIsFullException):
        full_priority_queue.put('Test', 'medium')


"""
Test front
"""
def test_front_on_empty_priority_queue_returns_none(empty_priority_queue):
    expect(empty_priority_queue.front()) == None


def test_front_returns_index_of_highest_priority_item(priority_queue_with_data):
    expect(priority_queue_with_data.front()) == 1


"""
Test peek
"""
def test_peek_on_empty_priority_queue_returns_none(empty_priority_queue):
    expect(empty_priority_queue.peek()) == None


def test_peek_returns_value_of_highest_priority_item(priority_queue_with_data):
    expect(priority_queue_with_data.peek()) == 'Alice'


"""
Test get
"""
def test_get_on_queue_with_data_removes_items(priority_queue_with_data):
    expect(priority_queue_with_data.size) == 3
    priority_queue_with_data.put('Mallory', 'high')

    expect(priority_queue_with_data.size) == 4
    expect(priority_queue_with_data.get()) == 'Alice'
    expect(priority_queue_with_data.size) == 3
    expect(priority_queue_with_data.get()) == 'Mallory'
    expect(priority_queue_with_data.size) == 2
    expect(priority_queue_with_data.get()) == 'Bob'
    expect(priority_queue_with_data.size) == 1
    expect(priority_queue_with_data.get()) == 'Eve'
    expect(priority_queue_with_data.size) == 0


def test_get_on_empty_priority_queue_raises_queueisemptyexception(empty_priority_queue):
    with pytest.raises(QueueIsEmptyException):
        empty_priority_queue.get()

