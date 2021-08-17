# -*-coding:utf-8-*-
import pytest


@pytest.fixture(scope="session")
def start():
    print("打开home page")
