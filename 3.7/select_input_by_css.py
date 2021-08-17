# -*- coding: utf-8 -*-
from selenium import webdriver

import os
driver = webdriver.Chrome()
file_path = 'file://' + os.path.abspath('textinput.html')
driver.get(file_path)

# 直接选择所有type为text的元素，并给文本框赋值
text_inputs =  driver.find_elements_by_css_selector('input[type=text]')

add_texts = ['auto', 'test', 'python']
# 从中筛选出type为text的元素，并分别赋值
index = 0
for input in text_inputs:
    input.send_keys(add_texts[index])
    index += 1

time.sleep(3)
driver.quit()
