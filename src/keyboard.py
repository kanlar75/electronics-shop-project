from src.item import Item


class KeyBoard(Item):

    def __init__(self, name: str, price: float, quantity: int, language="EN"):
        super().__init__(name, price, quantity)
        self._language = language

    def change_lang(self):
        """ Метод для изменения языка (раскладки клавиатуры). """

        if self.language == "EN":
            self._language = "RU"
        else:
            self._language = "EN"
        return self

    @property
    def language(self):
        """ Возвращает атрибут name. """

        return f'{self._language}'
