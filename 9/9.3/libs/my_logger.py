#! /usr/bin/env python
# coding=utf-8

import logging

'''
   基于logging封装操作类
   author: freephp
   date: 2020
'''
class My_logger:

    _logger = None

    '''
    初始化函数，主要用于设置命令行和文件日志的报错级别和参数
    '''
    def __init__(self, path, console_level=logging.DEBUG, file_level=logging.DEBUG):
        self._logger = logging.getLogger(path)
        self._logger.setLevel(logging.DEBUG)
        fmt = logging.Formatter('[%(asctime)s] [%(levelname)s] %(message)s', '%Y-%m-%d %H:%M:%S')
        # 设置命令行日志
        sh = logging.StreamHandler()
        sh.setLevel(console_level)
        sh.setFormatter(fmt)

        # 设置文件日志
        fh = logging.FileHandler(path, encoding='utf-8')
        fh.setFormatter(fmt)
        fh.setLevel(file_level)
        self._logger.addHandler(sh)
        self._logger.addHandler(fh)

    # 当级别为debug的时候的记录调用
    def debug(self, message):
        self._logger.debug(message)

    # 当级别为info的时候的记录调用
    def info(self, message):
        self._logger.info(message)

    # 当级别为警告的时候的记录调用
    def warning(self, message):
        self._logger.warning(message)

    # 当级别为error的时候的记录调用
    def error(self, message):
        self._logger.error(message)

    # 当级别为严重错误的时候的记录调用，类似于PHP中的Fata Error
    def critical(self, message):
        self.logger.critical(message)



#
# if __name__ == '__main__':
#     logger = My_logger('./catlog1.txt')
#     logger.warning("FBI warning it\r\n")