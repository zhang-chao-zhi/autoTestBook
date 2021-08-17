# -*- coding: utf-8 -*-
'''
使用logging模块自定义封装一个日志类
@author freePHP
@version 1.0.0
'''
import logging
import os.path
import time

class Logger(object):
    def __init__(self):
            self.logger = logging.getLogger("")
            # 设置输出的等级
            LEVELS = {'NOSET': logging.NOTSET,
                      'DEBUG': logging.DEBUG,
                      'INFO': logging.INFO,
                      'WARNING': logging.WARNING,
                      'ERROR': logging.ERROR,
                      'CRITICAL': logging.CRITICAL}
            # 创建文件目录
            logs_dir="logs2"
            if os.path.exists(logs_dir) and os.path.isdir(logs_dir):
                pass
            else:
                os.mkdir(logs_dir)
            # 修改log保存位置
            timestamp=time.strftime("%Y-%m-%d",time.localtime())
            logfilename='%s.txt' % timestamp
            logfilepath=os.path.join(logs_dir,logfilename)
            rotatingFileHandler = logging.handlers.RotatingFileHandler(filename =logfilepath,
                                                                       maxBytes = 1024 * 1024 * 50,
                                                                       backupCount = 5)
            # 设置输出格式
            formatter = logging.Formatter('[%(asctime)s] [%(levelname)s] %(message)s', '%Y-%m-%d %H:%M:%S')
            rotatingFileHandler.setFormatter(formatter)
            # 控制台句柄
            console = logging.StreamHandler()
            console.setLevel(logging.NOTSET)
            console.setFormatter(formatter)
            # 添加内容到日志句柄中
            self.logger.addHandler(rotatingFileHandler)
            self.logger.addHandler(console)
            self.logger.setLevel(logging.NOTSET)

        def info(self, message):
            self.logger.info(message)

        def debug(self, message):
            self.logger.debug(message)

        def warning(self, message):
            self.logger.warning(message)

        def error(self, message):
            self.logger.error(message)
