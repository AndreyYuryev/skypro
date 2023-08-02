import random


def get_words(filename='words.txt'):
    '''
    Возвращает список слов полученный из файла
    '''
    words = []
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            words.append(line.strip())
    return words


def get_random_word(word_list):
    '''
    Возвращает слово выбранное случайным образом из списка
    '''
    return random.choice(word_list)


def get_mixed_word(in_word):
    '''
    Меняет местами буквы в слове
    '''
    word_list = list(in_word)
    random.shuffle(word_list)
    return "".join(word_list)


def get_players(filename='history.txt'):
    '''
    Функция возвращает список игроков с количеством игр и количеством набранных очков
    в виде словаря
    формат:  Имя: [количество игр, максимальное количество очков за игру]
    '''
    players_list = {}
    line_list = []
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            line_list = line.strip().split(':')
            players_list[line_list[0]] = [int(line_list[1]), int(line_list[2])]
    return players_list


def set_players(filename='history.txt', players_list={}):
    '''
    Сохраняет топ игроков в файл
    Имя игрока:количество игр:максимальное количество очков
    '''
    with open(filename, 'w', encoding='utf-8') as file:
        for keys, value in players_list.items():
            file.write(f"{keys}:{value[0]}:{value[1]}\n")


def main():
    '''
    Основная программа
    '''
    # список результатов игроков
    players = get_players()
    # список слов
    words = get_words()

    user_name = input("Введите ваше имя: ")

    # результаты игрока ранее
    top_scores, games = players.get(user_name, [0, 0])
    score_counter = 0

    # блок угадывания слов
    for attempt in range(len(words)):
        word = get_random_word(words)
        user_answer = input(f"Угадайте слово: {get_mixed_word(word)}: ")
        if user_answer == word:
            print("Верно! Вы получаете 10 очков.")
            score_counter += 10
        else:
            print(f"Неверно! Верный ответ – {word}.")

    # запись в топ игроков
    if int(top_scores) < score_counter:
        players[user_name] = [int(score_counter), int(games) + 1]
    else:
        players[user_name] = [int(top_scores), int(games) + 1]

    set_players(players_list=dict(sorted(players.items(), key=lambda x: x[1], reverse=True)))

    # вывод топа игроков
    print("-- Top players --")
    for key, value in players.items():
        print(f"Игрок {key}: очков - {value[0]}")


if __name__ == '__main__':
    main()
