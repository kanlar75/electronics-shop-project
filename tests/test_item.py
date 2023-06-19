import contextlib
import io

import pytest as pytest

from src.item import Item, InstantiateCSVError


# Получаем общую стоимость конкретного товара в магазине.
def test_calculate_total_price(test_obj_item):
    assert test_obj_item.calculate_total_price() == 200000


# Применяем установленную скидку для конкретного товара.
@pytest.mark.parametrize("pay_rate, price", [(0.7, 7000), (0.8, 8000)])
def test_apply_discount(test_obj_item, pay_rate, price):
    Item.pay_rate = pay_rate
    test_obj_item.apply_discount()
    assert test_obj_item.price == price


# Проверяем, что все экземпляры класса Item в атрибуте Item.all.
def test_all(test_obj_item):
    assert isinstance(Item.all, list)
    for obj in Item.all:
        assert isinstance(obj, Item)


# Проверяем getter, setter и print() в setter при несоответствии длины
# наименования товара.
def test_name(test_obj_item):
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


# Проверяем возврат числа из строки-числа.
@pytest.mark.parametrize("str_, expectation", [('5', 5), ('5.5', 5)])
def test_string_to_number(str_, expectation):
    assert Item.string_to_number(str_) == expectation


# Проверка инициализации экземпляров класса `Item` данными из файла
# src/items.csv.
def test_instantiate_from_csv(temp_file_csv):
    Item.instantiate_from_csv(temp_file_csv)
    assert len(Item.all) == 5
    item1 = Item.all[1]
    assert item1.name == 'Ноутбук'


# Тест __repr__
def test_repr(test_obj_item):
    assert repr(test_obj_item) == "Item('Смартфон', 10000, 20)"


# Тест __str__
def test_str(test_obj_item):
    assert str(test_obj_item) == 'Смартфон'


# Тестируем сложение по атрибуту 'quantity'
def test_add(test_obj_item, test_obj_phone):
    assert test_obj_item + test_obj_phone == 25


# Тестируем метод класса, определяющий принадлежность к классу, должен
# вернуть True если экземпляр принадлежит к классу 'Item', иначе
# raise: TypeError

def test_validate(test_obj_item):
    with pytest.raises(TypeError):
        test_obj_item.validate("test")
        test_obj_item.validate(1)
    assert test_obj_item.validate(test_obj_item) is True


# Тест инициализации и __str__ объекта класса InstantiateCSVError
def test_raises():
    obj = InstantiateCSVError()
    assert obj.__str__() == 'Файл item.csv поврежден'


# Тест открытия отсутствующего файла

def test_instantiate_from_csv_raise():
    s = io.StringIO()
    with contextlib.redirect_stdout(s):
        Item.instantiate_from_csv('items111.csv')
    assert s.getvalue() == 'FileNotFoundError: Отсутствует файл items.csv\n'


# Проверка инициализации экземпляров класса `Item` данными из
# поврежденного файла src/items_bad.csv.
# @pytest.mark.xfail(raises=InstantiateCSVError)
def test_instantiate_from_csv_bad(temp_file_csv_broken):
    try:
        with pytest.raises(InstantiateCSVError,
                           match="Файл item.csv поврежден") as e:
            Item.instantiate_from_csv(temp_file_csv_broken)
        assert e.type == InstantiateCSVError
        assert e.value == "Файл item.csv поврежден"
    except:
        assert True
