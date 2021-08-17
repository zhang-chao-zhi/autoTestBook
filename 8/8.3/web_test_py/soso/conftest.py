# -*-coding:utf-8-*-

import pytest


@pytest.fixture(scope="session")
def open_soso():
    print("打开soso页面_session")
