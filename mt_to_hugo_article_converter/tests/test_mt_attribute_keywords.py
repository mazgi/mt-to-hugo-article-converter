import pytest
from ..mt.attribute import Author, Title, Basename, Status, PrimaryCategory, Category, Date, Tags, Body, ExtendedBody, Keywords


def test_mt_attribute_keywords_empty_value():
    keywords = Keywords().set(
        '-----'
    ).set(
        'KEYWORDS:'
    ).set(
        ''
    ).set(
        '-----'
    )
    v = keywords.value()
    assert len(v) == 0
    assert v == []


def test_mt_attribute_keywords_single_value():
    keywords = Keywords().set(
        '-----'
    ).set(
        'KEYWORDS:'
    ).set(
        'keyword-a'
    ).set(
        '-----'
    )
    v = keywords.value()
    assert len(v) == 1
    assert v == ['keyword-a']


def test_mt_attribute_keywords_comma_separated_values():
    keywords = Keywords().set(
        '-----'
    ).set(
        'KEYWORDS:'
    ).set(
        'keyword-a,keyword-b , keyword-c'
    ).set(
        '-----'
    )
    v = keywords.value()
    assert len(v) == 3
    assert v == ['keyword-a', 'keyword-b', 'keyword-c']


def test_mt_attribute_keywords_whitespace_separated_values():
    keywords = Keywords().set(
        '-----'
    ).set(
        'KEYWORDS:'
    ).set(
        ' keyword-a keyword-b  keyword-c '
    ).set(
        '-----'
    )
    v = keywords.value()
    assert len(v) == 3
    assert v == ['keyword-a', 'keyword-b', 'keyword-c']
