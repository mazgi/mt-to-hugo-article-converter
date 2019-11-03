import pytest
from ..config import Config


def test_config():
    config = Config()
    assert config.get_version() == '2019.10.0'
