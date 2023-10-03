import urllib.request
import json
import ast
request = urllib.request.urlopen('http://127.0.0.1:8000/accounts/test_api/')
var = request.read().str()
# request_data = json.loads(var)
print(var)
# print(*request.__dir__(), sep='\n')