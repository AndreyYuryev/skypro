from Lesson_8_2_13_3.data_manager import load_data


def get_statistics():
    ''' Вернуть длину списка'''
    data = load_data()
    return len(data)
