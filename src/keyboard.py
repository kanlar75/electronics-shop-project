from src.item import Item


class MixinLayout:
    layout = "EN"

    def change_lang(self):
        """ Метод для изменения языка (раскладки клавиатуры). """

        if self.layout == "EN":
            self._language = "RU"
        else:
            self._language = "EN"
        MixinLayout.layout = self._language
        return self

class KeyBoard(Item, MixinLayout):

    def __init__(self, name: str, price: float, quantity: int):
        super().__init__(name, price, quantity)
        self._language = MixinLayout.layout

    @property
    def language(self):
        """ Возвращает атрибут language. """

        return f'{self._language}'
