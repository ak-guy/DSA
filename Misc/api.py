import urllib.request
import json
import ast
import requests
import time
# request = urllib.request.urlopen('http://127.0.0.1:8000/accounts/test_api/')
count = 0
# time_now = time.time
# print(time.__dir__())

# while True:
#     request = requests.get('http://127.0.0.1:8000/accounts/test_api/')
#     print(request.status_code)
#     count += 1
#     print(count)
# # var = request.read().str()
# # request_data = json.loads(var)
# # print(type(request.json()))
# # print(type(request.content))

# # print(*request.__dir__(), sep='\n')

request = requests.get('https://realpython.com/python-gil/')
# print(request.__dir__())

txt = request
print(txt)