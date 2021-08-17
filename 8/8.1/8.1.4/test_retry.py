# -*-coding:utf-8-*-

import pytest
import random

# 重试测试类
class TestReTry():

    @pytest.mark.flaky(reruns=5)
    def test_random(self):
        print(1)
        pytest.assume((random.randint(0, 8) + 1) == 5)

    @pytest.mark.flaky(returns=3)
    def test_ping(self):
        ping = random.choice([True, False])
        assert (ping == True)
