from src.item import Item


def test_calculate_total_price(creat_obj):
    assert creat_obj.calculate_total_price() == 200000


def test_apply_discount(creat_obj):
    Item.pay_rate = 0.7
    creat_obj.apply_discount()
    assert creat_obj.price == 7000


def test_all(creat_obj):
    assert isinstance(Item.all, list)
    for obj in Item.all:
        assert isinstance(obj, Item)

