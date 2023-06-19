import csv

import pytest as pytest

from src.item import Item
from src.keyboard import KeyBoard
from src.phone import Phone


@pytest.fixture
def test_obj_item():
    """ Тестовый объект класса Item. """

    obj = Item("Смартфон", 10000, 20)
    return obj


@pytest.fixture
def test_obj_phone():
    """ Тестовый объект класса Phone. """

    obj = Phone("iPhone 14", 120_000, 5, 2)
    return obj


@pytest.fixture
def test_obj_keyboard():
    """ Тестовый объект класса KeyBoard. """

    obj = KeyBoard('Dark Project KD87A', 9600, 5)
    return obj


@pytest.fixture(scope='module')
def csv_data():
    """ Содержит данные csv для тестов. """

    csv_ = [{'name': 'Смартфон', 'price': 100, 'quantity': 1},
            {'name': 'Ноутбук', 'price': 1000, 'quantity': 3},
            {'name': 'Кабель', 'price': 10, 'quantity': 5},
            {'name': 'Мышка', 'price': 50, 'quantity': 5},
            {'name': 'Клавиатура', 'price': 75, 'quantity': 5}]

    return csv_


@pytest.fixture(scope='module')
def temp_file_csv(tmpdir_factory, csv_data):
    """
    Записываем тестовые данные в файл 'test_items.csv' во временной
    директории.
    """

    temp_data = csv_data
    file_ = tmpdir_factory.mktemp('data').join('test_items.csv')
    fieldnames = ['name', 'price', 'quantity']

    with open(file_, 'w', newline='') as f:
        test_file = csv.DictWriter(f, fieldnames=fieldnames)
        test_file.writeheader()
        test_file.writerows(temp_data)
    return file_


@pytest.fixture(scope='module')
def csv_data_broken():
    """ Содержит данные csv без последней колонки для тестов. """

    csv_broken = [{'name': 'Смартфон', 'price': 100},
            {'name': 'Ноутбук', 'price': 1000},
            {'name': 'Кабель', 'price': 10},
            {'name': 'Мышка', 'price': 50},
            {'name': 'Клавиатура', 'price': 75}]

    return csv_broken


@pytest.fixture(scope='module')
def temp_file_csv_broken(tmpdir_factory, csv_data_broken):
    """
    Записываем тестовые данные в файл 'test_items_broken.csv' во временной
    директории.
    """

    temp_data = csv_data_broken
    file_broken = tmpdir_factory.mktemp('data').join('test_items_broken.csv')
    fieldnames = ['name', 'price']

    with open(file_broken, 'w', newline='') as f:
        test_file = csv.DictWriter(f, fieldnames=fieldnames)
        test_file.writeheader()
        test_file.writerows(temp_data)
    return file_broken
