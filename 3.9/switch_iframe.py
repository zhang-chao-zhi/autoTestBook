# -*- coding: utf-8 -*-

from selenium import webdriver

import time

import os

driver = webdriver.Chrome()

file_path = 'file:///' + os.path.abspath('iframe.html')
driver.get(file_path)

driver.implicitly_wait(30)

# 先找到最外层的iframe(if1)
driver.switch_to_frame("if1")

# 再找内层的iframe(id=if2)
driver.switch_to_frame("if2")

# 操作元素
driver.find_element_by_id("query").send_keys("Python")
driver.find_element_by_id("stb").click()

time.sleep(3)
driver.quit()
