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

