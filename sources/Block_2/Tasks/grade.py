grades = {2: "Плохо",
          3: "Удовлетворительно",
          4: "Хорошо",
          5: "Отлично"}


def get_grade(grade):
    if grade in grades:
        return grades[grade]
    else:
        return "Ошибка"


def test_get_grade():
    assert get_grade(2) == "Плохо"
    assert get_grade(3) == "Удовлетворительно"
    assert get_grade(4) == "Хорошо"
    assert get_grade(5) == "Отлично"
    assert get_grade("") == "Ошибка"
    assert get_grade(1) == "Ошибка"
    assert get_grade('Z') == "Ошибка"