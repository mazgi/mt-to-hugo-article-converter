import pytest
from ..mt.attribute import Author, Title, Basename, Status, PrimaryCategory, Category, Date, Tags, Body, ExtendedBody, Keywords


def test_mt_attribute_category_empty_value():
    category = Category().set('CATEGORY: ')
    v = category.value()
    assert len(v) == 0
    assert v == []


def test_mt_attribute_category_single_value():
    category = Category().set('CATEGORY: a-category')
    v = category.value()
    assert len(v) == 1
    assert v == ['a-category']


def test_mt_attribute_category_single_value_include_whitespace():
    category = Category().set('CATEGORY: a category')
    v = category.value()
    assert len(v) == 1
    assert v == ['a category']
