USER_GREETINGS = '''Привет! Предлагаю проверить свои знания английского!
Напиши, как тебя зовут.'''

ALL_QUESTIONS_COUNTER = 3

CORRECT_ANSWER_SCORE = 10

QUESTION_1 = "My name ___ Vova."
ANSWER_1 = "is"
QUESTION_2 = "I ___ a coder."
ANSWER_2 = "am"
QUESTION_3 = "I live ___ Moscow."
ANSWER_3 = "in"

# баллы за ответы
score_correct_answers = 0
# верные ответы
correct_answers = 0
# процент верных ответов
correct_answers_percent = 0
# ответ пользователя
user_answer = ""

# получаем имя пользователя
user_name = str(input(USER_GREETINGS))

print(f"Привет, {user_name}, начинаем тренировку!")

# блок вопросы - ответы
# ---------- первый вопрос -----
user_answer = str(input(QUESTION_1))

if user_answer == ANSWER_1:
    correct_answers += 1
    print("Ответ верный!", f"Вы получаете {CORRECT_ANSWER_SCORE} баллов!", sep="\n")
else:
    print("Неправильно.", f"Правильный ответ: {ANSWER_1}", sep="\n")
# ------------------------------

# ---------- второй вопрос -----
user_answer = str(input(QUESTION_2))
if user_answer == ANSWER_2:
    correct_answers += 1
    print("Ответ верный!", f"Вы получаете {CORRECT_ANSWER_SCORE} баллов!", sep="\n")
else:
    print("Неправильно.", f"Правильный ответ: {ANSWER_2}", sep="\n")
# ------------------------------

# ---------- третий вопрос -----
user_answer = str(input(QUESTION_3))
if user_answer == ANSWER_3:
    correct_answers += 1
    print("Ответ верный!", f"Вы получаете {CORRECT_ANSWER_SCORE} баллов!", sep="\n")
else:
    print("Неправильно.", f"Правильный ответ: {ANSWER_3}", sep="\n")
# ------------------------------

# вычисление процентов и баллов
score_correct_answers = correct_answers * CORRECT_ANSWER_SCORE
correct_answers_percent = round(correct_answers / ALL_QUESTIONS_COUNTER * 100)

# подведение итогов
print(f"Вот и всё, {user_name}!",
      f"Вы ответили на {correct_answers} вопросов из {ALL_QUESTIONS_COUNTER} верно.",
      f"Вы заработали {score_correct_answers} баллов.",
      f"Это {correct_answers_percent} процентов.", sep="\n")
