import urllib.request
import json
import ast
import requests
# request = urllib.request.urlopen('http://127.0.0.1:8000/accounts/test_api/')
request = requests.get('http://127.0.0.1:8000/accounts/test_api/')
# var = request.read().str()
# request_data = json.loads(var)
print(type(request.json()))
print(type(request.content))

# print(*request.__dir__(), sep='\n')