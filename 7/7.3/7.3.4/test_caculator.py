# -*- coding: utf-8 -*-
import time
import os
import unittest
import HTMLTestRunner
from appium import webdriver


class CalculateTest(unittest.TestCase):

    @classmethod # 只初始化一次
    def setUpClass(cls):
        # 使用生成的模拟器的配置
        desire_caps = dict()
        desire_caps['platformName'] = 'Android'
        desire_caps['platformVersion'] = '29'
        desire_caps['deviceName'] = 'Nenux S'
        desire_caps['appPackage'] = 'com.android.calculator2'
        desire_caps['appActivity'] = '.Calculator'
        cls.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desire_caps)

    # 测试加法的计算
    def test_add(self):
        self.driver.find_element_by_name('9').click()
        self.driver.find_element_by_id('com.android.calculator2:id/plus').click()
        self.driver.find_element_by_name('5').click()
        self.driver.find_element_by_name('=').click()
        result = self.driver.find_element_by_class_name('android.widget.EditText').text
        self.assertEqual(result, str(9+5)) # 断言判断
        self.driver.find_element_by_name('CLR') # 清空结果，方便后续测试

    # 测试减法功能
    def test_substract(self):
        self.driver.find_element_by_name('9').click()
        self.driver.find_element_by_id('com.android.calculator2:id/minus').click()
        self.driver.find_element_by_name('4').click()
        self.driver.find_element_by_name('=').click()
        result = self.driver.find_element_by_class_name('android.widget.EditText').text
        self.assertEqual(result, str(9-4))
        self.driver.find_element_by_name('CLR')

    # 测试乘法运算
    def test_multi(self):
        self.driver.find_element_by_name('9').click()
        self.driver.find_element_by_id('com.android.calculator2:id/mul').click()
        self.driver.find_element_by_name('7').click()
        self.driver.find_element_by_name('=').click()
        result = self.driver.find_element_by_class_name('android.widget.EditText').text
        self.assertEqual(result, str(9*7))
        self.driver.find_element_by_name('CLR')

    # 测试除法运算
    def test_div(self):
        self.driver.find_element_by_name('6').click()
        self.driver.find_element_by_id('com.android.calculator2:id/div').click()
        self.driver.find_element_by_name('3').click()
        self.driver.find_element_by_name('=').click()
        result = self.driver.find_element_by_class_name('android.widget.EditText').text
        self.assertEqual(result, str(int(6/3)))
        self.driver.find_element_by_name('CLR').click()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == '__main__':
    cal_suit = unittest.makeSuite(CalculateTest, 'test')
    path = os.path.abspath(os.path.dirname(os.getcwd()))
    report_time = time.strftime('%Y%m%d', time.localtime())
    report_name = path + '\\report\\' + report_time + '-report.html' # 结果报告保存路径及名称
    with open(report_name, 'wb') as fp:
        # 生成报告未HTML格式
        runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=u'手机计算器测试报告', description=u'用例执行情况')
        runner.run(cal_suit) # 执行