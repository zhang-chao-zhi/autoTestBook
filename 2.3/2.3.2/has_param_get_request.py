#-*-coding:utf-8-*-
import requests
'''
 最终拼接效果为:
 https://www.baidu.com/s?wd=Python
'''
param = {"wd":"Python"}
get_url = 'https://www.baidu.com'
response = requests.get(get_url, params=param)
print(response.text)
