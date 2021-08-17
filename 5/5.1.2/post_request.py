# -*- coding: utf-8 -*-
from urllib import request

data = b'word=Wuhan&slogan=comeOn'
url = 'http://httpbin.org/post'

response = request.urlopen(url, data=data)
print(response.read().decode())