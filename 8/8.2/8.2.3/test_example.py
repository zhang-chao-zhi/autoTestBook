# -*-coding:utf-8-*-

import pytest


class TestExample():

    def test_run_all(self):
        assert ("install" == "install")

    def test_pick_me(self, x):
        x = 'ycy'
        assert "superstar" in x

    def test_add(self):
        sum_result = 10 + 5
        assert 16 == sum_result
