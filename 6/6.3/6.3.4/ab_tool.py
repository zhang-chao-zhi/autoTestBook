# -*- coding: utf-8 -*-
import os
import json


class AbTool(object):

    def __init__(self, url, child_process, request_num):
        self.url = url
        self.child_process = child_process
        self.request_num = request_num

    def set_url(self, url):
        self.url = url

    def set_child_process(self, child_process):
        self.child_process = child_process

    def set_request_num(self, request_num):
        self.request_num = request_num

    def set_time(self, seconds):
        self.seconds = seconds

    def runAndStore(self):
        cmd = "ab -n " + str(self.request_num) + " -c " + str(self.child_process) + " -t 5 " + self.url
        print(cmd)
        os.system(cmd)


tool = AbTool('https://www.soso.com/', 2, 100)
tool.runAndStore()