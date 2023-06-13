from src.item import Item


class MixinLayout:
    layout = None

    def change_lang(self):
        """ Метод для изменения языка (раскладки клавиатуры). """

        if self._language == "EN":
            self._language = "RU"
        else:
            self._language = "EN"
        MixinLayout.layout = self._language
        return self


class KeyBoard(Item, MixinLayout):

    def __init__(self, name: str, price: float, quantity: int, language="EN"):
        super().__init__(name, price, quantity)
        self._language = language
        MixinLayout.layout = self._language

    @property
    def language(self):
        """ Возвращает атрибут name. """

        return f'{self._language}'
