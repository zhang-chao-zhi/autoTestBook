# -*- coding: utf-8 -*-
from urllib import request,parse

url = 'http://httpbin.org/post'

data = bytes(parse.urlencode({'star': 'Kobe', 'wish': 'God want to see the star plays basketball in the heaven.'}), encoding='utf8')

response = request.urlopen(url, data=data)
print(response.read().decode('utf-8'))
