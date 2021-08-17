#-*-coding:utf-8-*-
from selenium import webdriver
# 引入Keys类包
from slenium.webdriver.common.keys import Keys
import time
'''
针对使用Keys类包实现键盘操作，封装成工具类。
包含输入、删除内容、输入带空格内容、输入带Tab键内容、剪切输入框内容、输入框重新输入内容、回车键使用
'''
class KeyBoardOperator:
    # 将driver注入
    def __init__(self, driver):
       self.driver = driver
    # 输入一段文字
    def input_words(self, locator, text):
        self.driver.find_element_by_xpath(locator).send_keys(text)
        time.sleep(3)
    # 删除一个字符
    def del_some_word_with_backspace(self, locator):
        self.driver.find_element_by_xpath(locator).send_keys(Keys.BACK_SPACE)
        time.sleep(2.5)
    # 全选
    def select_all(self, locator):
        self.driver.find_element_by_xpath(locator).send_keys(Keys.CONTROL, 'a')
        time.sleep(3)

    # 剪切内容
    def cut_content(self, locator):
        self.driver.find_element_by_id(locator).send_keys(Keys.CONTROL, 'x')
        time.sleep(2)

    # 粘贴内容
    def paste_content(self, locator):
        self.driver.find_element_by_id(locator).send_keys(Keys.CONTROL, 'v')
        time.sleep(2)

    # 回车代替点击操作
    def enter_click(self, locator):
        self.driver.find_element_by_id(locator).send_keys(Keys.ENTER)
        time.sleep(2.5)