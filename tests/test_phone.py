import pytest

from src.phone import Phone


@pytest.fixture
def copy_item():
    return Phone('Самсунг', 5000, 5, 2)


def test_init(copy_item):
    assert copy_item.name == 'Самсунг'
    assert copy_item.price == 5000
    assert copy_item.quantity == 5
    assert copy_item.number_of_sim == 2


def test_repr(copy_item):
    assert repr(copy_item) == "Phone('Самсунг', 5000, 5, 2)"


def test_getter(copy_item):
    assert copy_item.number_of_sim == 2


def test_setter(copy_item):
    copy_item.number_of_sim = 5

    with pytest.raises(ValueError):
        copy_item.number_of_sim = 0
