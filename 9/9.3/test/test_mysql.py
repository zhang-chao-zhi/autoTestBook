#!/usr/bin/env python
import sys
sys.path.append('../libs/')
from SmartMySQL import SmartMySQL

config = {
    'host': '127.0.0.1',
    'port': 3306,
    'user': 'root',
    'password': '1234567qaz,TW',
    'db': 'for_python_test'
}
mysql_obj = SmartMySQL(config)

