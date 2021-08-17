#-*-coding:utf-8-*-

#创建基础类
class BasePage(object):
    #初始化
    def __init__(self, driver):
        self.base_url = 'https://pan.baidu.com/'
        self.driver = driver
        self.timeout = 30

    def _open(self):
        url = self.base_url
        self.driver.get(url)
        btn = self.driver.find_element_by_id('TANGRAM__PSP_4__footerULoginBtn')  #切换到登录窗口的iframe
        btn.click()

    def open(self):
        self._open()

    def find_element(self,*loc):
        return self.driver.find_element(*loc)


#创建LoginPage类
class LoginPage(BasePage):
    username_location = (By.ID, "TANGRAM__PSP_4__userName")
    password_location = (By.ID, "TANGRAM__PSP_4__password")
    login_location = (By.ID, "TANGRAM__PSP_4__submit")

    #输入用户名
    def type_username(self,username):
        self.find_element(*self.username_location).clear()
        self.find_element(*self.username_location).send_keys(username)

    #输入密码
    def type_password(self,password):
        self.find_element(*self.password_locaction).send_keys(password)

    #点击登录
    def type_login(self):
        self.find_element(*self.login_loc).click()

def test__login(driver, username, password):
    """测试用户名and密码是否可以登录"""
    login_page = LoginPage(driver)
    login_page.open()
    login_page.type_username(username)
    login_page.type_password(password)
    login_page.type_login


def main():
    driver = webdriver.Edge()
    username = 'sdsd'    #账号
    password = 'kemixxxx'    #密码
    test_user_login(driver, username, password)
    sleep(3)

    driver.quit()

if __name__ == '__main__':
    main()
