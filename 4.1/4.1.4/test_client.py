# -*- coding: utf-8 -*-
"""
用于测试client类的测试类

@author freePHP
@version v1.1.0
"""
import unittest
from unittest import mock
from . import client


class TestClient(unittest.TestCase):

    def test_success_request(self):
        success_send = mock.Mock(return_value='200')
        client.send_request = success_send
        self.assertEqual(client.visit_baidu(), '200')

    def test_fail_request(self):
        forbidden_send = mock.Mock(return_value='403')
        client.send_request = forbidden_send
        self.assertEqual(client.visit_baidu(), '403')


if __name__ == '__main__':
    unittest.main()
