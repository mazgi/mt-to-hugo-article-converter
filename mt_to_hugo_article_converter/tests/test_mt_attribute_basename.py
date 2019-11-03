import pytest
from mt.attribute import Author, Title, Basename, Status, PrimaryCategory, Category, Date, Tags, Body, ExtendedBody, Keywords


def test_mt_attribute_basename_basic():
    basename = Basename().set('BASENAME: a-basename')
    assert basename.value() == 'a-basename'


def test_mt_attribute_basename_include_uppercases():
    basename = Basename().set('BASENAME: A-Basename')
    assert basename.value() == 'a-basename'


def test_mt_attribute_basename_include_underscores():
    basename = Basename().set('BASENAME: a_basename')
    assert basename.value() == 'a-basename'


def test_mt_attribute_basename_include_slashes():
    basename = Basename().set('BASENAME: a/basename')
    assert basename.value() == 'a-basename'
