# -*- coding: utf-8 -*-
import os
import yaml

class AbTool(object):

    def __init__(self):
       config_data =  self.load_config()
       self.url = config_data['config']['url']
       self.child_process = config_data['config']['child_process']
       self.request_num = config_data['config']['request_num']
       self.running_time = config_data['config']['running_time']  # 执行持续时间

    # 从yaml文件获取config
    def load_config(self):
        config_data = {}
        file_path = './ab_config.yaml'
        with open(file_path, 'rb') as f:
            config_data = yaml.load(f)

        return config_data


    def set_url(self, url):
        self.url = url

    def set_child_process(self, child_process):
        self.child_process = child_process

    def set_request_num(self, request_num):
        self.request_num = request_num

    def set_time(self, seconds):
        self.seconds = seconds

    def runAndStore(self):
        cmd = "ab -n " + str(self.request_num) + " -c " + str(self.child_process) + " -t " + str(self.running_time) + " " + self.url
        print(cmd)
        os.system(cmd)


tool = AbTool()
tool.runAndStore()