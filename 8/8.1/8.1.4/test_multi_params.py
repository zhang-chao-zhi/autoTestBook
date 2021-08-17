# -*-coding:utf-8-*-

import pytest


@pytest.mark.parametrize('n1,n2', [
    (7 + 5, 12),
    (2 - 5, 1),
    (6 * 5, 30),
    (9 / 3, 2)
])
def test_equal(n1, n2):
    assert n1 == n2