# -*- coding: utf-8 -*-
import scrapy
from items import DetailItem
import sys


class TiebaSpider(scrapy.Spider):
    """
    name:scrapy唯一定位实例的属性名称。
    allowed_domains：允许爬取的域名列表。
    start_urls：起始爬取的链接。
    start_requests：它就是从start_urls中读取链接，然后使用make_requests_from_url生成Request，
                    可以在start_requests方法中根据我们自己的需求往start_urls中写入
                    已自定义的规律的链接。
    parse：回调函数，处理html字符串内容
    log：打印日志信息
    closed：关闭spider对象
    """
    # 设置name
    name = "spidertieba"
    # 设定域名
    allowed_domains = ["baidu.com"]
    # 填写爬取地址
    start_urls = [
        "https://tieba.baidu.com/f?kw=%E6%AD%A6%E5%8A%A8%E4%B9%BE%E5%9D%A4&ie=utf-8",
    ]

    # 编写爬取方法
    def parse(self, response):
        for line in response.xpath('//li[@class=" j_thread_list clearfix"]'):
            # 初始化item对象保存爬取的信息
            item = DetailItem()
            # 这部分是爬取部分，使用xpath的方式选择信息，具体方法根据网页结构而定
            item['title'] = line.xpath(
                './/div[contains(@class,"threadlist_title pull_left j_th_tit ")]/a/text()').extract()
            item['author'] = line.xpath(
                './/div[contains(@class,"threadlist_author pull_right")]//span[contains(@class,"frs-author-name-wrap")]/a/text()').extract()
            item['reply'] = line.xpath(
                './/div[contains(@class,"col2_left j_threadlist_li_left")]/span/text()').extract()
            yield item