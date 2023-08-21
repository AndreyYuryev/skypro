class Player:
    def __init__(self, user_name):
        '''инициализация параметров пользователя'''
        self.user_name = user_name
        self.user_words = []

    def __repr__(self):
        '''представление объекта игрок'''
        words = ', '.join(self.user_words)
        return f"Игрок {self.user_name}. Угаданные слова: {words}"

    def add_guessed_word(self, user_word):
        '''добавить слово в список успешных попыток'''
        self.user_words.append(user_word)

    def is_already_guessed(self, user_word):
        '''проверяет угадоно ли уже слово'''
        return user_word in self.user_words

    def already_guessed(self):
        '''возвращает количество угаданных слов'''
        return len(self.user_words)

    def get_statistic(self):
        '''возвращает статистику'''
        guessed = self.already_guessed()
        return f"вы угадали {guessed} {self._get_number_digit(guessed, add_one='слово', add_two='слова', add_ten='слов')}"

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
