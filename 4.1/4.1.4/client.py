# -*- coding: utf-8 -*-
import requests

# 发出get请求
def send_request(url):
    r = requests.get(url)
    return r.status_code

# 访问百度
def visit_baidu():
    return send_request("https://www.baidu.com")