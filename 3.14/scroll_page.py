# -*- coding: utf-8 -*-
from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.get("https://www.baidu.com")

# 查询golang
driver.find_element_by_id("kw").send_keys("golang")
driver.find_element_by_id("su").click()
time.sleep(2)
#将页面滚动条拖到底部
js = "var q=document.documentElement.scrollTop=10000"
driver.execute_script(js)
time.sleep(3)
#将滚动条移动到页面的顶部
js_back = "var q=document.documentElement.scrollTop=0"
driver.execute_script(js_back)
time.sleep(3)

driver.quit()