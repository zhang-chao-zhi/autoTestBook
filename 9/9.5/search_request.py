#! /usr/bin/env python
# coding=utf-8

import unittest
import requests
import json
import sys
import time


sys.path.append('./libs/')
from SmartMySQL import SmartMySQL
from my_logger import My_logger

sys.path.append('./config/')
from dbconfig import get_config

class Api_Test4(unittest.TestCase):

    _search_url = None

    def setUp(self) -> None:
        self._search_url = "http://127.0.0.1:5000/my_app/api/v1/articles"


    def test_get(self):
        response = requests.get(self._search_url)
        db_config = get_config()
        mysql_obj = SmartMySQL(db_config)
        print(response.text)
        json_data = json.loads(response.text)
        articles = json_data["articles"]

        make_batch_insert_sql(articles)
        exit(0)
        for article in articles:
            # 组装sql
            make_insert_sql(article)
            exit(0)
            pass
        print(response.text)
        json_data = json.loads(response.text)
        articles = json_data["article"]
        # self.assertCountEqual(5, 5)

        for article in articles:
            # 组装sql
            pass




# 单个sql拼接，逐条插入
def make_insert_sql(row_data):
    sql = "INSERT api_articles (title, author, price, created) VALUES('%s', '%s', %s, %s)" % (row_data['title'], row_data['author'], row_data['price'], int(time.time()))
    return sql

# 批量插入的sql组装
def make_batch_insert_sql(data):
    sql = "INSERT api_articles (title, author, price, created) VALUES"

    for row_data in data:



        sql += "('%s', '%s', %s, %s)," % (row_data['title'], row_data['author'], row_data['price'], int(time.time()))

    sql = sql[0:len(sql) - 1] # 去掉最后一个多余的逗号字符
    return sql