import pytest
from mt.attribute import Author, Title, Basename, Status, PrimaryCategory, Category, Date, Tags, Body, ExtendedBody, Keywords


def test_author_name():
    author = Author()
    assert author.name() == 'Author'
