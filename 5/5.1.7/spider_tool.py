#-*- coding:utf-8 -*-
import random

import requests
class SpiderTool(object):

    def __init__(self, url):
        self.url = url
        user_agent = self.get_random_user_agent()
        self.headers = {
            'user-agent': user_agent
        }

    def get_html(self, method_type='get', data={}):
        if method_type == 'get':
            response = requests.get(self.url)
        elif method_type == 'post':
            response = requests.post(self.url, data=data)
        else:
            print("It is not correct http method!")
            exit(1)
        html = response.text
        return html

    def parse(self):
        pass

    # 这里只写入到本地文件，如果要写入数据库则自己进行适当修改
    def store(self, data):
        with open('data.txt', 'w') as f:
            f.write(data)

    def get_random_user_agent(self):

        user_agents = [
            'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.163 Safari/535.1',
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36',
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11',
            'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50',
            'Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; en) Presto/2.8.131 Version/11.11',
            'Opera/9.80 (Windows NT 6.1; U; en) Presto/2.8.131 Version/11.11',
            'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Maxthon 2.0)',
            'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; 360SE)',
            'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; TencentTraveler 4.0)'
        ]
        num = len(user_agents)

        random_num = random.randint(0, num - 1)
        return user_agents[random_num]


if __name__ == '__main__':
    spider = SpiderTool('https://zhihu.com')