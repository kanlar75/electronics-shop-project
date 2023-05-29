import pytest as pytest

from src.item import Item


@pytest.fixture
def creat_obj():
    obj = Item("Смартфон", 10000, 20)
    return obj



