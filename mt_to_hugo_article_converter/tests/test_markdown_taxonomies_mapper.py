import pytest
import os
from ..config import Config
from ..markdown.taxonomies_mapper import TaxonomiesMapper
from ..mt.attribute import Author, Title, Basename, Status, PrimaryCategory, Category, Date, Tags, Body, ExtendedBody, Keywords


def get_config():
    dirname = os.path.dirname(__file__)
    filepath = os.path.join(dirname, "data/config.yml")
    config = Config(filepath)
    return config


def test_markdown_taxonomies_mapper_single_tag_not_included():
    config = get_config()
    taxonomies_mapper = TaxonomiesMapper()
    attr_name = Tags().name()
    attr_values = ['a']
    mapped = taxonomies_mapper.map(config, attr_name, attr_values)
    assert mapped['tags'] == []
    assert mapped['categories'] == []


def test_markdown_taxonomies_mapper_single_tag_matche_key():
    config = get_config()
    taxonomies_mapper = TaxonomiesMapper()
    attr_name = Tags().name()
    attr_values = ['tag-a']
    mapped = taxonomies_mapper.map(config, attr_name, attr_values)
    assert mapped['tags'] == ['tag-a']
    assert mapped['categories'] == []


def test_markdown_taxonomies_mapper_single_tag_included_values():
    config = get_config()
    taxonomies_mapper = TaxonomiesMapper()
    attr_name = Tags().name()
    attr_values = ['tag-a1']
    mapped = taxonomies_mapper.map(config, attr_name, attr_values)
    assert mapped['tags'] == ['tag-a']
    assert mapped['categories'] == []


def test_markdown_taxonomies_mapper_1():
    config = get_config()
    taxonomies_mapper = TaxonomiesMapper()
    attr_name = Tags().name()
    attr_values = ['a', 'TAG-A', 'tag-a1', 'tag-b1', 'tag-b2']
    mapped = taxonomies_mapper.map(config, attr_name, attr_values)
    assert mapped['tags'] == ['tag-a', 'tag-b']
    assert mapped['categories'] == []


def test_markdown_taxonomies_mapper_2():
    config = get_config()
    taxonomies_mapper = TaxonomiesMapper()
    attr_name = Tags().name()
    attr_values = ['category-a', 'CATEGORY-A', 'category-a1']
    mapped = taxonomies_mapper.map(config, attr_name, attr_values)
    assert mapped['tags'] == []
    assert mapped['categories'] == []


def test_markdown_taxonomies_mapper_3():
    config = get_config()
    taxonomies_mapper = TaxonomiesMapper()
    attr_name = Category().name()
    attr_values = ['a', 'TAG-A', 'tag-a1', 'tag-b1', 'tag-b2']
    mapped = taxonomies_mapper.map(config, attr_name, attr_values)
    assert mapped['tags'] == ['tag-a', 'tag-b']
    assert mapped['categories'] == []


def test_markdown_taxonomies_mapper_4():
    config = get_config()
    taxonomies_mapper = TaxonomiesMapper()
    attr_name = Category().name()
    attr_values = ['category-a', 'CATEGORY-A', 'category-a1']
    mapped = taxonomies_mapper.map(config, attr_name, attr_values)
    assert mapped['tags'] == []
    assert mapped['categories'] == ['category-a']
