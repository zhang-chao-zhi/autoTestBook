#-*- coding:utf-8 -*-
__author__ = 'freePHP'
import re
text = input("Please input your Email address：\n")
if re.match(r'^[0-9a-zA-Z_]{0,19}@[0-9a-zA-Z]{1,13}\.[com,cn,net]{1,3}$',text):
    print('Email address is Right!')
else:
    print('Please reset your right Email address!')