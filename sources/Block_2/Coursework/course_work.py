from utils import load_random_word
from basic import BasicWord
from player import Player

URL_JSON = 'https://jsonkeeper.com/b/LJHI'


def main():
    ''' Получаем слово и его анаграммы, пытаемся угадать все'''

    # получение имени пользователя
    player = Player(input("Введите имя пользователя:"))
    print(f"Привет, {player.user_name}")

    word_list = load_random_word(URL_JSON)
    word = BasicWord(word=word_list.get('word'), anagrams=word_list.get('subwords'))
    if word.is_empty():
        print("Слово не загрузилось")
        return

    print(f"Составьте {word.count_words()} слов из слова '{word.word}'")
    # print(repr(word))
    print(f"Слова должны быть не короче 3 букв")
    print(f"Чтобы закончить игру угадайте все слова или напишите 'стоп'")
    print("Поехали, ваше первое слово?")
    while True:
        user_word = input()
        if user_word == 'стоп':
            print("Статистика:")
            break
        if len(user_word) < 3:
            print("слишком короткое слово")
            continue
        if not word.is_correct(user_word=user_word):
            print("неверно")
            continue
        if player.is_already_guessed(user_word=user_word):
            print("уже использовано")
            continue
        print("верно")
        player.add_guessed_word(user_word=user_word)
        if player.already_guessed() == word.count_words():
            break
    print(f"Игра завершена, {player.get_statistic()}")


if __name__ == '__main__':
    main()
