# -*- coding: utf-8 -*-
from selenium import webdriver

import os
import time
driver = webdriver.Chrome()
file_path = 'file://' + os.path.abspath('textinput.html')
driver.get(file_path)

# 选择页面上所有input tag对象
input_objs = driver.find_elements_by_tag_name('input')
add_texts = ['auto', 'test', 'python']
# 从中筛选出type为text的元素，并分别赋值
index = 0
for input in input_objs:
    if input.get_attribute('type') == 'text':
        input.send_keys(add_texts[index])
        index += 1


time.sleep(3)
driver.quit()
