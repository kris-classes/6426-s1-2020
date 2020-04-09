"""
DO NOT MODIFY THIS FILE.

ISCG6426 Lab 1 Semester 1 2020 by Kris Pritchard / @krisrp

Tests used to check correctness of Lab1 answers.
This file requires 'pytest' and 'pyexpect' to run.
Install them with the following command:
    pip install pytest pyexpect

Then run the file with:
    pytest -xv ex6_set_tests.py

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
from ex6_set import *


'''
Set fixtures

These get recreated every time a test is run.
'''
@pytest.fixture
def empty_set():
    return Set()


@pytest.fixture
def data_A():
    return [1, 2, 3, 4, 3, 2, 1]


@pytest.fixture
def set_A():
    return Set([1, 2, 3, 4, 3, 2, 1])


@pytest.fixture
def data_B():
    return ['AAA', 'BBB', 'CCC', 'BBB']


@pytest.fixture
def set_B():
    return Set(['AAA', 'BBB', 'CCC', 'BBB'])


@pytest.fixture
def data_C():
    return [1, 10, 100, 'ZZZ', 1, 'BBB', 'XXX', 10]


@pytest.fixture
def set_C():
    return Set([1, 10, 100, 'ZZZ', 1, 'BBB', 'XXX', 10])


'''
Test __str___
'''
def test_empty_set_str_method():
    expect(str(Set())) == '<Set __str__: []>'


def test_set_A_str_method(set_A):
    expect(str(set_A)) == '<Set __str__: [1, 2, 3, 4]>'


def test_set_B_str_method(set_B):
    expect(str(set_B)) == "<Set __str__: ['AAA', 'BBB', 'CCC']>"

def test_set_C_str_method(set_C):
    expect(str(set_C)) == "<Set __str__: [1, 10, 100, 'ZZZ', 'BBB', 'XXX']>"


'''
Test __repr___
'''
def test_set_A_repr_method(set_A):
    expect(repr(set_A)) == '<Set __repr__: [1, 2, 3, 4]>'


def test_set_B_repr_method(set_B):
    expect(repr(set_B)) == "<Set __repr__: ['AAA', 'BBB', 'CCC']>"


def test_set_C_repr_method(set_C):
    expect(repr(set_C)) == "<Set __repr__: [1, 10, 100, 'ZZZ', 'BBB', 'XXX']>"


'''
Test __contains___
'''
def test_set_A_contains_method(set_A):
    expect(3 in set_A) == True


def test_set_B_contains_method(set_B):
    expect('AAA' in set_B) == True


def test_set_C_contains_method(set_C):
    expect('CCC' not in set_C) == True


def test_empty_set_contains_method(empty_set):
    expect(123 not in empty_set) == True


'''
Test __add___
'''
def test_add_method(set_A):
    expect(5 in set_A) == False
    set_A.add(5)
    expect(5 in set_A) == True


'''
Test __remove___
'''
def test_remove_method(set_A):
    set_A.remove(3)
    expect(3 not in set_A) == True


def test_remove_raises_SetElementNotFoundException_if_element_not_in_set(set_A):
    with pytest.raises(SetElementNotFoundException):
        set_A.remove(5)


'''
Test disjoint method
'''
def test_disjoint_method_on_set_A_and_set_B(data_A, set_A, data_B, set_B):
    expect(set(data_A).isdisjoint(set(data_B))) == True
    expect(set_A.isdisjoint(set_B)) == True


def test_disjoint_method_on_set_A_and_set_B(data_B, set_B, data_C, set_C):
    expect(set(data_B).isdisjoint(set(data_C))) == False
    expect(set_B.isdisjoint(set_C)) == False


def test_empty_set_is_disjoint_with_set_C(empty_set, set_C):
    expect(empty_set.isdisjoint(set_C)) == True


def test_set_C_is_not_disjoint_with_itself(set_C):
    expect(set_C.isdisjoint(set_C)) == False


def test_empty_set_is_disjoint_with_itself(empty_set):
    expect(empty_set.isdisjoint(empty_set)) == True


'''
Test union method
'''
def test_union_method_on_set_A_and_set_B(data_A, set_A, data_B, set_B):
    expected_set = set(data_A).union(set(data_B))
    test_set = set_A.union(set_B)
    expect(set(test_set.data)) == expected_set


def test_union_method_on_set_B_and_set_C(data_B, set_B, data_C, set_C):
    expected_set = set(data_B).union(set(data_C))
    test_set = set_B.union(set_C)
    expect(set(test_set.data)) == expected_set


'''
Test intersection method
'''
def test_intersection_method_on_set_A_and_set_B(data_A, set_A, data_B, set_B):
    expected_set = set(data_A).intersection(set(data_B))
    test_set = set_A.intersection(set_B)
    expect(set(test_set.data)) == expected_set


def test_intersection_method_on_set_B_and_set_C(data_B, set_B, data_C, set_C):
    expected_set = set(data_B).intersection(set(data_C))
    test_set = set_B.intersection(set_C)
    expect(set(test_set.data)) == expected_set

'''
Test difference method
'''
def test_difference_method_on_set_A_and_set_B(data_A, set_A, data_B, set_B):
    expected_set = set(data_A).difference(set(data_B))
    test_set = set_A.difference(set_B)
    expect(set(test_set.data)) == expected_set

def test_difference_method_on_set_B_and_set_C(data_B, set_B, data_C, set_C):
    expected_set = set(data_B).difference(set(data_C))
    test_set = set_B.difference(set_C)
    expect(set(test_set.data)) == expected_set


'''
Test symmetric difference method
'''
def test_symmetric_difference_method_on_set_A_and_set_B(set_A, data_A, set_B, data_B):
    expected_set = set(data_A).symmetric_difference(set(data_B))
    test_set = set_A.symmetric_difference(set_B)
    expect(set(test_set.data)) == expected_set


def test_symmetric_difference_method_on_set_B_and_set_C(set_B, data_B, set_C, data_C):
    expected_set = set(data_B).symmetric_difference(set(data_C))
    test_set = set_B.symmetric_difference(set_C)
    expect(set(test_set.data)) == expected_set


'''
Test that nobody is cheating by using a set().
'''
def test_that_nobody_is_cheating_by_using_a_set(set_A, set_C):
    expect(isinstance(set_A.data, set)) == False

