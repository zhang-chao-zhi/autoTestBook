# -*-coding:utf-8-*-

import pytest


@pytest.fixture(scope="function")
def open_wordpress():
    print("打开wordpress页面_function")
