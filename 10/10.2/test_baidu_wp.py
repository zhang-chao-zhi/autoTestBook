# -*- coding: utf-8 -*-
from __future__ import absolute_import
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
import time

if __name__ == '__main__':
    orgin_url = ['https://pan.baidu.com/']
    driver = webdriver.Chrome(executable_path='/Users/tony/Documents/chromedriver')
    driver.get(orgin_url[0])
    time.sleep(5)
    elem_static = driver.find_element_by_id("TANGRAM__PSP_4__footerULoginBtn")
    elem_static.click()
    time.sleep(0.5)
    elem_username = driver.find_element_by_id("TANGRAM__PSP_4__userName")
    elem_username.clear()
    elem_username.send_keys(u"tewerwr")  # 填入帐号
    elem_userpas = driver.find_element_by_id("TANGRAM__PSP_4__password")
    elem_userpas.clear()
    elem_userpas.send_keys(u"dfsfdsdfas")  # 密码
    elem_submit = driver.find_element_by_id("TANGRAM__PSP_4__submit")
    elem_submit.click()
    time.sleep(10)
driver.close()