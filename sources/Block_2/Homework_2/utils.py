import json


def load_students(filename='students.json'):
    '''
    Читает из файла JSON с описанием студентов и возвращает в виде словаря
    '''
    with open(file=filename, encoding='utf-8', mode='r') as file:
        students_data = json.load(file)
    return students_data


def load_professions(filename='professions.json'):
    '''
    Читает из файла JSON с описанием профессий и возвращает в виде словаря
    '''
    with open(file=filename, encoding='utf-8', mode='r') as file:
        professions_data = json.load(file)
    return professions_data