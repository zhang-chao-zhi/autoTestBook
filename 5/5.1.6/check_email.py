#-*- coding:utf-8 -*-
__author__ = '杨鑫'
import re
text = input("Please input your Email address：\n")
if re.match(r'[0-9a-zA-Z_]{0,19}@163.com',text):
    print('Email address is Right!')
else:
    print('Please reset your right Email address!')