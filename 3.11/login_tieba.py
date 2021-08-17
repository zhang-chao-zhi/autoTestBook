# -*- coding: utf-8 -*-
from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.get('https://tieba.baidu.com/index.html')
# 点击登录链接
first_btn = driver.find_element_by_css_selector("#com_userbar > ul > li.u_login > div > a")
first_btn.click()

time.sleep(3)
# 点击【用户名登录】选项
show_account_login = driver.find_element_by_id('TANGRAM__PSP_10__footerULoginBtn')
show_account_login.click()
time.sleep(2)
# 填充账号和密码
# TANGRAM__PSP_10__userName
# TANGRAM__PSP_10__password

driver.find_element_by_id('TANGRAM__PSP_10__userName').send_keys('your_account')
time.sleep(2)
driver.find_element_by_id('TANGRAM__PSP_10__password').send_keys('you password')

time.sleep(2)

driver.find_element_by_id('TANGRAM__PSP_10__submit').click()
