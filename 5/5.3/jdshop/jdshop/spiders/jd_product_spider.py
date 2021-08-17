# -*- coding: utf-8 -*-
import scrapy
from jdshop.items import JdshopItem

class JdProductSpider(scrapy.Spider):
    name = "JdShop"
    allowed_domains = ['list.jd.com']
    start_urls = ['https://list.jd.com/list.html?cat=670,671,672&page=1&sort=sort_totalsales15_desc&trans=1&JL=6_0_0#J_main']

    def parse(self, response):
        # product_name = response.xpath()
        # product_price = response.xpath()
        # product_sale_num = response.xpath()
        # product_type = response.xpath()
        # product_detail_link = response.xpath()

        product_list = response.xpath('//li[contains(@class,"gl-item")]')
        print(product_list)
        for item in product_list:
            # //*[@id="plist"]/ul/li[1]/div/div[2]/strong[1]/i
            print(item.xpath('div/div[@class="p-price"]/strong/i/text()'))

    def store(self, data):
        pass