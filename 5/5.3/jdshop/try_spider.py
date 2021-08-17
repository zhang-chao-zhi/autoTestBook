'''
爬取京东商品信息:
    请求url:
        https://www.jd.com/
    提取商品信息:
        1.商品详情页
        2.商品名称
        3.商品价格
        4.评价人数
        5.商品商家
'''
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


def get_good(driver):
    try:

        # 通过JS控制滚轮滑动获取所有商品信息
        js_code = '''
            window.scrollTo(0,5000);
        '''
        driver.execute_script(js_code)  # 执行js代码

        # 等待数据加载
        time.sleep(2)

        # 3、查找所有商品div
        # good_div = driver.find_element_by_id('J_goodsList')
        good_list = driver.find_elements_by_class_name('gl-item')
        n = 1
        for good in good_list:
            # 根据属性选择器查找
            # 商品链接
            good_url = good.find_element_by_css_selector(
                '.p-img a').get_attribute('href')

            # 商品名称
            good_name = good.find_element_by_css_selector(
                '.p-name em').text.replace("\n", "--")

            # 商品价格
            good_price = good.find_element_by_class_name(
                'p-price').text.replace("\n", ":")

            # 评价人数
            good_commit = good.find_element_by_class_name(
                'p-commit').text.replace("\n", " ")

            good_content = f'''
                        商品链接: {good_url}
                        商品名称: {good_name}
                        商品价格: {good_price}
                        评价人数: {good_commit}
                        \n
                        '''
            print(good_content)
            with open('jd.txt', 'a', encoding='utf-8') as f:
                f.write(good_content)

        next_tag = driver.find_element_by_class_name('pn-next')
        next_tag.click()

        time.sleep(2)

        # 递归调用函数
        get_good(driver)

        time.sleep(10)

    finally:
        driver.close()



if __name__ == '__main__':

    good_name = input('请输入爬取商品信息:').strip()

    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    # 1、往京东主页发送请求
    driver.get('https://www.jd.com/')

    # 2、输入商品名称，并回车搜索
    input_tag = driver.find_element_by_id('key')
    input_tag.send_keys(good_name)
    input_tag.send_keys(Keys.ENTER)
    time.sleep(2)

    get_good(driver)