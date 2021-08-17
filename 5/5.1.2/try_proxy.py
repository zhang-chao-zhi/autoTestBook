from urllib import request

url = 'http://httpbin.org/ip'
proxy = {'http': '218.18.232.26:80', 'https': '218.18.232.26:80'}
proxies = request.ProxyHandler(proxy)  # 创建代理处理器
opener = request.build_opener(proxies)  # 创建opener对象

resp = opener.open(url)
print(resp.read().decode())