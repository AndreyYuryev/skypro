import json
import random

QUESTIONS_FILE = 'questions.json'


class Questioner:
    def __init__(self, filename):
        self._greetings()
        self.questions = self._prepare_questions(filename)

    def _greetings(self):
        '''
        вывести приветствие
        '''
        print("Игра начинается!")

    def _prepare_questions(self, filename):
        '''
        Возвращает перемешанный список объектов типа вопрос
        '''
        questions = []
        question_list = self._load_questions(filename)
        for question in question_list:
            questions.append(Question(question['q'], question['a'], question['d']))
        random.shuffle(questions)
        return questions

    def _load_questions(self, filename='questions.json'):
        '''
        Читает из файла JSON с описанием вопросов и возвращает в виде словаря
        '''
        with open(file=filename, encoding='utf-8', mode='r') as file:
            questions_data = json.load(file)
        return questions_data

    def print_statistic(self):
        '''
        распечатать статистику
        '''
        print("Вот и все!")
        asked = 0
        score = 0
        correct_answer = 0
        for question in self.questions:
            if question.asked:
                asked += 1
            if question.correct_answer:
                correct_answer += 1
                score += question.get_points()
        print(f"Отвечено {correct_answer} вопроса из {asked}")
        print(f"Набранно {score} баллов")

    def ask(self):
        '''
        Задает вопрос и обрабатывает ответы
        '''
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
    questioner = Questioner(QUESTIONS_FILE)
    questioner.ask()
    questioner.print_statistic()


if __name__ == '__main__':
    main()
