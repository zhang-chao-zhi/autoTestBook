#-*-coding:utf-8-*-
from selenium_tool import Tool
import time
from selenium import webdriver
# 测试自动化登录百度网盘
def testLogin():
    driver = webdriver.Chrome()
    client = Tool(driver)
    client.driver.get("https://pan.baidu.com")
    show_login_form = ("id", "TANGRAM__PSP_4__footerULoginBtn")
    # 点击显示账号登录方式，显示登录输入框
    client.click(show_login_form)
    time.sleep(0.5)
    #element = client.find(("name", "wd"))
    # 账号
    account = ("id", "TANGRAM__PSP_4__userName")
    # 密码
    password = ("id", "TANGRAM__PSP_4__password")
    # 设置账号和密码
    client.fill(account, "你的账号")
    # 休眠2.5秒，让操作更真实
    time.sleep(2.5)

    client.fill(password, "你的密码")
    # 休眠3秒，让操作更真实
    time.sleep(3)
    click_obj = ("id", "TANGRAM__PSP_4__submit")
    # 点击登录按钮
    client.click(click_obj)
    time.sleep(10)

if __name__ == '__main__':
    testLogin()