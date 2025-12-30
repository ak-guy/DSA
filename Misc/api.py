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
# ['_content', '_content_consumed', '_next', 'status_code', 'headers', 'raw', 'url', 'encoding', 'history', 'reason', 'cookies', 'elapsed', 'request', 'connection', '__module__', '__doc__', '__attrs__', '__init__', '__enter__', '__exit__', '__getstate__', '__setstate__', '__repr__', '__bool__', '__nonzero__', '__iter__', 'ok', 'is_redirect', 'is_permanent_redirect', 'next', 'apparent_encoding', 'iter_content', 'iter_lines', 'content', 'text', 'json', 'links', 'raise_for_status', 'close', '__dict__', '__weakref__', '__new__', '__hash__', '__str__', '__getattribute__', '__setattr__', '__delattr__', '__lt__', '__le__', '__eq__', '__ne__', '__gt__', '__ge__', '__reduce_ex__', '__reduce__', '__subclasshook__', '__init_subclass__', '__format__', '__sizeof__', '__dir__', '__class__']
request = requests.get(
    "https://leetcode.com/problems/reverse-words-in-a-string-ii/description/"
)
# print(request.__dir__())

print(request.json)
