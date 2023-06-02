import contextlib
import io

import pytest as pytest

from src.item import Item


def test_calculate_total_price(creat_obj):
    assert creat_obj.calculate_total_price() == 200000


@pytest.mark.parametrize("pay_rate, price", [(0.7, 7000), (0.8, 8000)])
def test_apply_discount(creat_obj, pay_rate, price):
    Item.pay_rate = pay_rate
    creat_obj.apply_discount()
    assert creat_obj.price == price


def test_all(creat_obj):
    assert isinstance(Item.all, list)
    for obj in Item.all:
        assert isinstance(obj, Item)


def test_name(creat_obj):
    item1 = Item('Смартфон', 10000, 5)
    item1.name = 'Phone'
    assert item1.name == 'Phone'
    item1.name = 'Phone111111'
    s = io.StringIO()
    with contextlib.redirect_stdout(s):
        item1.name = 'Phone111111'
    assert s.getvalue() == f'Длина наименования товара превышает 10 ' \
                           f'символов.\n'


@pytest.mark.parametrize("str_, expectation", [('5', 5), ('5.5', 5)])
def test_string_to_number(str_, expectation):
    assert Item.string_to_number(str_) == expectation


def test_instantiate_from_csv(temp_file_csv):
    Item.instantiate_from_csv(temp_file_csv)
    assert len(Item.all) == 5
    item1 = Item.all[1]
    assert item1.name == 'Ноутбук'
