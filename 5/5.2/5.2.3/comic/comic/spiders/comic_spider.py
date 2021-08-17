# -*- coding: utf-8 -*-

import scrapy

from comic.items import ComicItem

class ComicSpider(scrapy.Spider):
    name = "comic"
    allowed_domains = ['ac.qq.com']
    start_urls = ['https://ac.qq.com/Comic/comicInfo/id/635188']

    def parse(self, response):
        # link_urls = response.xpath('//dd/a[1]/@href').extract()
        # 漫画名
        comic_name = response.xpath('/html/body/div[3]/div[3]/div[1]/div[1]/div[2]/div[1]/div[1]/h2/strong/text()').extract()[0]
        # //*[@id="special_bg"]/div[3]/div[1]/div[1]/div[2]/div[1]/p[1]/span[1]/em
        # 漫画作者名
        author_name = response.xpath('//*[@id="special_bg"]/div[3]/div[1]/div[1]/div[2]/div[1]/p[1]/span[1]/em/text()').extract()[0]
        # 漫画作品简介
        desc = response.xpath('//*[@id="special_bg"]/div[3]/div[1]/div[1]/div[2]/div[1]/p[2]/text()').extract()[0]

        comic_item = ComicItem()
        ##print(desc)

        # 章节列表获取    //*[@id="chapter"]/div[2]/ol[2]       //*[@id="chapter"]/div[2]/ol[2]/li/p[1]/span[1]/a   //*[@id="chapter"]/div[2]/ol[2]/li/p[2]/span[1]/a
        chapters = response.xpath('//*[@id="chapter"]/div[2]/ol[2]/li').extract()[0]
        # >> > response.xpath('//a[contains(@href, "image")]/@href').getall()

        hrefs = response.xpath('//a[contains(@href, "ComicView")]/@href').getall()
        valid_hrefs = []
        # 去重
        for href in hrefs:
            if href not in valid_hrefs:
                valid_hrefs.append(href)


        chapter_names = response.xpath('//a[contains(@href, "ComicView")]/@title').getall()
        # 筛选出有效标题
        valid_chapter_names = []
        for chapter in chapter_names:
            if "迷都奇点：" in chapter:
                pure_name = chapter.replace("迷都奇点：", "")
                if pure_name not in valid_chapter_names:
                    valid_chapter_names.append(pure_name)

        item_num = len(valid_chapter_names)
        # 章节结构
        chapters = []
        for index in range(item_num):
            tmp_row = {"name": valid_chapter_names[index], "url": valid_hrefs[index]}
            chapters.append(tmp_row)

        comic_item['chapters'] = chapters
        comic_item['name'] = comic_name
        comic_item['author'] = author_name
        comic_item['desc'] = desc
        print(comic_item)
