"""
DO NOT MODIFY THIS FILE.

ISCG6426 Lab 1 Semester 1 2020 by Kris Pritchard / @krisrp

Tests used to check correctness of Lab1 answers.
This file requires 'pytest' and 'pyexpect' to run.
Install them with the following command:
    pip install pytest pyexpect

Then run the file with:
    pytest -xv ex5_dictionary_tests.py

You need to implement this code so that all of the tests pass.
Feel free to comment out specific tests, but only submit your answers files.
When checking your answers I will use the test files from this repository.


Naive Dictionary (Interface):
    For this introductory lab you need to implement functionality for a basic dictionary/hashmap data structure.
    Performance doesn't matter for this.
    None of the method implementations require more than 6 lines of code.
"""
import pytest
from pyexpect import expect
from ex5_dictionary import *


@pytest.fixture
def data_A():
    return {'name': 'Zaphod', 'age': 42}


@pytest.fixture
def data_B():
    return {'manufacturer': 'Pagani', 'model': 'Zonda'}


@pytest.fixture
def dictionary_A():
    return Dictionary({'name': 'Zaphod', 'age': 42})


@pytest.fixture
def dictionary_B():
    return Dictionary({'manufacturer': 'Pagani', 'model': 'Zonda'})


"""
Test __str__
"""
def test_str_method_on_dictionary_A(data_A, dictionary_A):
    expect(str(dictionary_A)) == f'<Dictionary __str__: {data_A}>'


def test_str_method_on_dictionary_B(data_B, dictionary_B):
    expect(str(dictionary_B)) == f'<Dictionary __str__: {data_B}>'


"""
Test __repr__
"""
def test_repr_method_on_dictionary_A(data_A, dictionary_A):
    expect(repr(dictionary_A)) == f'<Dictionary __repr__: {data_A}>'


def test_repr_method_on_dictionary_B(data_B, dictionary_B):
    expect(repr(dictionary_B)) == f'<Dictionary __repr__: {data_B}>'


"""
Test __getitem__ aka my_dictionary['keyname'] lookup
"""
def test_getitem_works_on_dictionary_A(dictionary_A):
    expect(dictionary_A['name']) == 'Zaphod'


def test_getitem_raises_dictionarykeynotfoundexception_on_nonexistent_key(dictionary_A):
    expect(lambda: dictionary_A['height']).to_raise(DictionaryKeyNotFoundException)


"""
Test __setitem__ aka my_dictionary['keyname'] = 'somevalue'
"""
def test_setitem_works_on_dictionary_and_raises_dictionarykeynotfoundexception_otherwise(dictionary_A):
    try:
        dictionary_A['email'] = 'zaphod@beeblebrox.com'
        expect(dictionary_A['email']) == 'zaphod@beeblebrox.com'
    except DictionaryKeyNotFoundException:
        raise DictionaryException('You forgot to implement Dictionary.__setitem__()')

"""
Test get aka my_dictionary.get('keyname')
"""
def test_dictionary_get_method_works(dictionary_B):
    expect(dictionary_B.get('manufacturer')) == 'Pagani'

def test_dictionary_get_method_supports_default_values(dictionary_B):
    try:
        year = dictionary_B.get('year', 2020)
    except KeyError:
        raise NotImplementedError("Your Dictionary.get() isn't quite finished yet. Add default value support.")
    else:
        expect(dictionary_B.get('year', 2020)) == 2020

"""
Test keys()
"""
def test_dictionary_keys_method_on_dictionary_A(dictionary_A):
    expect(dictionary_A.keys()) == dictionary_A.data.keys()

def test_dictionary_keys_method_on_dictionary_B(dictionary_B):
    expect(dictionary_B.keys()) == dictionary_B.data.keys()


"""
Test values()
"""
def test_dictionary_values_method_on_dictionary_A(dictionary_A):
    expect(list(dictionary_A.values())) == list(dictionary_A.data.values())

def test_dictionary_values_method_on_dictionary_B(dictionary_B):
    expect(list(dictionary_B.values())) == list(dictionary_B.data.values())


"""
Test values()
"""
def test_dictionary_items_method_on_dictionary_A(dictionary_A):
    expect(dictionary_A.items()) == dictionary_A.data.items()


def test_dictionary_items_method_on_dictionary_B(dictionary_B):
    expect(dictionary_B.items()) == dictionary_B.data.items()

