USER_GREETINGS = '''Привет! Предлагаю проверить свои знания английского!
Наберите "ready", чтобы начать!'''

USER_READY = "ready"

questions = ["My name ___ Vova.", "I ___ a coder.", "I live ___ Moscow."]
answers = ["is", "am", "in"]

# правильная форма слова
word_questions = ["вопрос", "вопроса", "вопросов"]
word_points = ["балл", "балла", "баллов"]
word_percent = ["процент", "процента", "процентов"]

# баллы за ответы
score_correct_answers = 0
# верные ответы
correct_answers = 0

# получаем согласие пользователя
is_user_ready = bool(input(USER_GREETINGS) == USER_READY)

if not is_user_ready:
    print("Кажется, вы не хотите играть. Очень жаль")
else:
    # блок вопросы - ответы
    for question_number, question in enumerate(questions):
        attempt = 3
        is_wrong_answer = False

        while attempt > 0:
            if is_wrong_answer:
                print(f"Осталось попыток: {attempt}, попробуйте еще раз!")

            # задаем вопрос
            user_answer = input(question)

            # проверяем корректность ответа и начисляем баллы
            if user_answer == answers[question_number]:
                print("Ответ верный!")
                correct_answers += 1
                score_correct_answers += attempt
                break
            else:
                attempt -= 1
                is_wrong_answer = True
        else:
            print(f"Увы, но нет. Верный ответ: {answers[question_number]}")

    # вычисление процентов
    correct_answers_percent = round(correct_answers / len(questions) * 100)

    # это дополнительный блок для правильного склонения слов

    # вычисление правильной формы слова
    if 20 < correct_answers < 100:
        if correct_answers % 10 == 1:
            question_index = 0
        elif 2 <= correct_answers % 10 <= 4:
            question_index = 1
        else:
            question_index = 2
    elif 5 <= correct_answers <= 20:
        question_index = 2
    elif 2 <= correct_answers <= 4:
        question_index = 1
    elif correct_answers == 1:
        question_index = 0
    else:
        question_index = 2

    if 20 < correct_answers_percent < 100:
        if correct_answers_percent % 10 == 1:
            percent_index = 0
        elif 2 <= correct_answers_percent % 10 <= 4:
            percent_index = 1
        else:
            percent_index = 2
    elif 5 <= correct_answers_percent <= 20:
        percent_index = 2
    elif 2 <= correct_answers_percent <= 4:
        percent_index = 1
    elif correct_answers_percent == 1:
        percent_index = 0
    else:
        percent_index = 2

    if 20 < score_correct_answers < 100:
        if score_correct_answers % 10 == 1:
            point_indexd = 0
        elif 2 <= score_correct_answers % 10 <= 4:
            point_index = 1
        else:
            point_index = 2
    elif 5 <= score_correct_answers <= 20:
        point_index = 2
    elif 2 <= score_correct_answers <= 4:
        point_index = 1
    elif score_correct_answers == 1:
        point_index = 0
    else:
        point_index = 2

    # подведение итогов
    print(f"Вот и всё!",
          f"Вы ответили на {correct_answers} {word_questions[question_index]} из {len(questions)} верно.",
          f"Вы набрали dd{score_correct_answers} {word_points[point_index]}.",
          f"Это {correct_answers_percent} {word_percent[percent_index]}.", sep="\n")
