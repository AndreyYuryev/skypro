import requests
import json

response = requests.get(url='https://jsonkeeper.com/b/LJHI', verify=False)

data = response.json()
print(data)
