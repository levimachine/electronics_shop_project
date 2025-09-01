from src.keyboard import Keyboard
import pytest


@pytest.fixture
def copy_item():
    return Keyboard('Microsoft_123', 1000, 10)


def test_setter(copy_item):
    with pytest.raises(AttributeError):
        copy_item.language = 'JJ'


def test_getter(copy_item):
    copy_item.change_lang()
    assert copy_item.language == 'RU'
    copy_item.change_lang()
    assert copy_item.language == 'EN'


def test_str(copy_item):
    assert str(copy_item) == 'Microsoft_123'
