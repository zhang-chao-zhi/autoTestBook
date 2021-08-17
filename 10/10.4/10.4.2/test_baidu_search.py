#-*-coding:utf-8-*-

import unittest,time
from selenium import webdriver
from ddt import ddt,data,unpack

@ddt
class WebTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path='/Users/tony/Documents/chromedriver')
        cls.driver.implicitly_wait(3)
        cls.driver.get("https://baidu.com")

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    @data(("Python","Python_百度搜索"),("PHP","PHP_百度搜索"))
    @unpack
     # 搜索
    def test_search_info(self,search_value, expected_result):
        self.search = self.driver.find_element_by_xpath("//*[@id='kw']")
        self.search.clear()
        self.search.send_keys(search_value)
        self.search.submit()
        time.sleep(1.5)
        self.result = self.driver.title
        self.assertEqual(expected_result,self.result)

if __name__ == '__main__':
    unittest.main(verbosity=2)