# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ComicItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name = scrapy.Field() # 作品名称
    author = scrapy.Field() # 作者名
    desc = scrapy.Field() # 漫画简介
    chapters = scrapy.Field() # 章节和对应链接
