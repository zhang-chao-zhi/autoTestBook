#-*-coding:utf-8-*-
'''
基于Selenium的操作封装类。
@Author freePHP(我的艺名)
@Created at 2019
'''
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
class Tool():
    def __init__(self, driver):
        self.driver = driver

    #查找指定定位的元素
    def find(self, locator):
        element = WebDriverWait(self.driver, 10, 1).until(lambda x: x.find_element(*locator))
        return element

    # 填充文本到指定的文本元素
    def fill(self, locator, text):
        self.find(locator).send_keys(text)

    # 检查该元素是否存在
    def element_exists(self, locator) -> bool:
        ones=self.finds(locator)
        if len(ones) >= 1:
            return True
        else:
            return False

    # 触发点击事件
    def click(self, locator):
        self.find(locator).click()