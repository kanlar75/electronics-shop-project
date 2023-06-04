import csv


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = name
        self.price = price
        self.quantity = quantity

    @classmethod
    def instantiate_from_csv(cls, file_path="items.csv"):

        with open(file_path) as csvfile:
            readers = csv.DictReader(csvfile)
            for reader in readers:
                name = reader['name']
                price = reader['price']
                quantity = reader['quantity']
                new_ = Item(name=name, price=price, quantity=quantity)
                cls.all.append(new_)

    @staticmethod
    def string_to_number(str_):

        return int(float(str_))

    @property
    def name(self):
        return f'{self.__name}'

    @name.setter
    def name(self, value):
        if len(value.strip()) < 10:
            self.__name = value
        else:
            print('Длина наименования товара превышает 10 символов.')

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        total_cost = self.price * self.quantity
        return total_cost

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """

        self.price = self.price * Item.pay_rate

    def __repr__(self):
        return f"Item('{self.__name}', {self.price}, {self.quantity})"

    def __str__(self):
        return self.__name
