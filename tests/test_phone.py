import pytest


# Тестируем метод класса, определяющий принадлежность к классу, должен
# вернуть значение атрибута 'quantity' экземпляра класса 'Phone',
# если принадлежит классу 'Item' или 'Phone', иначе raise: TypeError
def test_validate(test_obj_phone):
    with pytest.raises(TypeError):
        test_obj_phone.validate("test")
        test_obj_phone.validate(1)
    assert test_obj_phone.validate(test_obj_phone) == 5


# Тест __repr__
def test_repr(test_obj_phone):
    assert repr(test_obj_phone) == "Phone('iPhone 14', 120000, 5, 2)"


# Проверяем setter, устанавливаем новое значение int, получаем атрибут.
# Проверяем, что при попытке установить значение 0, < 0, str или float,
# возникает исключение ValueError

def test_name(test_obj_phone):
    test_obj_phone.number_of_sim = 1
    assert test_obj_phone.number_of_sim == 1
    with pytest.raises(ValueError):
        test_obj_phone.number_of_sim = 0
        test_obj_phone.number_of_sim = -1
        test_obj_phone.number_of_sim = 2.0
        test_obj_phone.number_of_sim = '2.0'


# Тестируем сложение по атрибуту 'quantity'
def test_add(test_obj_phone, test_obj_item):
    assert test_obj_phone + test_obj_item == 25
