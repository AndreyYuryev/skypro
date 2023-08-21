import json


def load_data():
    ''' загрузить JSON '''
    with open("data_manager/data.json") as file:
        data = json.load(file)
    return data
