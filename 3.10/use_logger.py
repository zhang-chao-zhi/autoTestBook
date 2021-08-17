# -*- coding: utf-8 -*-
# 调用logger类
import logging
import logger

mylogger = logger.Logger()
mylogger.debug("Start to debug it")
mylogger.info ("Start to info it")
mylogger.warning("Start to warning")
mylogger.error("Something is wrong")
