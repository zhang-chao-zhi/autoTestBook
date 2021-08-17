# -*-coding:utf-8-*-

import pytest

def test_03(start, open_wordpress):
    print("测试用例test_03")
    assert 1

def test_04(start, open_wordpress):
    print("测试用例test_04")
    assert 1

def test_05(start, open_soso):
    '''跨模块调用wordpress模块下的conftest'''
    print("测试用例test_05,跨模块调用soso")
    assert 1

if __name__ == "__main__":
    pytest.main(["-s", "test_2_wordpress.py"])