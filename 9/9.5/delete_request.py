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


class Api_Test3(unittest.TestCase):
    _insert_data = None
    _insert_url = None

    # 用setUp来代替__init__，setUp会在每一个case执行前被自动执行
    def setUp(self) -> None:
        self._delete_data = [4, 5]

        self._update_url = "http://127.0.0.1:5000/my_app/api/v1/articles"

    def test_delete(self):
        for id in self._delete_data:
            response = requests.delete(self._update_url + '/' + str(id))
            print(response.text)
            res_data = json.loads(response.text)
            self.assertEqual(res_data['result'], True)
