import requests
import json
import urllib3


class BasicWord:
    pass


class Player:
    pass


def load_random_word(url='https://jsonkeeper.com/b/LJHI'):
    '''
    считать список слов из внешнего ресурса и вернуть объект типа BasicWord
    '''
    urllib3.disable_warnings()
    response = requests.get(url=url, verify=False)
    if response.status_code == 200:
        data = response.json()
        return BasicWord()
