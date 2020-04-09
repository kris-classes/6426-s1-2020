"""
DO NOT MODIFY THIS FILE.

ISCG6426 Lab 1 Semester 1 2020 by Kris Pritchard / @krisrp

Tests used to check correctness of Lab1 answers.
This file requires 'pytest' and 'pyexpect' to run.
Install them with the following command:
    pip install pytest pyexpect

Then run the file with:
    pytest -xv ex3_queue_tests.py

You need to implement this code so that all of the tests pass.
Feel free to comment out specific tests, but only submit your answers files.
When checking your answers I will use the test files from this repository.


Queue (FIFO):
    For this introductory lab you need to implement functionality for a basic queue data structure.
    Performance doesn't matter for this.
    None of the method implementations require more than 4 lines of code.
"""

import collections
import pytest
import random
from pyexpect import expect
from ex3_queue import *


@pytest.fixture
def empty_queue():
    return Queue()


@pytest.fixture
def full_queue():
    return Queue(maxsize=0)


@pytest.fixture
def small_queue():
    queue = Queue()
    queue.queue = collections.deque([1, 2, 3])
    return queue


@pytest.fixture
def random_queue():
    queue_size = random.randint(5, 30)
    my_queue = Queue(maxsize=50)
    my_queue.queue = collections.deque([random.randint(1, 10) for i in range(queue_size)])
    return my_queue


def test_str_method_on_empty_queue(empty_queue):
    expect(str(empty_queue)) == f'<Queue __str__: {empty_queue.queue}>'


def test_str_method_on_small_queue(small_queue):
    expect(str(small_queue)) == f'<Queue __str__: {small_queue.queue}>'


def test_str_method_on_random_queue(random_queue):
    expect(str(random_queue)) == f'<Queue __str__: {random_queue.queue}>'


def test_repr_method_on_empty_queue(empty_queue):
    expect(repr(empty_queue)) == f'<Queue __repr__: {empty_queue.queue}>'


def test_repr_method_on_small_queue(small_queue):
    expect(repr(small_queue)) == f'<Queue __repr__: {small_queue.queue}>'


def test_repr_method_on_random_queue(random_queue):
    expect(repr(random_queue)) == f'<Queue __repr__: {random_queue.queue}>'


def test_size_on_empty_queue(empty_queue):
    expect(empty_queue.size) == 0


def test_is_empty_on_empty_queue(empty_queue):
    expect(empty_queue.is_empty) == True


def test_is_full_on_empty_queue(empty_queue):
    expect(empty_queue.is_full) == False


def test_is_full_on_full_queue(full_queue):
    expect(full_queue.is_full) == True


def test_put_method_on_empty_queue(empty_queue):
    expect(len(empty_queue.queue)) == 0
    empty_queue.put(1)
    empty_queue.put(2)
    empty_queue.put(3)
    expect(len(empty_queue.queue)) == 3


def test_put_method_on_full_queue_raises_queueisfullexception(full_queue):
    with pytest.raises(QueueIsFullException):
        full_queue.put(123)


def test_size_on_small_queue(small_queue):
    expect(small_queue.size) == len(small_queue.queue)


def test_size_on_random_queue(random_queue):
    expect(random_queue.size) == len(random_queue.queue)


def test_peek_on_empty_queue_returns_none(empty_queue):
    expect(empty_queue.peek()) == None


def test_peek_on_small_queue(small_queue):
    expect(small_queue.peek()) == small_queue.queue[0]


def test_peek_on_random_queue(random_queue):
    expect(random_queue.peek()) == random_queue.queue[0]


def test_get_on_empty_queue_raises_queueisemptyexception(empty_queue):
    with pytest.raises(QueueIsEmptyException):
        empty_queue.get()


def test_get_on_small_queue_gets_first_item(small_queue):
    expect(small_queue.get()) == 1


def test_get_on_random_queue_gets_first_item(random_queue):
    queue_item = random_queue.queue[0]
    expect(random_queue.get()) == queue_item

