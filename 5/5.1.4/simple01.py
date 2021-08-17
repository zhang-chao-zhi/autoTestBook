# -*- coding: utf-8 -*-
# from urllib import request
# import ssl
from bs4 import BeautifulSoup

# 由于是本地html文件，需要打开文件然后读取
file_path = './simple01.html'

html_file = open(file_path, 'r', encoding='utf-8')
html_handle = html_file.read()

# 使用lxml解析器
soup = BeautifulSoup(html_handle, 'lxml')

print(soup.a)
print(soup.a.parent.name)
print(soup.a.parent.parent.name)