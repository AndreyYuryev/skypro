def is_palindrome(word):
    word_str = "".join(word.lower().split())
    word_list = []
    word_list = list(word_str)
    if word_list == list(reversed(word_list)):
        return True
    return False


def test_level():
    assert is_palindrome("leve l")


def test_saagas():
    assert is_palindrome("s a ga s")


def test_hero():
    assert not is_palindrome("hero")


def test_drama():
    assert not is_palindrome("drama")


def test_Level():
    assert is_palindrome("Level")


def test_levels_wrong():
    '''
    Тестовый случай levels
    '''
    assert not is_palindrome('levels')
