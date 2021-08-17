#-*-coding:utf-8-*-
import requests,json
url  = 'http://httpbin.org/post'
files = {'file':open('./report.txt','rb')} # 设置要被打开的文件
res = requests.post(url_mul,files=files) # 发送POST请求
print(res)
print(res.text)
print(res.content)