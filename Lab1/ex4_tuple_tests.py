"""
DO NOT MODIFY THIS FILE.

ISCG6426 Lab 1 Semester 1 2020 by Kris Pritchard / @krisrp

Tests used to check correctness of Lab1 answers.
This file requires 'pytest' and 'pyexpect' to run.
Install them with the following command:
    pip install pytest pyexpect

Then run the file with:
    pytest -xv ex4_tuple_tests.py

You need to implement this code so that all of the tests pass.
Feel free to comment out specific tests, but only submit your answers files.
When checking your answers I will use the test files from this repository.


Tuple (Immutable Container):
    For this introductory lab you need to implement functionality for a basic tuple data structure.
    Performance doesn't matter for this.
    None of the method implementations require more than 6 lines of code.
"""
import random
import pytest
from pyexpect import expect
from ex4_tuple import *


"""
Fixtures
"""
@pytest.fixture
def tuple_A():
    return Tuple([1, 2, 3, 2])

@pytest.fixture
def tuple_B():
    return Tuple([1, 2, 3, 4])

@pytest.fixture
def tuple_C():
    return Tuple([random.randint(0, 10) for i in range(100)])


"""
Test __str__
"""
def test_tuple_A_str_method(tuple_A):
    expect(str(tuple_A)) == '<Tuple __str__: [1, 2, 3, 2]>'


def test_tuple_B_str_method(tuple_B):
    expect(str(tuple_B)) == '<Tuple __str__: [1, 2, 3, 4]>'


def test_tuple_C_str_method(tuple_C):
    expect(str(tuple_C)) == f'<Tuple __str__: {tuple_C.data}>'


"""
Test __repr__
"""
def test_tuple_A_repr_method(tuple_A):
    expect(repr(tuple_A)) == '<Tuple __repr__: [1, 2, 3, 2]>'


def test_tuple_B_str_method(tuple_B):
    expect(repr(tuple_B)) == '<Tuple __repr__: [1, 2, 3, 4]>'


def test_tuple_C_str_method(tuple_C):
    expect(repr(tuple_C)) == f'<Tuple __repr__: {tuple_C.data}>'


"""
Test __getitem__ aka my_tuple[0] lookups.
"""
def test_tuple_A_getitem(tuple_A):
    expect(tuple_A[0]) == 1


def test_tuple_B_getitem(tuple_B):
    expect(tuple_B[-1]) == 4


def test_tuple_C_raises_tuple_index_exception_on_invalid_index(tuple_C):
    expect(lambda: tuple_C[100]).to_raise(exception_class=TupleIndexException)


"""
Test __setitem__ aka my_tuple[0] = some_value raises TupleModifyException
"""
def test_modifying_tuple_raises_tuplemodifyexception(tuple_A):
    with pytest.raises(TupleModifyException):
        tuple_A[0] = 123


"""
Test __add__ aka tuple3 = tuple1 + tuple2
"""
def test_adding_two_tuples(tuple_A, tuple_B):
    test_tuple = tuple_A + tuple_B
    expect(test_tuple.data) == list(tuple_A.data + tuple_B.data)


"""
Test count
"""
def test_tuple_count_method(tuple_A):
    expect(tuple_A.count(4)) == 0
    expect(tuple_A.count(2)) == 2


"""
Test index
"""
def test_tuple_index_method(tuple_B):
    expect(tuple_B.index(4)) == 3
    expect(tuple_B.index(2)) == 1
    expect(tuple_B.index(1)) == 0

