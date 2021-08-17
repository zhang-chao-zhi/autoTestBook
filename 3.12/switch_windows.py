# -*- coding: utf-8 -*-
from selenium import webdriver
import time
driver = webdriver.Chrome()
# 访问腾讯首页
driver.get('https://www.qq.com/?fromdefault')

# 获得当前窗口
nowhandle = driver.current_window_handle
# 打开新窗口
driver.find_element_by_css_selector("[bosszone=dh_1]").click()
time.sleep(3)
# 获取所有窗口
all_handles = driver.window_handles

for handle in all_handles:
    if handle != nowhandle:
        print("need to switch to nowhandle")
        driver.switch_to.window(handle)
        time.sleep(3)


driver.quit()


