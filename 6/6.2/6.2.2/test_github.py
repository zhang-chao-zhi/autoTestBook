# -*- coding: utf-8 -*-
from locust import HttpLocust, TaskSet, task

# 继承TaskSet
class WebsiteTasks(TaskSet):
    def on_start(self):  # 初始化工作
        payload = {
            "username": "test_me",
            "password": "123456",
        }
        header = {
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
        }
        self.client.post("/login", data=payload,headers=header)

    @task(5)
    def index(self):
        self.client.get("/")

    @task(1)
    def about(self):
        self.client.get("/about/")


class WebsiteUser(HttpLocust):
    host = "https://github.com/"   # 提供给--host的参数
    task_set = WebsiteTasks  # TaskSet类
    min_wait = 5000  # 每个用户的间隔时间，单位毫秒，在max和min之间的随机时间
    max_wait = 15000 # 最大间隔时间