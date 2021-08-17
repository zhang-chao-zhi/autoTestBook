# -*- coding: utf-8 -*-
from urllib import request

from http import cookiejar

url = 'http://www.soso.com'

# 创建一个cookiejar对象
cookie = cookiejar.CookieJar()

# 使用HTTPCookieProcessor创建cookie处理器
cookies = request.HTTPCookieProcessor(cookie)

# 以它为参数创建Opener对象
opener = request.build_opener(cookies)

# 发起带cookie的请求
response = opener.open(url)

for i in cookie:
    print(i)
