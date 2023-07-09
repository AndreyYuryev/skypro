import random


MORSE = {
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
  ")": "-.--.-"
}

def morse_encode(in_word='test'):
    '''Функция кодирования полученного слова при помощи словаря morse.
    Возвращает строку кодов разделелнных пробелом'''
    out_code = list()
    for letter in in_word:
        code = MORSE[letter]
        out_code.append(code)
    return str(" ".join(out_code))


def morse_decode(in_code='- . ... -'):
    '''Функция декодирования полученного кодоа в виде строки с разделителями пробелами
    при помощи словаря morse. Возвращает строку'''
    out_word = str()
    in_code_list = in_code.split()
    for code_word in in_code_list:
        for key, item in MORSE.items():
            if code_word == item:
                out_word += key
    return out_word


def get_random_word(in_words):
    '''Функция возвращает случайное слово из списка words'''
    return random.choice(in_words)


def print_answers(in_answers):
    '''Функция на основе списка верных/неверных ответов печатает статистику'''
    correct_answer = 0
    wrong_answer = 0
    for item in in_answers:
        if item:
            correct_answer += 1
        else:
            wrong_answer += 1
    print("-------------------------")
    print(f"Всего задач: {len(in_answers)}",
          f"Отвечено верно: {correct_answer}",
          f"Отвечено неверно: {wrong_answer}", sep="\n")


def create_words_list():
    '''Функция создает список из 5 слов коды которых известны пользователю'''
    words = list()
    for word_counter in range(5):
        user_word = input("Введите слово: ").lower()
        words.append(user_word)
    return words

def main():
    '''Основная программа'''
    # words = ["test", "andrey", "word", "help", "pen"]
    answers = list()
    words = list()

    user_input = input(f"Сегодня мы потренируемся расшифровывать азбуку Морзе.\nНажмите Enter и начнем")

    # создать список из 5 слов коды которых известны пользователю
    words = create_words_list()

    # Угадываем слова
    for attempt in range(len(words)):
        word = get_random_word(words)
        code = morse_encode(word)
        print(f"Слово {attempt + 1}: ", code)
        user_answer = input()
        if user_answer == word:
            print(f"Верно: {word}!")
            answers.append(True)
        else:
            print(f"Неверно: {word}!")
            answers.append(False)

    # вывести статистику
    print_answers(answers)

    user_code = input("Введите код: ")
    word = morse_decode(user_code)
    print(word)

if __name__ == '__main__':
    main()

