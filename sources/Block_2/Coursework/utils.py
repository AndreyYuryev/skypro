import requests
import json
import urllib3
import random


def load_random_word(url='https://jsonkeeper.com/b/LJHI', jsonkeeper=False):
    '''
    считать список слов из внешнего ресурса и вернуть словарь для создания объекта BasicWord
    '''
    if jsonkeeper == True:
        urllib3.disable_warnings()
        response = requests.get(url=url, verify=False)
    else:
        response = requests.get(url=url)
    words_list = []
    if response.status_code == 200:
        data = response.json()
        # for item in data:
        #     words_list.append(BasicWord(item['word'], item['subwords']))
        return random.choice(data)
