#-*-coding:utf-8-*-

import xlrd,unittest,time
from selenium import webdriver
from ddt import ddt,data,unpack
import os, sys

def get_data(filename):
    rows = []
    data_file = xlrd.open_workbook(filename,encoding_override='utf-8')
    sheet = data_file.sheet_by_index(0)
    for row_idx in range(1,sheet.nrows):
        rows.append(list(sheet.row_values(row_idx,0,sheet.ncols)))
    print(rows)
    return rows

@ddt
class WebTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()
        cls.driver.implicitly_wait(3)
        cls.driver.get("http://baidu.com")

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
    dir = os.path.dirname(os.path.abspath(__file__))

    @data(*get_data("testdata.xlsx"))
    @unpack
     # 搜索
    def test_search_info(self,search_value, expected_result):
        self.search = self.driver.find_element_by_xpath("//*[@id='kw']")
        self.search.clear()
        self.search.send_keys(search_value)
        self.search.submit()
        time.sleep(1.5)
        self.result = self.driver.title
        self.assertEqual(expected_result, self.result)

if __name__ == '__main__':
    unittest.main(verbosity=2)