"""
ISCG6426 Lab 1 Semester 1 2020. Code by Kris Pritchard / @krisrp

Tests used to check correctness of Lab1 answers.
This file requires 'pytest' and 'pyexpect' to run.
Install it with the following command:
    pip install pytest
    pip install pyexpect

Then run the file with:
    pytest -v Lab1_tests.py

You need to fix the code so that all of these tests pass.
Feel free to comment out specific tests, but only submit the Lab1_answers file.
When checking your answers I will use the full uncommented version of this file.
"""

import random
import unittest
import pytest
from pyexpect import expect
from Lab1 import *  # Don't import * in your job. It's ok for assignments.
#from Lab1_answers import *


def test_list():
    """
    This code tests the List class for Lab1.
    """
    my_list = List([1, 2, 3])
    my_list2 = List([1, 2, 3, 4])
    my_list3 = List([random.randint(0, 10) for i in range(100)])

    # Test __init__ method.
    expect(my_list.data) == [1, 2, 3]

    # Test __str__ method.
    expect(str(my_list)) == '<List __str__: [1, 2, 3]>'
    expect(str(my_list2)) == '<List __str__: [1, 2, 3, 4]>'
    expect(str(my_list3)) == f'<List __str__: {my_list3.data}>'

    # Test __repr__ method.
    expect(repr(my_list)) == '<List __repr__: [1, 2, 3]>'
    expect(repr(my_list2)) == '<List __repr__: [1, 2, 3, 4]>'
    expect(repr(my_list3)) == f'<List __repr__: {my_list3.data}>'

    # Test __getitem__ aka looking up items via subscript or [] syntax.
    expect(my_list[0]) == 1
    expect(my_list2[-1]) == 4
    expect(lambda: my_list[100]).to_raise(exception_class=ListIndexException)

    # Test __setitem__ aka setting items via subscript or [] syntax.
    my_list[0] = 123
    expect(my_list[0]) == 123
    expect(my_list2[-1]) == 4
    expect(lambda: my_list[100]).to_raise(exception_class=ListIndexException)

    # Test __add__ method aka list1 + list2.
    new_list = my_list + my_list2
    expect(new_list.data) == [123, 2, 3, 1, 2, 3, 4]

    # Test append method.
    my_list.append(42)
    expect(my_list[3]) == 42

    # Test pop method.
    expect(my_list.pop) == 42
    expect(my_list.pop) == 3
    expect(my_list.pop) == 2
    expect(my_list.pop) == 123
    expect(lambda: my_list.pop).raises(ListIsEmptyException)

    # Test insert method.
    my_list2.insert(1, 100)
    expect(my_list2[1]) == 100

    # Test clear method.
    my_list3.clear()
    expect(my_list3.data) == []


def test_recursion():
    expect(recursion_example(11)) == 10
    expect(recursion_example(100, stop=95)) == 95


def test_stack():
    my_stack = Stack()
    my_stack.push(1)
    my_stack.push(2)
    my_stack.push(3)
    empty_stack = Stack()
    full_stack = Stack(maxsize=0)

    # Test __str__ method.
    expect(str(my_stack)) == f'<Stack __str__: {my_stack.stack}>'
    expect(str(empty_stack)) == f'<Stack __str__: {empty_stack.stack}>'
    expect(str(full_stack)) == f'<Stack __str__: {full_stack.stack}>'

    # Test __repr__ method.
    expect(repr(my_stack)) == f'<Stack __repr__: {my_stack.stack}>'
    expect(repr(empty_stack)) == f'<Stack __repr__: {empty_stack.stack}>'
    expect(repr(full_stack)) == f'<Stack __repr__: {full_stack.stack}>'

    # Test size on empty stack.
    expect(empty_stack.size) == 0

    # Test is_empty on empty stack.
    expect(empty_stack.is_empty) == True

    # Test is_full on empty stack.
    expect(empty_stack.is_full) == False

    # Test push method.
    expect(len(my_stack.stack)) == 3
    my_stack.push(4)
    expect(len(my_stack.stack)) == 4

    # Test push method on full stack raises StackIsFullException.
    with pytest.raises(StackIsFullException):
        full_stack.push(123)

    # Test size on regular stack.
    expect(my_stack.size) == 4

    # Test peek method on empty stack.
    expect(empty_stack.peek()) == None

    # Test peek method on regular stack.
    expect(my_stack.peek()) == 4

    # Test is_empty method on regular stack.
    expect(my_stack.is_empty) == False

    # Test is_full method on full stack.
    expect(empty_stack.is_full) == False
    expect(my_stack.is_full) == False
    expect(full_stack.is_full) == True

    # Test pop method on regular stack.
    item = my_stack.peek()
    expect(my_stack.pop) == 4

    # Test pop method on empty stack raises StackIsEmptyException.
    with pytest.raises(StackIsEmptyException):
        empty_stack.pop


def test_queue():
    my_queue = Queue()
    my_queue.put(1)
    my_queue.put(2)
    my_queue.put(3)
    empty_queue = Queue()
    full_queue = Queue(maxsize=0)

    # Test __str__ method.
    expect(str(my_queue)) == f'<Queue __str__: {my_queue.queue}>'
    expect(str(empty_queue)) == f'<Queue __str__: {empty_queue.queue}>'
    expect(str(full_queue)) == f'<Queue __str__: {full_queue.queue}>'

    # Test __repr__ method.
    expect(repr(my_queue)) == f'<Queue __repr__: {my_queue.queue}>'
    expect(repr(empty_queue)) == f'<Queue __repr__: {empty_queue.queue}>'
    expect(repr(full_queue)) == f'<Queue __repr__: {full_queue.queue}>'

    # Test size on empty queue.
    expect(empty_queue.size) == 0

    # Test is_empty on empty queue.
    expect(empty_queue.is_empty) == True

    # Test is_full on empty queue.
    expect(empty_queue.is_full) == False

    # Test is_full on full queue.
    expect(full_queue.is_full) == True

    # Test put method.
    expect(len(my_queue.queue)) == 3
    my_queue.put(4)
    expect(len(my_queue.queue)) == 4

    # Test put method on full queue raises QueueIsFullException.
    with pytest.raises(QueueIsFullException):
        full_queue.put(123)

    # Test size on regular queue.
    expect(my_queue.size) == 4

    # Test peek method on empty queue.
    expect(empty_queue.peek()) == None

    # Test peek method on regular queue.
    expect(my_queue.peek()) == 1

    # Test get method on regular queue.
    expect(my_queue.get()) == 1

    # Test get method raises QueueIsEmptyException on empty queue.
    with pytest.raises(QueueIsEmptyException):
        empty_queue.get()


def test_tuple():
    """
    Tests the Tuple class for Lab1.
    """
    my_tuple = Tuple([1, 2, 3])
    my_tuple2 = Tuple([1, 2, 3, 4])
    my_tuple3 = Tuple([random.randint(0, 10) for i in range(100)])

    # Test __init__ method.
    expect(my_tuple.data) == [1, 2, 3]
    expect(isinstance(my_tuple.data, list)) == True

    # Test __str__ method.
    expect(str(my_tuple)) == '<Tuple __str__: [1, 2, 3]>'
    expect(str(my_tuple2)) == '<Tuple __str__: [1, 2, 3, 4]>'
    expect(str(my_tuple3)) == f'<Tuple __str__: {my_tuple3.data}>'

    # Test __repr__ method.
    expect(repr(my_tuple)) == '<Tuple __repr__: [1, 2, 3]>'
    expect(repr(my_tuple2)) == '<Tuple __repr__: [1, 2, 3, 4]>'
    expect(repr(my_tuple3)) == f'<Tuple __repr__: {my_tuple3.data}>'

    # Test __getitem__ aka looking up items via subscript or [] syntax.
    expect(my_tuple[0]) == 1
    expect(my_tuple2[-1]) == 4
    expect(lambda: my_tuple[100]).to_raise(exception_class=TupleIndexException)

    # Test __setitem__ aka setting items via subscript or [] syntax.
    with pytest.raises(TupleModifyException):
        my_tuple[0] = 123

    # Test __add__ method aka tuple1 + tuple2.
    new_tuple = my_tuple + my_tuple2
    expect(new_tuple.data) == [1, 2, 3, 1, 2, 3, 4]

    # Test count method.
    expect(new_tuple.count(4)) == 1
    expect(new_tuple.count(1)) == 2

    # Test index method.
    expect(new_tuple.index(4)) == 6
    expect(new_tuple.count(3)) == 2


def test_dictionary():
    """
    Tests for Dictionary class for Lab1.
    """
    data = {'name': 'Zaphod', 'age': 42}
    data2 = {'manufacturer': 'Pagani', 'model': 'Zonda'}
    my_dictionary = Dictionary(data)
    my_dictionary2 = Dictionary(data2)

    # Test __str__ method.
    expect(str(my_dictionary)) == f'<Dictionary __str__: {data}>'
    expect(str(my_dictionary2)) == f'<Dictionary __str__: {data2}>'

    # Test __repr__ method.
    expect(repr(my_dictionary)) == f'<Dictionary __repr__: {data}>'
    expect(repr(my_dictionary2)) == f'<Dictionary __repr__: {data2}>'

    # Test __getitem__ method.
    expect(my_dictionary['name']) == 'Zaphod'
    expect(lambda: my_dictionary['height']).to_raise(DictionaryKeyNotFoundException)

    # Test __setitem__ method.
    try:
        my_dictionary['email'] = 'zaphod@beeblebrox.com'
        expect(my_dictionary['email']) == 'zaphod@beeblebrox.com'
    except DictionaryKeyNotFoundException:
        raise DictionaryException('You forgot to implement Dictionary.__setitem__()')

    # Test get method.
    expect(my_dictionary2.get('manufacturer')) == 'Pagani'
    try:
        year = my_dictionary2.get('year', 2020)
    except KeyError:
        raise DictionaryException("Your Dictionary.get() isn't quite finished yet. Add default value support.")
    else:
        expect(my_dictionary2.get('year', 2020)) == 2020

    # Test keys() method.
    expect(my_dictionary.keys()) == my_dictionary.data.keys()
    expect(my_dictionary2.keys()) == my_dictionary2.data.keys()

    # Test values() method.
    expect(list(my_dictionary.values())) == list(my_dictionary.data.values())
    expect(list(my_dictionary2.values())) == list(my_dictionary2.data.values())

    # Test items() method.
    expect(my_dictionary.items()) == my_dictionary.data.items()
    expect(my_dictionary2.items()) == my_dictionary2.data.items()


def test_priority_queue():
    my_priority_queue = PriorityQueue()
    my_priority_queue.put('Bob', 'normal')
    my_priority_queue.put('Alice', 'high')
    my_priority_queue.put('Eve')

    empty_priority_queue = PriorityQueue()
    full_priority_queue = PriorityQueue(maxsize=0)

    # Test __str__method.
    expect(str(my_priority_queue)) == f'<PriorityQueue __str__: {my_priority_queue.queue}>'
    expect(str(empty_priority_queue)) == f'<PriorityQueue __str__: {empty_priority_queue.queue}>'
    expect(str(full_priority_queue)) == f'<PriorityQueue __str__: {full_priority_queue.queue}>'

    # Test __repr__method.
    expect(repr(my_priority_queue)) == f'<PriorityQueue __repr__: {my_priority_queue.queue}>'
    expect(repr(empty_priority_queue)) == f'<PriorityQueue __repr__: {empty_priority_queue.queue}>'
    expect(repr(full_priority_queue)) == f'<PriorityQueue __repr__: {full_priority_queue.queue}>'

    # Test size on empty queue.
    expect(empty_priority_queue.size) == 0

    # Test is_empty on empty queue.
    expect(empty_priority_queue.is_empty) == True

    # Test add_with_priority method.
    expect(my_priority_queue.size) == 3
    my_priority_queue.put('Mallory', 'high')
    expect(my_priority_queue.size) == 4

    # Test add_with_priority on full queue raises QueueIsFullException.
    with pytest.raises(QueueIsFullException):
        full_priority_queue.put('Test', 'medium')

    # Test is_empty on regular queue.
    expect(my_priority_queue.is_empty) == False

    # Test size on regular queue.
    expect(my_priority_queue.size) == 4

    # Test is_full on regular queue.
    expect(my_priority_queue.is_full) == False

    # Test is_full on full queue.
    expect(full_priority_queue.is_full) == True

    # Test front method on empty queue returns None.
    expect(empty_priority_queue.front()) == None

    # Test front method on regular queue returns index of 'Alice'
    expect(my_priority_queue.front()) == 1

    # Test peek on empty queue returns None.
    expect(empty_priority_queue.peek()) == None

    # Test peek on regular queue.
    expect(my_priority_queue.peek()) == 'Alice'

    # Test get on regular queue.
    expect(my_priority_queue.size) == 4
    expect(my_priority_queue.get()) == 'Alice'
    expect(my_priority_queue.size) == 3
    expect(my_priority_queue.get()) == 'Mallory'
    expect(my_priority_queue.size) == 2
    expect(my_priority_queue.get()) == 'Bob'
    expect(my_priority_queue.size) == 1
    expect(my_priority_queue.get()) == 'Eve'

    # Test get on empty queue raises QueueIsEmptyException.
    with pytest.raises(QueueIsEmptyException):
        empty_priority_queue.get()


def test_set():
    """
    Tests for Set class for Lab1.
    """
    data = [1, 2, 3, 4, 3, 2, 1]
    data2 = ['AAA', 'BBB', 'CCC', 'BBB']
    data3 = [1, 10, 100, 'ZZZ', 1, 'BBB', 'XXX', 10]
    my_set = Set(data)
    my_set2 = Set(data2)
    my_set3 = Set(data3)
    my_empty_set = Set()

    # Test __str__ method.
    expect(str(my_set)) == '<Set __str__: [1, 2, 3, 4]>'
    expect(str(my_set2)) == "<Set __str__: ['AAA', 'BBB', 'CCC']>"
    expect(str(my_set3)) == "<Set __str__: [1, 10, 100, 'ZZZ', 'BBB', 'XXX']>"

    # Test __repr__ method.
    expect(repr(my_set)) == '<Set __repr__: [1, 2, 3, 4]>'
    expect(repr(my_set2)) == "<Set __repr__: ['AAA', 'BBB', 'CCC']>"
    expect(repr(my_set3)) == "<Set __repr__: [1, 10, 100, 'ZZZ', 'BBB', 'XXX']>"

    # Test __contains__ method.
    expect(3 in my_set) == True
    expect('AAA' in my_set2) == True
    expect('CCC' not in my_set3) == True
    expect(123 not in my_empty_set) == True

    # Test add method.
    expect(5 in my_set) == False
    my_set.add(5)
    expect(5 in my_set) == True

    # Test remove method.
    my_set.remove(5)
    expect(5 not in my_set) == True
    with pytest.raises(SetElementNotFoundException):
        my_set.remove(5)

    # Test disjoint method.
    expect(set(data).isdisjoint(set(data2))) == True
    expect(my_set.isdisjoint(my_set2)) == True
    expect(set(data2).isdisjoint(set(data3))) == False
    expect(my_set2.isdisjoint(my_set3)) == False
    expect(my_empty_set.isdisjoint(my_set3)) == True
    expect(my_set3.isdisjoint(my_set3)) == False
    expect(my_empty_set.isdisjoint(my_empty_set)) == True

    # Test union method.
    actual_set = set(data).union(set(data2))
    new_set = my_set.union(my_set2)
    expect(set(new_set.data)) == actual_set
    actual_set2 = set(data2).union(set(data3))
    new_set2 = my_set2.union(my_set3)
    expect(set(new_set2.data)) == actual_set2

    # Test intersection method.
    actual_set = set(data).intersection(set(data2))
    new_set = my_set.intersection(my_set2)
    expect(set(new_set.data)) == actual_set
    actual_set2 = set(data2).intersection(set(data3))
    new_set2 = my_set2.intersection(my_set3)
    expect(set(new_set2.data)) == actual_set2

    # Test difference method.
    actual_set = set(data).difference(set(data2))
    new_set = my_set.difference(my_set2)
    expect(set(new_set.data)) == actual_set
    actual_set2 = set(data2).difference(set(data3))
    new_set2 = my_set2.difference(my_set3)
    expect(set(new_set2.data)) == actual_set2

    # Test symmetric difference method.
    actual_set = set(data).symmetric_difference(set(data2))
    new_set = my_set.symmetric_difference(my_set2)
    expect(set(new_set.data)) == actual_set
    actual_set2 = set(data2).symmetric_difference(set(data3))
    new_set2 = my_set2.symmetric_difference(my_set3)
    expect(set(new_set2.data)) == actual_set2

