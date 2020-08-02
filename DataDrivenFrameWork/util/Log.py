# !/usr/bin/env python
# -- coding: utf-8 --
# title = '' 
# author = '20991' 
# mtime = '2020/7/25'
__author__ = 'YourName'

import logging
import logging.config
from config.VarConfig import parentDirPath

# 读取日志配置文件
logging.config.fileConfig(parentDirPath + u"\config\Logger.conf")
# 选择一个日志格式
logger = logging.getLogger("example02") # 或者exxample01

def debug(message):
    # 定义debug级别的日志打印方法
    logger.debug(message)


def info(message):
    # 定义info级别的日志打印方法
    logger.info(message)


def warning(message):
    # 定义warning级别的日志打印方法
    logger.warning(message)


def main(argv):
    """Do someting..."""
    return 0


if __name__ == '__main__':
    exit(main(sys.argv[1:]))