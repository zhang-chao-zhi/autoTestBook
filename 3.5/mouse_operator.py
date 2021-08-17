#-*-coding:utf-8-*-
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
'''
针对使用ActionChains类实现鼠标操作，封装成工具类。
double_click() 双击
context_click() 右键单击
drag_and_drop() 拖动鼠标
move_to_element() 鼠标悬停在一个元素上
click_and_hold() 按下鼠标左键在一个元素上
'''
class MouseOperator:
    def __init__(self, driver):
        self.driver = driver

    # 处理双击事件
    def double_click(self, locator):
        # 定位到要双击的元素
        double =self.driver.find_element_by_xpath(locator)
        # 对定位到的元素执行鼠标双击操作
        ActionChains(self.driver).double_click(double).perform()

    # 处理鼠标右键
    def right_click(self, locator):
        # 定位到要右击的元素
        right = self.driver.find_element_by_xpath(locator)
        # 对定位到的元素执行鼠标右键操作
        ActionChains(self.driver).context_click(right).perform()

    # 处理拖放元素
    def drag_drop(self, source_locator, target_locator):
        # 定位元素的原位置
        element = self.driver.find_element_by_name(source_locator)
        # 定位元素要移动到的目标位置
        target = self.driver.find_element_by_name(target_locator)
        # 执行元素的移动操作
        ActionChains(self.driver).drag_and_drop(element, target).perform()

    def hover_one_element(self, locator):
        # 定位到鼠标移动到上面的元素
        above = self.driver.find_element_by_xpath(locator)
        # 对定位到的元素执行鼠标移动到上面的操作
        ActionChains(self.driver).move_to_element(above).perform()

    def left_click_hover(self, locator):
        # 定位到鼠标按下左键的元素
        left = self.driver.find_element_by_xpath(locator)
        # 对定位到的元素执行鼠标左键按下的操作
        ActionChains(self.driver).click_and_hold(left).perform()