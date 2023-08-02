# словарь с результатами
user_data = {'level': '',
             True: [],
             False: []
             }

words_easy = {
    "family": "семья",
    "hand": "рука",
    "people": "люди",
    "evening": "вечер",
    "minute": "минута",
}

words_medium = {
    "believe": "верить",
    "feel": "чувствовать",
    "make": "делать",
    "open": "открывать",
    "think": "думать",
}

words_hard = {
    "rural": "деревенский",
    "fortune": "удача",
    "exercise": "упражнение",
    "suggest": "предлагать",
    "except": "кроме",
}

levels = {
    0: "Нулевой",
    1: "Так себе",
    2: "Можно лучше",
    3: "Норм",
    4: "Хорошо",
    5: "Отлично",
}

# выбор уровня сложности
print("Выберите уровень сложности.")
std_input = input("Легкий, средний, сложный. ")
user_data['level'] = std_input.lower()

if user_data['level'] in ['легкий', 'средний', 'сложный']:
    # вывод уровня сложности
    print(f"Выбран уровень сложности {user_data['level']}, мы предложим 5 слов, подберите перевод.")
    std_input = input("Нажмите Enter. ")

    # создание рабочего словаря копированием
    if user_data['level'] == "легкий":
        words = words_easy.copy()
    elif user_data['level'] == "средний":
        words = words_medium.copy()
    elif user_data['level'] == "сложный":
        words = words_hard.copy()

    # цикл угадывания слов
    for key, value in words.items():
        first_letter = value[0]
        std_input = input(f"{key}, {len(value)} букв, начинается на {first_letter}...")
        if std_input == value:
            print(f"Верно, {key} — это {value}.")
            user_data[True].append(key)
        else:
            print(f"Неверно. {key} — это {value}.")
            user_data[False].append(key)

    # вывод статистики
    print("Правильно отвечены слова: ")
    for value in user_data[True]:
        print(value)
    print("Неправильно отвечены слова: ")
    for value in user_data[False]:
        print(value)
    print("Ваш ранг: ")
    print(levels[len(user_data[True])])

else:
    print("Уровень не выбран. Вы не хотите поиграть.")
