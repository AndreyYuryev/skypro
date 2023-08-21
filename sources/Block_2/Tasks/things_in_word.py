class Numbers:
    def __init__(self, digit_number, one_thing="слово", two_thing='слова', ten_thing='слов'):
        self.digit_number = int(digit_number) % 1000
        self.thing_word = self._get_number_digit(digit_number=self.digit_number, add_one=one_thing, add_two=two_thing,
                                                 add_ten=ten_thing)

    def __str__(self):
        return f"{self.digit_number} {self.thing_word}"

    def _get_number_digit(self, digit_number, add_one, add_two, add_ten):
        ''' Атрибуты: digit_number - число из 3х разрядов которое разбираем, например: 124
        add_one - это обозначение слова для 1,21,31 и далее кратно 10 штуки
        add_two - обозначение слова для 2,3,4 штук
        add_ten - обозначени слов для остальных случаев
        digit_gender - обозначение рода числа, для правильного вывода 1 или 2 и кратных им'''

        # промежуточная переменная для хранения числа прописью
        temp_digit = ""
        # добавка к числу
        digit_addition_one = add_one
        digit_addition_two = add_two
        digit_addition_ten = add_ten
        is_one = False
        is_two = False

        if 1 <= digit_number <= 999:
            # десятки и единицы
            digit_remainder = digit_number % 100
            if 20 <= digit_remainder <= 99:
                digit_ten_remainder = digit_remainder % 10
                if digit_ten_remainder == 1:
                    is_one = True
                elif digit_ten_remainder == 2:
                    is_two = True
                elif digit_ten_remainder == 3:
                    is_two = True
                elif digit_ten_remainder == 4:
                    is_two = True
            elif digit_remainder == 1:
                is_one = True
            elif digit_remainder == 2:
                is_two = True
            elif digit_remainder == 3:
                is_two = True
            elif digit_remainder == 4:
                is_two = True
            if is_one:
                temp_digit += digit_addition_one
            elif is_two:
                temp_digit += digit_addition_two
            else:
                temp_digit += digit_addition_ten
        return temp_digit
