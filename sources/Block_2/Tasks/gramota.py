import requests
import json
import pprint
import urllib3

urllib3.disable_warnings()
response = requests.get(url='https://jsonkeeper.com/b/LJHI', verify=False)

data = response.json()
pp = pprint.PrettyPrinter(indent=4)
pp.pprint(data)
