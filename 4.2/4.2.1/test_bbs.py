# -*- coding: utf-8 -*-
import unittest, json
from unittest import mock
import requests

'''
用于测试tinyBBS系统的测试类

@author freePHP
@version 1.0.0
'''
class TestBBS(unittest.TestCase):
    # 用于测试新增留言接口
    def test_add(self):
        url = 'http://127.0.0.1:5000/add'
        data = {"message": "井底点灯深烛伊，共郎长行莫围棋。玲珑骰子安红豆，入骨相思知不知。"}
        mock_return_data = {"data": [], "errorMsg": "", "result": True}  # mock数据返回结果
        mock_data = mock.Mock(return_value=mock_return_data)
        print(mock_data)

        res = requests.post(url, data=data)
        print(res.text)
        try:
            return_data = json.loads(res.text)
            self.assertEqual(return_data['result'], True)
        except:
            print("json loads error")

    # 测试新增留言失败的情况的单元测试用例
    def test_add_fail_case(self):
        url = 'http://127.0.0.1:5000/add'
        data = {"message": "onetwo"} # 设置长度小于20个字符的message
        mock_return_data = {"data": [], "errorMsg": "The message is too short,min is 20 character", "result": False}  # mock数据返回结果
        mock_data = mock.Mock(return_value=mock_return_data)
        print(mock_data)

        res = requests.post(url, data=data)
        print(res.text)
        return_data = json.loads(res.text)
        self.assertEqual(return_data['result'], False)
        self.assertEqual(return_data['errorMsg'], "The message is too short,min is 20 character 2333")
