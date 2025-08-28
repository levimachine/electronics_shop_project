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


def test_getter(copy_item):
    assert copy_item.name == 'Зарядник'


def test_setter(copy_item):
    copy_item.name = 'СуперЗарядник'
    assert copy_item.name == 'СуперЗаряд'
    copy_item.name = 'ЗаРядниК'
    assert copy_item.name == 'ЗаРядниК'


def test_instantiate_from_csv():
    Item.instantiate_from_csv(r'C:\Users\User\PycharmProjects\electronics-shop-project\src\items.csv')
    assert Item.all[0].name == 'Смартфон'
    assert Item.all[0].price == 100.0
    assert Item.all[0].quantity == 1


def test_string_to_number(copy_item):
    assert copy_item.string_to_number('5.5') == 5
    assert copy_item.string_to_number('5') == 5
    assert copy_item.string_to_number('5.0') == 5