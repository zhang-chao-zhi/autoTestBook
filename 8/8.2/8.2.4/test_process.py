# -*-coding:utf-8-*-
import allure


@allure.step('Start with some function in the tile, postitional: “{0}”, keyword: “{key}”')
def step_with_title_fun1(arg1, key=None):
    pass


def test_steps_with_fun():
    step_with_title_fun1(1, key="hello")
    step_with_title_fun1(2)
    step_with_title_fun1(3, "China")
