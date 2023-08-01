def is_palindrome(word):
    word_str = "".join(word.lower().split())
    word_list = []
    word_list = list(word_str)
    if word_list == list(reversed(word_list)):
        return True
    return False


def test_is_palindrome():
    assert is_palindrome("leve l")
    assert is_palindrome("s a ga s")
    assert not is_palindrome("hero")
    assert not is_palindrome("drama")
    assert is_palindrome("Level")

