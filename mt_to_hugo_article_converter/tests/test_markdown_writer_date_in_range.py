import pytest
from ..config import Config
from ..markdown import Writer
from ..mt.attribute import Author, Title, Basename, Status, PrimaryCategory, Category, Date, Tags, Body, ExtendedBody, Keywords


def test_markdown_writer_date_in_range_1():
    record = Date().set('DATE: 11/22/2010 05:00:01 AM')
    config = Config(
    ).set_start_at(
        '2010/11/22 05:00:00'
    ).set_stop_at(
        '2010/11/22 05:00:01'
    )
    writer = Writer(config)
    assert writer.is_not_target(record.value()) == False


def test_markdown_writer_date_in_range_2():
    record = Date().set('DATE: 11/22/2010 05:00:01 AM')
    config = Config(
    ).set_start_at(
        '2010/11/22 05:00:01'
    ).set_stop_at(
        '2010/11/22 05:00:02'
    )
    writer = Writer(config)
    assert writer.is_not_target(record.value()) == False


def test_markdown_writer_date_in_range_3():
    record = Date().set('DATE: 11/22/2010 05:00:01 AM')
    config = Config(
    ).set_start_at(
        '2010/11/22 05:00:01'
    ).set_stop_at(
        None
    )
    writer = Writer(config)
    assert writer.is_not_target(record.value()) == False


def test_markdown_writer_date_in_range_4():
    record = Date().set('DATE: 11/22/2010 05:00:01 AM')
    config = Config(
    ).set_start_at(
        None
    ).set_stop_at(
        '2010/11/22 05:00:01'
    )
    writer = Writer(config)
    assert writer.is_not_target(record.value()) == False
