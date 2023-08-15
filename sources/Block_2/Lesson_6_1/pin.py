def check_pin(pin_code):
    if len(pin_code) == 4 and pin_code.isdigit():
        return True
    return False


def test_check_pin():
    assert check_pin("1234")
    assert not check_pin("123")
    assert not check_pin("a000")
    assert check_pin("0000")


print("Печатается всегда - pin.py")


if __name__ == "__main__":
    print("Печатается только при запуске pin.py")
    try:
        assert check_pin("1234")
        assert not check_pin("123")
        assert not check_pin("a000")
        assert check_pin("0000")
    except AssertionError:
        print("Неверно, проверьте функцию на разных значениях")
    else:
        print("Все хорошо, все работает")