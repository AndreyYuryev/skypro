import json
import random
import os

QUESTIONS_FILE = 'questions.json'


def print_statistic(questions):
    '''
    распечатать статистику на основе списка объектов
    '''
    if not questions:
        return
    print("Вот и все!")
    asked = 0
    score = 0
    correct_answer = 0
    for question in questions:
        if question.asked:
            asked += 1
        if question.correct_answer:
            correct_answer += 1
            score += question.get_points()
    print(f"Отвечено {correct_answer} вопроса из {asked}")
    print(f"Набранно {score} баллов")


def prepare_questions(filename='questions.json'):
    '''
    Возвращает перемешанный список объектов типа вопрос
    '''
    questions = []
    question_list = load_questions(filename)
    if question_list is not None:
        for question in question_list:
            questions.append(Question(question['q'], question['a'], question['d']))
        random.shuffle(questions)
    return questions


def load_questions(filename='questions.json'):
    '''
    Читает из файла JSON с описанием вопросов и возвращает в виде словаря
    '''
    if os.path.exists(filename):
        with open(file=filename, encoding='utf-8', mode='r') as file:
            questions_data = json.load(file)
        return questions_data


class Questioner:
    def __init__(self, questions):
        self._greetings()
        self.questions = questions

    def _greetings(self):
        '''
        вывести приветствие
        '''
        print("Игра начинается!")

    def _question_list_empty(self):
        '''
        Список вопросов пустой
        '''
        print("Список вопросов пуст, проверьте файл с вопросами")

    def ask(self):
        '''
        Задает вопрос и обрабатывает ответы
        '''
        if not self.questions:
            self._question_list_empty()
        else:
            for question in self.questions:
                print(question.build_question())
                print(question.build_feedback(input()))


class Question:
    '''
    Класс содержит вопрос, ответ и сложность
    '''

    def __init__(self, q, a, d):
        self.question = q
        self.answer = a
        self.difficulty = d
        self.score = int(d) * 10
        self.asked = False
        self.user_answer = None
        self.correct_answer = False

    def get_points(self):
        '''
        Возвращает int, количество баллов.
        Баллы зависят от сложности: за 1 дается 10 баллов, за 5 дается 50 баллов.
        '''
        return int(self.difficulty) * 10

    def is_correct(self, user_answer):
        '''
        Возвращает True, если ответ пользователя совпадает
        с верным ответов иначе False.
        '''
        self.asked = True
        self.user_answer = user_answer
        if self.answer.lower() == self.user_answer.lower():
            self.correct_answer = True
        return self.correct_answer

    def build_question(self):
        '''
        Возвращает вопрос в понятном пользователю виде, например:
        Вопрос: What do people often call American flag?
        Сложность 4/5
        '''
        return f"Вопрос: {self.question}\nСложность: {self.difficulty}/5"

    def build_feedback(self, user_answer):
        '''Возвращает :
        Ответ верный, получено __ баллов
        Возвращает :
        Ответ неверный, верный ответ __
        '''
        if self.is_correct(user_answer):
            return f"Ответ верный, получено {self.get_points()} баллов"
        return f"Ответ неверный. Верный ответ - {self.answer}"


def main():
    '''
    основной алгоритм вопросов - ответов
    '''
    questioner = Questioner(prepare_questions(QUESTIONS_FILE))
    questioner.ask()
    print_statistic(questioner.questions)


if __name__ == '__main__':
    main()
