"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest

from src.item import Item

@pytest.fixture
def copy_item():
    return Item('Зарядник', 1000.0, 5)


def test_calculate_total_price(copy_item):
    assert copy_item.calculate_total_price() == 5000.0


def test_apply_discount(copy_item):
    Item.pay_rate = 0.5
    copy_item.apply_discount()
    assert copy_item.price == 500.0
