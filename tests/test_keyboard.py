def test_init(test_obj_keyboard):
    assert test_obj_keyboard.name == "Dark Project KD87A"
    assert test_obj_keyboard._language == "EN"


def test_change_lang(test_obj_keyboard):
    assert test_obj_keyboard._language == "EN"
    test_obj_keyboard.change_lang()
    assert test_obj_keyboard._language == "RU"
    test_obj_keyboard.change_lang()
    assert test_obj_keyboard._language == "EN"


def test_language(test_obj_keyboard):
    assert test_obj_keyboard.language == "EN"
