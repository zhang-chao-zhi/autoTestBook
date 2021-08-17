# -*- coding: utf-8 -*-
from selenium import webdriver
import time
driver = webdriver.Chrome()

# 访问Python吧首页
index_url = 'http://tieba.baidu.com/f?ie=utf-8&kw=python'
# frs_list_pager
driver.get(index_url)
# 定位等到分页div
pagination_div = driver.find_element_by_id('frs_list_pager')
print(pagination_div)

# 计算最后一页的页码
# 先点击尾页按钮
driver.find_element_by_css_selector('.last.pagination-item').click()
time.sleep(3)
# 获取尾页的页码数
last_page_no = driver.find_element_by_css_selector('.pagination-current.pagination-item').text
time.sleep(2)
print(last_page_no)
# 跳回首页
driver.get(index_url)
# 循环last_page_no次获取每一页的数据
for index in last_page_no:
    # 一些收集数据的代码，省略
    time.sleep(2)
    driver.find_element_by_css_selector('.next.pagination-item').click()


driver.quit()