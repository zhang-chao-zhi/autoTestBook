#-*-coding:utf-8-*-
import requests  # 引入requests库
response = requests.get("https://www.baidu.com/")  # 使用GET方式请求百度首页

# 查看响应内容，response.text为Unicode格式的数据
print(response.text)
# 查看响应内容，response.content为字节流数据
print(response.content)
# 查看完整url地址
print(response.url)
# 查看响应头部字符编码
print(response.encoding)
# 查看响应码
print(response.status_code)