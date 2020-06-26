"""
DO NOT MODIFY THIS FILE.

ISCG6426 Lab 1 Semester 1 2020 by Kris Pritchard / @krisrp

Tests used to check correctness of Lab3 answers.
This file requires 'pytest' and 'pyexpect' to run.
Install them with the following command:
    pip install pytest pyexpect

Then run the file with:
    pytest -xv heap_priority_queue_tests.py

You need to implement this code so that all of the tests pass.
Feel free to comment out specific tests, but only submit your answers files.
When checking your answers I will use the test files from this repository.

"""
import pytest
import random
from pyexpect import expect
from heap_priority_queue import *


@pytest.fixture
def empty_priority_queue():
    return PriorityQueue()


@pytest.fixture
def full_priority_queue():
    return PriorityQueue(maxsize=0)


@pytest.fixture
def priority_queue_with_number_data():
    ordered_numbers = [i for i in range(10)]
    shuffled_numbers = ordered_numbers.copy()
    random.shuffle(shuffled_numbers)
    priority_queue = PriorityQueue()
    priority_queue._ordered_numbers = ordered_numbers
    priority_queue._shuffled_numbers = shuffled_numbers
    heapq.heapify(shuffled_numbers)
    priority_queue.queue = shuffled_numbers
    priority_queue.maxsize = 15
    return priority_queue

@pytest.fixture
def priority_queue_with_name_data():
    ordered_names = [
        'Ankit',
        'Avantika',
        'Jack',
        'Joswin',
        'Kam Ho',
        'Kris',
        'Mohamed',
        'Nour',
        'Onisha',
        'Reuben',
        'Robinson',
        'Yalikun',
        'Yolanda',
    ]
    shuffled_names = ordered_names.copy()
    random.shuffle(shuffled_names)

    priority_queue = PriorityQueue()
    priority_queue._ordered_names = ordered_names
    priority_queue._shuffled_names = shuffled_names
    heapq.heapify(shuffled_names)
    priority_queue.queue = shuffled_names
    priority_queue.maxsize = 15
    return priority_queue


"""
Test __init__
"""

def test_init_method_binds_queue_instance_variable():
    pq = PriorityQueue([1, 2, 3])
    expect(hasattr(pq, 'queue')) == True

def test_init_method_binds_maxsize_instance_variable():
    pq = PriorityQueue([1, 2, 3], maxsize=5)
    expect(hasattr(pq, 'maxsize')) == True

def test_init_method_with_no_initial_queue(empty_priority_queue):
    expect(empty_priority_queue.queue) == []

def test_init_method_with_initial_queue_data():
    pq = PriorityQueue([1, 2, 3])
    expect(pq.queue) == [1, 2, 3]

"""
Test __str__
"""
def test_str_method_on_empty_priority_queue(empty_priority_queue):
    expect(str(empty_priority_queue)) == f'<PriorityQueue __str__: {empty_priority_queue.queue}>'


def test_str_method_on_full_priority_queue(full_priority_queue):
    expect(str(full_priority_queue)) == f'<PriorityQueue __str__: {full_priority_queue.queue}>'


def test_str_method_on_priority_queue_with_number_data(priority_queue_with_number_data):
    expect(str(priority_queue_with_number_data)) == f'<PriorityQueue __str__: {priority_queue_with_number_data.queue}>'


def test_str_method_on_priority_queue_with_name_data(priority_queue_with_name_data):
    expect(str(priority_queue_with_name_data)) == f'<PriorityQueue __str__: {priority_queue_with_name_data.queue}>'
"""
Test __repr__
"""

def test_repr_method_on_empty_priority_queue(empty_priority_queue):
    expect(repr(empty_priority_queue)) == f'<PriorityQueue __repr__: {empty_priority_queue.queue}>'


def test_repr_method_on_full_priority_queue(full_priority_queue):
    expect(repr(full_priority_queue)) == f'<PriorityQueue __repr__: {full_priority_queue.queue}>'


def test_repr_method_on_priority_queue_with_number_data(priority_queue_with_number_data):
    expect(repr(priority_queue_with_number_data)) == f'<PriorityQueue __repr__: {priority_queue_with_number_data.queue}>'


def test_repr_method_on_priority_queue_with_name_data(priority_queue_with_name_data):
    expect(repr(priority_queue_with_name_data)) == f'<PriorityQueue __repr__: {priority_queue_with_name_data.queue}>'
"""
Test size
"""
def test_size_on_empty_priority_queue(empty_priority_queue):
    expect(empty_priority_queue.size) == 0


def test_size_on_priority_queue_with_number_data(priority_queue_with_number_data):
    expect(priority_queue_with_number_data.size) == 10

def test_size_on_priority_queue_with_name_data(priority_queue_with_name_data):
    expect(priority_queue_with_name_data.size) == 13

"""
Test is_empty
"""
def test_is_empty_on_empty_priority_queue(empty_priority_queue):
    expect(empty_priority_queue.is_empty()) == True


def test_is_empty_on_priority_queue_with_number_data(priority_queue_with_number_data):
    expect(priority_queue_with_number_data.is_empty()) == False

def test_is_empty_on_priority_queue_with_name_data(priority_queue_with_name_data):
    expect(priority_queue_with_name_data.is_empty()) == False

"""
Test is_full
"""
def test_is_full_on_empty_priority_queue(empty_priority_queue):
    expect(empty_priority_queue.is_full()) == False


def test_is_full_on_priority_queue_with_number_data(priority_queue_with_number_data):
    expect(priority_queue_with_number_data.is_full()) == False

def test_is_full_on_priority_queue_with_name_data(priority_queue_with_name_data):
    expect(priority_queue_with_name_data.is_full()) == False

def test_is_full_on_full_priority_queue(full_priority_queue):
    expect(full_priority_queue.is_full()) == True

"""
Test push
"""
def test_push_on_priority_queue_with_number_data(priority_queue_with_number_data):
    expect(priority_queue_with_number_data.size) == 10
    priority_queue_with_number_data.push(50)
    expect(priority_queue_with_number_data.size) == 11

def test_push_on_priority_queue_with_name_data(priority_queue_with_name_data):
    expect(priority_queue_with_name_data.size) == 13
    priority_queue_with_name_data.push('Python')
    expect(priority_queue_with_name_data.size) == 14

def test_push_on_full_queue_raises_queueisfullexception(full_priority_queue):
    with pytest.raises(QueueIsFullException):
        full_priority_queue.push('Zorro')



"""
Test peek
"""
def test_peek_on_empty_priority_queue_returns_none(empty_priority_queue):
    expect(empty_priority_queue.peek()) == None


def test_peek_returns_value_of_highest_priority_item(priority_queue_with_number_data):
    expect(priority_queue_with_number_data.peek()) == priority_queue_with_number_data._ordered_numbers[0]

def test_peek_returns_value_of_highest_priority_item(priority_queue_with_name_data):
    expect(priority_queue_with_name_data.peek()) == priority_queue_with_name_data._ordered_names[0]

"""
Test pop
"""
def test_pop_on_queue_with_number_data_removes_items(priority_queue_with_number_data):
    pq_length = len(priority_queue_with_number_data._ordered_numbers)
    pq_data = priority_queue_with_number_data._ordered_numbers
    expect(priority_queue_with_number_data.size) == pq_length
    priority_queue_with_number_data.push(random.randint(100, 200))

    expect(priority_queue_with_number_data.size) == pq_length + 1
    expect(priority_queue_with_number_data.pop()) == pq_data[0]
    expect(priority_queue_with_number_data.size) == pq_length
    expect(priority_queue_with_number_data.pop()) == pq_data[1]
    expect(priority_queue_with_number_data.size) == pq_length - 1
    expect(priority_queue_with_number_data.pop()) == pq_data[2]
    expect(priority_queue_with_number_data.size) == pq_length - 2
    expect(priority_queue_with_number_data.pop()) == pq_data[3]
    expect(priority_queue_with_number_data.size) == pq_length -3


def test_pop_on_queue_with_name_data_removes_items(priority_queue_with_name_data):
    pq_length = len(priority_queue_with_name_data._ordered_names)
    pq_data = priority_queue_with_name_data._ordered_names
    expect(priority_queue_with_name_data.size) == pq_length
    high_priority_name = 'Aardvark'
    low_priority_name = 'Xavier'

    priority_queue_with_name_data.push(low_priority_name)
    expect(priority_queue_with_name_data.size) == pq_length + 1

    priority_queue_with_name_data.push(high_priority_name)
    expect(priority_queue_with_name_data.size) == pq_length + 2

    expect(priority_queue_with_name_data.pop()) == high_priority_name
    expect(priority_queue_with_name_data.size) == pq_length + 1

    expect(priority_queue_with_name_data.pop()) == pq_data[0]
    expect(priority_queue_with_name_data.size) == pq_length

    expect(priority_queue_with_name_data.pop()) == pq_data[1]
    expect(priority_queue_with_name_data.size) == pq_length - 1

    expect(priority_queue_with_name_data.pop()) == pq_data[2]
    expect(priority_queue_with_name_data.size) == pq_length - 2

    expect(priority_queue_with_name_data.pop()) == pq_data[3]
    expect(priority_queue_with_name_data.size) == pq_length - 3

def test_pop_on_empty_priority_queue_raises_queueisemptyexception(empty_priority_queue):
    with pytest.raises(QueueIsEmptyException):
        empty_priority_queue.pop
