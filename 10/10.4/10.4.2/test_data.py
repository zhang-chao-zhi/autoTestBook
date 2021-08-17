# -*- coding: utf-8 -*-

import csv,unittest,time
from selenium import webdriver
from ddt import ddt,data,unpack

def get_data(filename):
    # 创建一个空的列表来存储列数据
    rows = []
    # 打开csv文件
    data_file = open(filename, "r",encoding='utf-8')
    # 读取文件内容
    reader = csv.reader(data_file)
    # 跳过头部
    next(reader, None)
    # 添加数据到list
    for row in reader:
        rows.append(row)
    return rows

@ddt
class MyTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path='/Users/tony/Documents/chromedriver')
        cls.driver.implicitly_wait(3)
        cls.driver.get("http://baidu.com")

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
    @data(*get_data("testdata.csv"))
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