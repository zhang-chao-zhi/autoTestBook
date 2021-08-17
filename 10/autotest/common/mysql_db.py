#!/usr/bin/env python
# *_*coding:utf-8 *_*
__author__ = "freephp"
from read_config import Read_Config
from my_logger import My_logger

readconf_obj = Read_Config()

host = readconf_obj.get_db("host")
username = readconf_obj.get_db("username")
password = readconf_obj.get_db("password")
port = readconf_obj.get_db("port")
database = readconf_obj.get_db("database")
dbconfig = {
    'host': str(host),
    'user': username,
    'password': password,
    'port': int(port),
    'db': database
}

import mysql.connector
import time, re
from mysql.connector import errorcode


class SmartMySQL:
    """Smart python class connects to MySQL. """

    # db配置，如账号、密码、数据库名
    _dbconfig = None
    _cursor = None
    _connect = None
    # error_code from MySQL
    _error_code = ''
    # quit connect if beyond 30 sec
    TIMEOUT_DEADLINE = 30
    TIMEOUT_THREAD = 10  # threadhold of one connect
    TIMEOUT_TOTAL = 0  # total time the connects have waste

    # 初始化
    def __init__(self, dbconfig):
        try:
            self._dbconfig = dbconfig
            self.check_dbconfig(dbconfig)
            self._connect = mysql.connector.connect(user=self._dbconfig['user'], password=self._dbconfig['password'],
                                                    database=self._dbconfig['db'])
            self.my_logger = My_logger('../logs/mysql-' + time.strftime("%Y-%m-%d-%H-%M-%S") + '.log')
        except mysql.connector.Error as e:
            print(e.msg)

            if e.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database dosen't exist, check it or create it")
                self.my_logger.error("Database dosen't exist, check it or create it")
            # 重试
            if self.TIMEOUT_TOTAL < self.TIMEOUT_DEADLINE:
                interval = 0
                self.TIMEOUT_TOTAL += (interval + self.TIMEOUT_THREAD)
                time.sleep(interval)
                self.__init__(dbconfig)
            raise Exception(e.errno)

        self._cursor = self._connect.cursor()
        print("init success and connect it")

    # 检查数据库配置是否正确
    def check_dbconfig(self, dbconfig):
        flag = True
        if type(dbconfig) is not dict:
            print('dbconfig is not dict')
            flag = False
        else:
            for key in ['host', 'port', 'user', 'password', 'db']:
                if key not in dbconfig:
                    print("dbconfig error: do not have %s" % key)
                    flag = False
            if 'charset' not in dbconfig:
                self._dbconfig['charset'] = 'utf8'

        if not flag:
            raise Exception('Dbconfig Error')
        return flag

    # 执行sql
    def query(self, sql, ret_type='all'):
        try:
            self._cursor.execute("SET NAMES utf8")
            self._cursor.execute(sql)
            if ret_type == 'all':
                return self.rows2array(self._cursor.fetchall())
            elif ret_type == 'one':
                return self._cursor.fetchone()
            elif ret_type == 'count':
                return self._cursor.rowcount
        except mysql.connector.Error as e:
            print(e.msg)
            self.my_logger.error(e.msg)
            return False

    def dml(self, sql):
        '''update or delete or insert'''
        try:
            self._cursor.execute("SET NAMES utf8")
            self._cursor.execute(sql)
            self._connect.commit()
            type = self.dml_type(sql)
            if type == 'insert':
                return self._cursor.getlastrowid()
            else:
                return True
        except mysql.connector.Error as e:
            self.my_logger.error(e.msg)
            print(e.msg)
            return False

    def dml_type(self, sql):
        re_dml = re.compile('^(?P<dml>\w+)\s+', re.I)
        m = re_dml.match(sql)
        if m:
            if m.group("dml").lower() == 'delete':
                return 'delete'
            elif m.group("dml").lower() == 'update':
                return 'update'
            elif m.group("dml").lower() == 'insert':
                return 'insert'
        print(
            "%s --- Warning: '%s' is not dml." % (time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())), sql))
        return False

    # 结果转化为数组
    def rows2array(self, data):
        '''transfer tuple to array.'''
        result = []
        for da in data:
            if type(da) is not dict:
                raise Exception('Format Error: data is not a dict.')
            result.append(da)
        return result

    # close it
    def __del__(self):
        '''free source.'''
        try:
            self._cursor.close()
            self._connect.close()
        except:
            pass

    def close(self):
        self.__del__()

