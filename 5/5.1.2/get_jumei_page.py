# -*- coding: utf-8 -*-
from urllib import request

#response = request.urlopen('https://www.jumei.com')
#print(response.read().decode())

# 自己生成ssl证书
#import ssl
# context = ssl._create_unverified_context()
# response = request.urlopen('https://cd.jumei.com', context=context)
# print(response.read())

# 全局取消证书认证
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
print(request.urlopen('https://cd.jumei.com').read())



