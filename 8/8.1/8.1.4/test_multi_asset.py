# -*-coding:utf-8-*-

import pytest
from pytest import assume


def test_multi_assert():
    assume(3 == 4)
    assume(5 == 5)
    assume(7 == 2)
