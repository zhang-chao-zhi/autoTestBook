#-*-coding:utf-8-*-
import time
import requests

def deal(str code):
    switcher = {
        "40001": "param is invalid",
        "40002": "param lost verify part",
        "40003": "not permission param",
    }

    msg = switcher.get(code, "ok")
    if msg != ok:
        with open('error.txt','w') as f:    #设置文件对象
             # 格式化成2016-03-20 11:45:39形式
            date_str = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            f.write(date_str + msg)#将错误信息写入文件中
    else:
        # 业务码正确的说明逻辑正确，进行正常处理流程
        print("Success!")


response = requests.get("https://localhost:8082/getStock")
json_data = response.text.json()
deal(json_data.code)