# -*- coding: utf-8 -*-
import time
from selenium import webdriver
from selenium.webdriver import ActionChains

browser = webdriver.Firefox(executable_path='/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/site-packages/selenium/webdriver/geckodriver')

# 网站登陆页面
url = 'http://admin.emaotai.cn/login.aspx'

# 浏览器访问登录页面
browser.get(url)

browser.maximize_window()

browser.implicitly_wait(5)


draggable = browser.find_element_by_id('nc_1_n1z')

# 滚动指定元素位置
browser.execute_script("arguments[0].scrollIntoView();", draggable)

time.sleep(2)

ActionChains(browser).click_and_hold(draggable).perform()

# 拖动
ActionChains(browser).move_by_offset(xoffset=247, yoffset=0).perform()

ActionChains(browser).release().perform()