#-*-coding:utf-8-*-
import pytest
class TestClass:
    # 检查名称是否包含某字符
    def test_check_username(self):
        username = "Supreme"
        assert "Cheer" in username

    # 测试是否有某字符为属性
    def test_has_attr(self):
        attr_str = "my"
        assert hasattr(attr_str, "fun")

    # 测试是否相等
    def test_equal(self):
        assert 2==4