# -*-coding:utf-8-*-

import pytest


def test_01(start, open_soso):
    print("测试用例test_1")
    assert 1


def test_02(start, open_soso):
    print("测试用例test_2")
    assert 1


if __name__ == "__main__":
    pytest.main(["-s", "test_1_soso.py"])
