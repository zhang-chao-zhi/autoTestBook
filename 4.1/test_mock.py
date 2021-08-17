import unittest
from unittest import mock

# 计算两正数之和
class SimpleCaculator(object):
    def sum(num1: int, num2: int) -> int:
        return num1 + num2


class SumTest(unittest.TestCase):
    def test(self):
        s = SimpleCaculator()
        num1 = 10
        num2 = 30
        sum_result = mock.Mock(return_value=40)
        s.sum = sum_result
        self.assertEqual(s.sum(), 40)

