#! /usr/bin/env python
# coding=utf-8

import unittest
import requests
import json
import sys
import time

sys.path.append('./libs/')
from SmartMySQL import SmartMySQL
from my_logger import My_logger

sys.path.append('./config/')
from dbconfig import get_config


class Api_Test(unittest.TestCase):
    _insert_data = None
    _insert_url = None

    # 用setUp来代替__init__，setUp会在每一个case执行前被自动执行
    def setUp(self) -> None:
        self._insert_data = [
            {
                'title': u'PHP全书',
                'author': u'freephp',
                'price': 45
            },
            {
                'title': u'Python自动化测试',
                'author': u'freephp',
                'price': 34
            },
            {
                'title': u'Unix编程',
                'author': u'鸟哥',
                'price': 97
            }
        ]

        self._insert_url = "http://127.0.0.1:5000/my_app/api/v1/articles"

    def test_insert(self):
        config = get_config()
        mysql_obj = SmartMySQL(config)
        api_path = self._insert_url
        http_method = 'POST'
        my_logger = My_logger('./logs/test_insert.log')
        for row_data in self._insert_data:

            json_data_str = json.dumps(row_data, ensure_ascii=False)

            response_str = 'ok'
            created = int(time.time())
            assert_result = "见报告"
            insert_sql = "INSERT request_logs (api_path, http_method, params, response, assert_result, created) VALUES("
            response = requests.post(self._insert_url, row_data)

            if response.status_code != 200:
                response_str = str(response.content)
                my_logger.error("The http code is %s" % str(response.status_code))

            res_data = json.loads(response.text)
            self.assertEqual(res_data['book']['price'], '45')
            self.assertEqual(res_data['book']['author'], 'freephp')

            insert_sql += "'" + api_path + "', '" + str(
                http_method) + "','" + json_data_str + "','" + response_str + "', '" + assert_result + "'," + str(
                created) + ")"
            print(insert_sql)
            res = mysql_obj.dml(insert_sql)
            # print("somthing: \r\n")
            # print(res)
            # print("over=======")
            # exit(0)


def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(Api_Test)
    test_result = unittest.TextTestRunner(verbosity=2).run(suite)
    print('All case number')
    print(test_result.testsRun)
    print('Failed case number')
    print(len(test_result.failures))
    print('Failed case and reason')
    print(test_result.failures)
    for case, reason in test_result.failures:
        print(case.id())
        print(reason)


if __name__ == '__main__':
    main()
