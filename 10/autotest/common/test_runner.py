#! /usr/bin/env python
# coding=utf-8

__author__ = "Free PHP"

import time,HTMLTestRunner
import unittest
from common.config import *
project_dir = os.path.abspath(os.path.join(os.path.dirname(__file__),os.pardir))
class TestRunner(object):
    ''' 执行测试用例 '''
    def __init__(self, cases="../",title="Auto Test Report",description="Test case execution"):
        self.cases = cases
        self.title = title
        self.des = description
    def run(self):
        for filename in os.listdir(project_dir):
            if filename == "report":
                break
        else:
            os.mkdir(project_dir+'/report')
        # fp = open(project_dir+"/report/" + "report.html", 'wb')
        now = time.strftime("%Y-%m-%d_%H_%M_%S")
        # fp = open(project_dir+"/report/"+"result.html", 'wb')
        fp = open(project_dir+"/report/"+ now +"result.html", 'wb')
        tests =  unittest.defaultTestLoader.discover(self.cases,pattern='test*.py',top_level_dir=None)
        runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=self.title, description=self.des)
        runner.run(tests)
        fp.close()