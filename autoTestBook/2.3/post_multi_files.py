#-*-coding:utf-8-*-
import requests,json
url  = 'http://httpbin.org/post'
multiple_files = [('images', ('test1.png', 'test1.png', 'rb'), 'impage/png'), ('images', ('test1.png', 'test2.png', 'rb'), 'impage/png')]
response = requests.post(url, files=multiple_files)
print(response.text)