#-*-coding:utf-8-*-
import requests,json

url_json = 'http://httpbin.org/post'
data_json = json.dumps({'stock_no':'600585','price':'52.12'})   #dumps：可以将python对象解码为json数据
res = requests.post(url_json,data_json)
print(res)
print(res.text)
print(res.content)