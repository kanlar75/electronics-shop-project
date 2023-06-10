from src.item import Item


class Phone(Item):

    def __init__(self, name, price, quantity, number_of_sim):
        """ Инициализатор. """

        super().__init__(name, price, quantity)

        self.__number_of_sim = number_of_sim

    @classmethod
    def validate(cls, obj):
        """
        Проверка принадлежности к классу 'Item' или 'Phone' для
        переопределения метода __add__.
        """

        if not isinstance(obj, (Item, Phone)):
            raise TypeError('Объект должен быть экземпляром класса '
                            'Item или Phone!')
        return obj.quantity

    @property
    def number_of_sim(self):
        """ Возвращает количество сим карт. """

        return self.__number_of_sim

    @number_of_sim.setter
    def number_of_sim(self, value):
        """ Сеттер количества сим карт с проверкой на целое число больше 0. """

        if not (value > 0) or value == 0 or not isinstance(value, int):
            raise ValueError("Количество физических SIM-карт должно быть "
                             "целым числом больше нуля")
        self.__number_of_sim = value

    def __repr__(self):
        """ __repr__"""

        return f"{self.__class__.__name__}('{self.name}', {self.price}," \
               f" {self.quantity}, {self.number_of_sim})"

    def __add__(self, other):
        """ Возвращает сумму двух экземпляров """

        obj = self.validate(other)
        return self.quantity + obj
