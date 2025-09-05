"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest

from src.item import Item, InstantiateCSVError

CSV_ITEM_PATH = r'C:\Users\User\PycharmProjects\electronics-shop-project\src\items.csv'
CSV_TEST_PATH = r'C:\Users\User\PycharmProjects\electronics-shop-project\tests\items.csv'

@pytest.fixture
def copy_item():
    return Item('Зарядник', 1000, 5)


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
    Item.instantiate_from_csv(CSV_ITEM_PATH)
    assert Item.all[0].name == 'Смартфон'
    assert Item.all[0].price == 100.0
    assert Item.all[0].quantity == 1


def test_string_to_number(copy_item):
    assert copy_item.string_to_number('5.5') == 5
    assert copy_item.string_to_number('5') == 5
    assert copy_item.string_to_number('5.0') == 5


def test_repr(copy_item):
    assert repr(copy_item) == "Item('Зарядник', 1000, 5)"


def test_str(copy_item):
    assert str(copy_item) == 'Зарядник'


def test_add(copy_item):
    assert copy_item + copy_item == 10

    with pytest.raises(TypeError):
        copy_item + 5

    with pytest.raises(TypeError):
        copy_item + 'abc'


def test_instantiate_csv_error_class(copy_item):
    with pytest.raises(FileNotFoundError):
        copy_item.instantiate_from_csv('items_1.csv')
    with pytest.raises(InstantiateCSVError):
        copy_item.instantiate_from_csv(CSV_TEST_PATH)
