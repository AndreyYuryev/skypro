import random

words = ["code", "bit", "list", "soul", "next"]

MORSE_CODES = {
    "0": "-----",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
    "a": ".-",
    "b": "-...",
    "c": "-.-.",
    "d": "-..",
    "e": ".",
    "f": "..-.",
    "g": "--.",
    "h": "....",
    "i": "..",
    "j": ".---",
    "k": "-.-",
    "l": ".-..",
    "m": "--",
    "n": "-.",
    "o": "---",
    "p": ".--.",
    "q": "--.-",
    "r": ".-.",
    "s": "...",
    "t": "-",
    "u": "..-",
    "v": "...-",
    "w": ".--",
    "x": "-..-",
    "y": "-.--",
    "z": "--..",
    ".": ".-.-.-",
    ",": "--..--",
    "?": "..--..",
    "!": "-.-.--",
    "-": "-....-",
    "/": "-..-.",
    "@": ".--.-.",
    "(": "-.--.",
    ")": "-.--.-"}

answers = []


def morse_encode(word="a"):
    """
    переводит слова на английском языке в последовательности точек и тирe.
    :param word: Исходное слово
    :return: строка морзянки
    """

    word_encoded = []

    for letter in word:
        word_encoded.append(MORSE_CODES.get(letter, ""))

    return " ".join(word_encoded)


def get_word():
    """
      получает случайное слово из списка.
    :return: строка слова
    """
    z = random.choices(words, k=2)
    return z


def print_statistics(answers):
    """
    на основе списка answers типа [True, False, False, True, False] выводит статистику
    :param answers: список верности ответов
    """

    answers_total = len(answers)
    answers_correct = sum(answers)
    answers_incorrect = answers_total - answers_correct

    print(f"Всего задачек: {answers_total}\n"
          f"Отвечено верно:{answers_correct}\n"
          f"Отвечено неверно:{answers_incorrect}\n")


def main():
    print("Сегодня мы потренируемся расшифровывать азбуку Морзе")
    print("Нажмите Enter и начнем")
    input()

    for i in range(1, len(words) + 1):

        current_word = get_word()
        current_encoded = morse_encode(current_word)

        print(f"Слово {i} {current_encoded}")

        user_input = input()

        if user_input.lower() == current_word[0]:
            print(f"Верно, {current_word[0]}!")
            answers.append(True)

        else:
            print(f"Неверно, {current_word[0]}!")
            answers.append(False)

    print_statistics(answers)


main()
