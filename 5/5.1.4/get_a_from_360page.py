# -*- coding: utf-8 -*-
from urllib import request
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

url = 'https://www.so.com/?src=pclm&ls=safarimac'
headers = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_5) \
AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36'}

req = request.Request(url, headers=headers)
response = request.urlopen(req)

html = response.read()
from bs4 import BeautifulSoup

bs = BeautifulSoup(html,"html.parser", from_encoding="utf8")
#print(bs.nav) # 定位到nav标签内容

nav = bs.nav
a_links = nav.find_all("a")
#print(a_links)

links = []
for link in a_links:
    links.append(link.get("href"))

print(links)