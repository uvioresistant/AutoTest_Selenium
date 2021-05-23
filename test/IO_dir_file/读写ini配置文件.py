#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:fengg
@file:读写ini配置文件.py
@time:2021/03/01
"""
# # ConfigParser模块是py自带的读取配置文件的模块，可以方便的读取配置文件
# # test.ini:
# # [info]  # []中的info是这段配置的名字
# # age = 21  # age、name都是属性
# # name = chen
# # gender = male
#
from __future__ import with_statement
import ConfigParser

config = ConfigParser.ConfigParser()    # 得到一个配置config对象
with open("testcfg.cfg", "rw") as cfgfile:  # 打开一个配置文件cfgfile
    config.readfp(cfgfile)  # 用readfp()读取这个文件，配置的内容就读到config对象里面了
    name = config.get("info", "name")   # 读取值，get()返回文本
    age = config.getint("info", "age")  # getint()返回整数
print name
print age
config.set("info", "gender", "male")    # 使用set(段名, 变量名, 值)设置变量
config.set("info", "age", "21")
age = config.get("info", "age")
print name
print age


# import configparser as ConfigParser # py3中使用configparser
import ConfigParser
import os


class ReadWriteConfFile:
    currentDir = os.path.dirname(__file__)
    filepath = currentDir + os.path.sep + "inetMsgConfigure.ini"

    @staticmethod
    def getConfigParser():
        cf = ConfigParser.ConfigParser()
        cf.read(ReadWriteConfFile.filepath)
        return cf

    @staticmethod
    def writeConfigParser(cf):
        f = open(ReadWriteConfFile.filepath, "w")
        cf.write(f)
        f.close()

    @staticmethod
    def getSectionValue(section, key):
        cf = ReadWriteConfFile.getConfigParser()
        return cf.get(section, key)

    @staticmethod
    def addSection(section):
        cf = ReadWriteConfFile.getConfigParser()
        allSections = cf.sections()
        if section in allSections:
            return section
        else:
            cf.add_section(section)
            ReadWriteConfFile.writeConfigParser(cf)

    @staticmethod
    def setSectionValue(section, key, value):
        cf = ReadWriteConfFile.getConfigParser()
        cf.set(section, key, value)
        ReadWriteConfFile.writeConfigParser(cf)


if __name__ == "__main__":
    ReadWriteConfFile.addSection('messages')
    ReadWriteConfFile.setSectionValue('messages', 'name', 'sophia')
    x = ReadWriteConfFile.getSectionValue('messages', '1000')
    print x
