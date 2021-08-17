#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
sys.path.append('../libs/')
from SmartMySQL import SmartMySQL
sys.path.append('../config/')
from dbconfig import get_config

create_article_sql = '''
CREATE TABLE `api_articles` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT COMMENT '主键',
  `title` varchar(80) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NOT NULL COMMENT '文章名',
  `author` varchar(80) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NOT NULL COMMENT '作者名',
  `price` int(11) NOT NULL DEFAULT '0' COMMENT '价格',
  `created` int(11) DEFAULT NULL COMMENT '记录创建时间',
  `modified` int(11) DEFAULT NULL COMMENT '记录修改时间',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin
'''

# 获取配置
db_config = get_config()

# print(" the db config is \r\n")
# print(db_config)
# exit(0)
create_request_log_sql = '''
CREATE TABLE `request_logs` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT COMMENT '主键',
  `api_path` varchar(0) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NOT NULL COMMENT '请求的接口地址',
  `http_method` varchar(6) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NOT NULL COMMENT '请求方式，GET、POST、PUT、DELETE',
  `params` varchar(1000) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NOT NULL COMMENT '参数，以json字符串形式存储',
  `response` varchar(500) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NOT NULL COMMENT '返回结果文本',
  `assert_result` varchar(500) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NOT NULL COMMENT '断言判断结果',
  `created` int(11) DEFAULT NULL COMMENT '记录创建时间',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin
'''

mysql_obj = SmartMySQL(db_config)
mysql_obj.query(create_article_sql)
mysql_obj.query(create_request_log_sql)