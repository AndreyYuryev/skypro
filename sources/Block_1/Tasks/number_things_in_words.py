ZERO = "ноль"
ONE_M = "один"
ONE_F = "одна"
ONE_N = "одно"
TWO_M = "два"
TWO_F = "две"
TWO_N = "два"
TREE = "три"
FOUR = "четыре"
FIVE = "пять"
SIX = "шесть"
SEVEN = "семь"
EIGHT = "восемь"
NINE = "девять"
TEN = "десять"
ELEVEN = "одиннадцать"
TWELVE = "двенадцать"
THIRTEEN = "тринадцать"
FOURTEEN = "четырнадцать"
FIFTEEN = "пятнадцать"
SIXTEEN = "шестнадцать"
SEVENTEEN = "семнадцать"
EIGHTEEN = "восемнадцать"
NINETEEN = "девятнадцать"
TWENTY = "двадцать"
THIRTY = "тридцать"
FOURTY = "сорок"
FIFTY = "пятьдесят"
SIXTY = "шестьдесят"
SEVENTY = "семьдесят"
EIGHTY = "восемьдесят"
NINETY = "девяносто"
THOUSAND_ONE = "тысяча"
THOUSAND_TWO = "тысячи"
THOUSAND_TEN = "тысяч"
MILLION_ONE = "миллион"
MILLION_TWO = "миллиона"
MILLION_TEN = "миллионов"
BILLION_ONE = "миллиард"
BILLION_TWO = "миллиарда"
BILLION_TEN = "миллиардов"
TRILLION_ONE = "триллион"
TRILLION_TWO = "триллиона"
TRILLION_TEN = "триллионов"
HUNDRED = "сто"
TWO_HUNDRED = "двести"
TREE_FOUR_HUNDRED = "ста"
HUNDREDS = "сот"


def get_number_digit(digit_number, add_one="", add_two="", add_ten="", digit_gender="M"):
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
        # сотни
        digit_remainder = digit // 100
        if digit_remainder == 1:
            temp_digit += HUNDRED
        elif digit_remainder == 2:
            temp_digit += TWO_HUNDRED
        elif digit_remainder == 3:
            temp_digit += TREE
            temp_digit += TREE_FOUR_HUNDRED
        elif digit_remainder == 4:
            temp_digit += FOUR
            temp_digit += TREE_FOUR_HUNDRED
        elif 5 <= digit_remainder <= 9:
            if digit_remainder == 5:
                temp_digit += FIVE
            elif digit_remainder == 6:
                temp_digit += SIX
            elif digit_remainder == 7:
                temp_digit += SEVEN
            elif digit_remainder == 8:
                temp_digit += EIGHT
            elif digit_remainder == 9:
                temp_digit += NINE
            temp_digit += HUNDREDS
        if bool(temp_digit):
            temp_digit += " "

        # десятки и единицы
        digit_remainder = digit % 100
        if 20 <= digit_remainder <= 99:
            digit_ten = digit_remainder // 10
            digit_ten_remainder = digit_remainder % 10
            if digit_ten == 2:
                temp_digit += TWENTY
            elif digit_ten == 3:
                temp_digit += THIRTY
            elif digit_ten == 4:
                temp_digit += FOURTY
            elif digit_ten == 5:
                temp_digit += FIFTY
            elif digit_ten == 6:
                temp_digit += SIXTY
            elif digit_ten == 7:
                temp_digit += SEVENTY
            elif digit_ten == 8:
                temp_digit += EIGHTY
            elif digit_ten == 9:
                temp_digit += NINETY
            #
            if digit_ten_remainder > 0:
                temp_digit += " "
            #
            if digit_ten_remainder == 1:
                if digit_gender == "M":
                    temp_digit += ONE_M
                elif digit_gender == "F":
                    temp_digit += ONE_F
                else:
                    temp_digit += ONE_N
                is_one = True
            elif digit_ten_remainder == 2:
                if digit_gender == "M":
                    temp_digit += TWO_M
                elif digit_gender == "F":
                    temp_digit += TWO_F
                else:
                    temp_digit += TWO_N
                is_two = True
            elif digit_ten_remainder == 3:
                temp_digit += TREE
                is_two = True
            elif digit_ten_remainder == 4:
                temp_digit += FOUR
                is_two = True
            elif digit_ten_remainder == 5:
                temp_digit += FIVE
            elif digit_ten_remainder == 6:
                temp_digit += SIX
            elif digit_ten_remainder == 7:
                temp_digit += SEVEN
            elif digit_ten_remainder == 8:
                temp_digit += EIGHT
            elif digit_ten_remainder == 9:
                temp_digit += NINE
        elif digit_remainder == 1:
            if digit_gender == "M":
                temp_digit += ONE_M
            elif digit_gender == "F":
                temp_digit += ONE_F
            else:
                temp_digit += ONE_N
            is_one = True
        elif digit_remainder == 2:
            if digit_gender == "M":
                temp_digit += TWO_M
            elif digit_gender == "F":
                temp_digit += TWO_F
            else:
                temp_digit += TWO_N
            is_two = True
        elif digit_remainder == 3:
            temp_digit += TREE
            is_two = True
        elif digit_remainder == 4:
            temp_digit += FOUR
            is_two = True
        elif digit_remainder == 5:
            temp_digit += FIVE
        elif digit_remainder == 6:
            temp_digit += SIX
        elif digit_remainder == 7:
            temp_digit += SEVEN
        elif digit_remainder == 8:
            temp_digit += EIGHT
        elif digit_remainder == 9:
            temp_digit += NINE
        elif digit_remainder == 10:
            temp_digit += TEN
        elif digit_remainder == 11:
            temp_digit += ELEVEN
        elif digit_remainder == 12:
            temp_digit += TWELVE
        elif digit_remainder == 13:
            temp_digit += THIRTEEN
        elif digit_remainder == 14:
            temp_digit += FIFTEEN
        elif digit_remainder == 15:
            temp_digit += FIFTEEN
        elif digit_remainder == 16:
            temp_digit += SIXTEEN
        elif digit_remainder == 17:
            temp_digit += SEVENTEEN
        elif digit_remainder == 18:
            temp_digit += EIGHTEEN
        elif digit_remainder == 19:
            temp_digit += NINETEEN
        temp_digit += " "
        if is_one:
            temp_digit += digit_addition_one
        elif is_two:
            temp_digit += digit_addition_two
        else:
            temp_digit += digit_addition_ten
    return temp_digit


print("Давайте напишем количество предметов прописью.",
      "Для этого необходимо написать как склоняется это число и",
      "какого оно рода: Мужского, Женского или Среднего.",
      "Например, яблоко - средний род, тутанхамон - мужской, чупакабра - женский", sep="\n")

print("Хорошо, начнем. Сначала вспомним как склоняется слово обозначающее предмет")
str_one_thing = input("Введите обозначение одного предмета. Например, 1 яблоко: 1 ")
str_two_thing = input("Введите обозначение двух предметов. Например, 2 яблока: 2 ")
str_ten_thing = input("Введите обозначение пяти предметов. Например, 5 яблок: 5 ")
str_gender = input("Введите число обозначающее род предмета 1 - мужской 2 - женский 3 - средний:_")
str_numbers = input("Введите целое число предметов от 0 до квадрилиона(1 и 15 нулей):_")

# разряды
result_out = ""
unit_digit = ""
thousand_digit = ""
million_digit = ""
billion_digit = ""
trillion_digit = ""

if int(str_gender) == 1:
    word_gender = "M"
elif int(str_gender) == 2:
    word_gender = "F"
elif int(str_gender) == 3:
    word_gender = "N"
else:
    print("Такого рода не существует")

if not str_numbers.isnumeric():
    print("Число не соответствует требованию")
else:
    int_numbers = int(str_numbers)
    if not 0 <= int_numbers <= 1000000000000000:
        print("Число не соответствует требованию")
    else:
        remainder = int_numbers
        if remainder == 0:
            unit_digit = ZERO
            unit_digit += " "
            unit_digit += str_ten_thing
            only_unit_digit = True
        else:
            only_unit_digit = False
            #  --- разряд
            digit = remainder % 1000
            #  --- остаток разрядов
            remainder = remainder // 1000
            #  --- класс единиц
            unit_digit = get_number_digit(digit, add_one=str_one_thing, add_two=str_two_thing, add_ten=str_ten_thing,
                                          digit_gender=word_gender)

        if remainder > 0:
            only_unit_digit = False
            #  --- разряд
            digit = remainder % 1000
            #  --- остаток разрядов
            remainder = remainder // 1000
            #  --- класс тысяч
            thousand_digit = get_number_digit(digit, THOUSAND_ONE, THOUSAND_TWO, THOUSAND_TEN, digit_gender="F")

            #  --- разряд
            digit = remainder % 1000
            #  --- остаток разрядов
            remainder = remainder // 1000
            #  --- класс миллионов
            million_digit = get_number_digit(digit, MILLION_ONE, MILLION_TWO, MILLION_TEN)

            #  --- разряд
            digit = remainder % 1000
            #  --- остаток разрядов
            remainder = remainder // 1000
            #  --- класс миллиардов
            billion_digit = get_number_digit(digit, BILLION_ONE, BILLION_TWO, BILLION_TEN)

            #  --- разряд
            digit = remainder % 1000
            #  --- остаток разрядов
            remainder = remainder // 1000
            #  --- класс триллионов
            trillion_digit = get_number_digit(digit, TRILLION_ONE, TRILLION_TWO, TRILLION_TEN)

    if only_unit_digit:
        # выводим только разряд единиц
        result_out = unit_digit
    else:
        # выводим все разряды если есть
        if bool(trillion_digit):
            result_out += trillion_digit
            result_out += " "
        if bool(billion_digit):
            result_out += billion_digit
            result_out += " "
        if bool(million_digit):
            result_out += million_digit
            result_out += " "
        if bool(thousand_digit):
            result_out += thousand_digit
            result_out += " "
        result_out += unit_digit

    # выводим полученный результат
    print(f"Заданное число предметов {str_numbers} пишется как: {result_out}")
