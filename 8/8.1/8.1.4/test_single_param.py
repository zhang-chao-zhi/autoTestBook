#-*-coding:utf-8-*-

import pytest
import random


@pytest.mark.parametrize('x', [(3), (7), (9)])
def test_add(x):
    print(x)
    assert x == random.randrange(1, 7)