#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:fengg
@file:Log.py
@time:2020/08/06
"""
import logging
import logging.config
from config.VarConfig import parentDirPath


# 读取日志配置文件
logging.config.fileConfig(parentDirPath + u"\\config\\Logger.conf")
# 选择一个日志格式
logger = logging.getLogger("example02")  # 或者example01


def debug(message):
    logger.debug(message)


def info(message):
    logger.info(message)


def warning(message):
    logger.info(message)

