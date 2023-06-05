import contextlib
import io

import pytest as pytest

from src.item import Item


# получаем общую стоимость конкретного товара в магазине
def test_calculate_total_price(test_obj):
    assert test_obj.calculate_total_price() == 200000


# применяем установленную скидку для конкретного товара
@pytest.mark.parametrize("pay_rate, price", [(0.7, 7000), (0.8, 8000)])
def test_apply_discount(test_obj, pay_rate, price):
    Item.pay_rate = pay_rate
    test_obj.apply_discount()
    assert test_obj.price == price


# проверяем, что все экземпляры класса Item в атрибуте Item.all
def test_all(test_obj):
    assert isinstance(Item.all, list)
    for obj in Item.all:
        assert isinstance(obj, Item)


# проверяем getter и setter
def test_name(test_obj):
    item1 = Item('Смартфон', 10000, 5)
    assert item1.name == 'Смартфон'
    item1.name = 'Phone'
    assert item1.name == 'Phone'
    item1.name = 'Phone111111'
    s = io.StringIO()
    with contextlib.redirect_stdout(s):
        item1.name = 'Phone111111'
    assert s.getvalue() == f'Длина наименования товара превышает 10 ' \
                           f'символов.\n'


# проверяем возврат числа из строки-числа
@pytest.mark.parametrize("str_, expectation", [('5', 5), ('5.5', 5)])
def test_string_to_number(str_, expectation):
    assert Item.string_to_number(str_) == expectation


# проверка инициализации экземпляров класса `Item` данными из файла
# src/items.csv
def test_instantiate_from_csv(temp_file_csv):
    Item.instantiate_from_csv(temp_file_csv)
    assert len(Item.all) == 5
    item1 = Item.all[1]
    assert item1.name == 'Ноутбук'


def test_repr(test_obj):
    assert repr(test_obj) == "Item('Смартфон', 10000, 20)"


def test_str(test_obj):
    assert str(test_obj) == 'Смартфон'


