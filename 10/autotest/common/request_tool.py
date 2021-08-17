#! /usr/bin/env python
# coding=utf-8

__author__ = "Free PHP"
from selenium import webdriver

import time, os

class Request_Tool(object):
    __project_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    def __init__(self, driver):
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()

    def open_url(self, url):
        self.driver.get(url)
        self.driver.implicitly_wait(30)

    def find_element(self, element_type, value):
        if element_type == 'id':
            el = self.driver.find_element_by_id(value)
        if element_type == 'name':
            el = self.driver.find_element_by_name(value)
        if element_type == 'class_name':
            el = self.driver.find_element_by_class_name(value)
        if element_type == 'tag_name':
            el = self.driver.find_elements_by_tag_name(value)
        if element_type == 'link':
            el = self.driver.find_element_by_link_text(value)
        if element_type == 'css':
            el = self.driver.find_element_by_css_selector(value)
        if element_type == 'partial_link':
            el = self.driver.find_element_by_partial_link_text(value)
        if element_type == 'xpath':
            el = self.driver.find_element_by_xpath(value)
            if el:
                return el
            else:
                return None

    # 利用Selenium的点击事件
    def click(self, element_type, value):
        self.find_element(element_type, value).click()

    # 利用Selenium输入
    def input_data(self, element_type, value, data):
        self.find_element(element_type, value).send_keys(data)

    # 获取截图
    def get_screenshot(self, id):

        for filename in os.listdir(os.path.dirname(os.getcwd())):
            if filename == 'picture':
                break

            else:
                os.mkdir(os.path.dirname(os.getcwd()) + '/picture/')
            photo = self.driver.get_screenshot_as_file(self.__project_dir + '/picture/' + str(id) + str('_') + time.strftime("%Y-%m-%d-%H-%M-%S") + '.png')
            return photo


    def delete_self(self):
        time.sleep(2)
        self.driver.close()
        self.driver.quit()



