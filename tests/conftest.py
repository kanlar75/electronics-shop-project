import csv

import pytest as pytest

from src.item import Item


@pytest.fixture
def creat_obj():
    obj = Item("Смартфон", 10000, 20)
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
    file_path = tmpdir_factory.mktemp('data').join('test_items.csv')
    fieldnames = ['name', 'price', 'quantity']

    with open(file_path, 'w', newline='') as f:
        test_file = csv.DictWriter(f, fieldnames=fieldnames)
        test_file.writeheader()
        test_file.writerows(temp_data)
    return file_path
