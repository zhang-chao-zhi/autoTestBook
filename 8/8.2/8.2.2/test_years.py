# -*-coding:utf-8-*-

import sys
sys.path.append(".")

import pytest
import is_leap_year

class TestYear():
    def test_some_exception(self):
        with pytest.raises(ValueError) as ex:
            is_leap_year.is_leap_year(-1)

        assert "从公元纪年开始" in str(ex.value)
        assert ex.type == ValueError