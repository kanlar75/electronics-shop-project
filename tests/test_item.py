import pytest

from src.item import Item


@pytest.fixture
def creat_obj():
    obj = Item("Смартфон", 10000, 20)
    return obj


def test_calculate_total_price(creat_obj):
    assert creat_obj.calculate_total_price() == 200000


def test_apply_discount(creat_obj):
    Item.pay_rate = 0.5
    assert creat_obj.apply_discount() == creat_obj.price


def test_all(creat_obj):
    assert len(Item.all) == 2
    assert isinstance(Item.all, list)
