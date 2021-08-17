# -*- coding: utf-8 -*-
import re

# 将正则表达式编译成Pattern对象
pattern = re.compile(r'Catch')

# 使用Pattern匹配文本，获得匹配结果，无法匹配时将返回None
match = pattern.match('Catch PHP and Python!How to catch me?')

if match:
    # 使用Match获得分组信息
    print(match.group())