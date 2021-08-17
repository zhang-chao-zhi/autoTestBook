# -*-coding:utf-8-*-
import pytest

@pytest.mark.run(order=2)
def test_order1():
    print("first test")
    assert True

@pytest.mark.run(order=1)
def test_order2():
    print("second test")
    assert True