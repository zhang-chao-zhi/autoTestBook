# -*- coding: utf-8 -*-
from selenium import webdriver

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains

import time
import os

driver = webdriver.Chrome()
file_path = 'file:///' + os.path.abspath('dropList.html')
driver.get(file_path)

# 点击button弹出下拉列表
driver.find_element_by_link_text('Event1').click()

# 在父元素下找到link为Event3的子元素

targets = driver.find_element_by_id('super1').find_element_by_link_text("Event3")

# 将鼠标移动到该子元素上
ActionChains(driver).move_to_element(menu).perform()
time.sleep(4)
driver.quit()

