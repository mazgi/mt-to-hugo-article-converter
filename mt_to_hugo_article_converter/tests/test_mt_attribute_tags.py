import pytest
from mt.attribute import Author, Title, Basename, Status, PrimaryCategory, Category, Date, Tags, Body, ExtendedBody, Keywords


def test_mt_attribute_tags_empty_value():
    tags = Tags().set('TAGS: ')
    v = tags.value()
    assert len(v) == 0
    assert v == []


def test_mt_attribute_tags_single_value():
    tags = Tags().set('TAGS: a-tag')
    v = tags.value()
    assert len(v) == 1
    assert v == ['a-tag']


def test_mt_attribute_tags_comma_separated_values():
    tags = Tags().set('TAGS: a-tag,b-tag, c-tag')
    v = tags.value()
    assert len(v) == 3
    assert v == ['a-tag', 'b-tag', 'c-tag']


def test_mt_attribute_tags_quoted_comma_separated_values():
    tags = Tags().set('TAGS: "a-tag,b-tag, c-tag "')
    v = tags.value()
    assert len(v) == 3
    assert v == ['a-tag', 'b-tag', 'c-tag']


def test_mt_attribute_tags_whitespace_separated_values():
    tags = Tags().set('TAGS: a-tag b-tag  c-tag')
    v = tags.value()
    assert len(v) == 3
    assert v == ['a-tag', 'b-tag', 'c-tag']


def test_mt_attribute_tags_quoted_whitespace_separated_values():
    tags = Tags().set('TAGS: "a-tag b-tag  c-tag "')
    v = tags.value()
    assert len(v) == 3
    assert v == ['a-tag', 'b-tag', 'c-tag']
