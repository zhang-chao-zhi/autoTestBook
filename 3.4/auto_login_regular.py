#-*-coding:utf-8-*-
from selenium import webdriver
import time
def auto_login():
    driver = webdriver.Chrome()
    #设置浏览器窗口的位置和大小
    driver.set_window_position(20, 40)
    driver.set_window_size(1100,700)
    # 访问QQ空间登录页
    driver.get("http://qzone.qq.com")
    # 切换到登录表单框架
    driver.switch_to_frame('login_frame')
    # 分别设置登录账号和密码，使用find_element_by_id
    driver.find_element_by_id('switcher_plogin').click()
    driver.find_element_by_id('u').clear()
    driver.find_element_by_id('u').send_keys('401112769')
    driver.find_element_by_id('p').clear()
    driver.find_element_by_id('p').send_keys('tonytang!2019')
    driver.find_element_by_id('login_button').click()
    time.sleep(5)
    # 关闭窗口
    driver.quit()

if __name__ == '__main__':
    auto_login()