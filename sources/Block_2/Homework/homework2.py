import os

from utils import load_students, load_professions

# имя дирректории с JSON файлами
DIRRECTORY = 'homework2_data'


def get_student_by_pk(pk):
    '''
    По номеру студента получает список с описанием студентов и
    возвращает словарь с описанием выбранного студента или None
    если студента с таким номером не найдено
    '''
    students_list = load_students(os.path.join(DIRRECTORY, 'students.json'))
    for student in students_list:
        if student.get('pk') == str(pk):
            return student
            break
    else:
        return None


def get_profession_by_title(title):
    '''
    По названию специальности получает список с описанием профессий
    возвращает словарь с описанием выбранной профессии или None
    если профессии с таким названием не найдено
    '''
    professions_list = load_professions(os.path.join(DIRRECTORY, 'professions.json'))
    for professions in professions_list:
        if professions.get('title') == str(title):
            return professions
            break
    else:
        return None


def get_suitability(student_info, skills_info):
    student_skills = set(student_info['skills'])
    professions_skills = set(skills_info['skills'])
    has = list(student_skills.intersection(professions_skills))
    like = list(professions_skills.difference(student_skills))
    percentage = len(has) / len(professions_skills) * 100
    return percentage, has, like


def _student_full_name(student_info):
    '''
    Вернуть значение для ключа full_name
    '''
    return student_info['full_name']


def _student_skills(student_info):
    '''
    Вернуть строку с навыками студента
    '''
    return " ".join(student_info['skills'])


def _speciality_title(speciality_info):
    '''
    Вернуть название специальности
    '''
    return speciality_info['title']

def main():
    '''
    Функция запрашивает код студента и название специальности и выводит наличие/отсутствие необходимых
    навыков. А также расчитывает процент пригодности
    '''
    # Выбрать информацию о студенте
    student_number = input("Введите номер студента: ")
    student = get_student_by_pk(pk=student_number)
    if student is None:
        print("У нас нет такого студента")
        return None
    print(f"Студент {_student_full_name(student)}")
    print(f"Знает {_student_skills(student)}")

    # Выбрать информацию о специальности
    student_speciality = input(f"Выберите специальность для оценки студента {_student_full_name(student)}: ")
    speciality = get_profession_by_title(title=student_speciality)
    if speciality is None:
        print("У нас нет такой специальности")
        return None
    print(f"{_speciality_title(speciality)}")

    student_suitability, known, unknown = get_suitability(student_info=student, skills_info=speciality)
    skills_known = " ".join(known)
    skills_unknown = " ".join(unknown)
    print(f"Пригодность {student_suitability}%")
    print(f"{_student_full_name(student)} знает {skills_known}")
    print(f"{_student_full_name(student)} не знает {skills_unknown}")


if __name__ == '__main__':
    main()
