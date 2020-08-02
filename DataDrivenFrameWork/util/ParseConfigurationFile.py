#!usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author:fengg
@file: ParseConfigurationFile.py
@time: 2020/07/12
"""
from ConfigParser import ConfigParser
from config.VarConfig import pageElementLocatorPath


class ParseConfigFile(object):

    def __init__(self):
        self.cf = ConfigParser()
        self.cf.read(pageElementLocatorPath)

    def getItemsSection(self, sectionName):
        # 获取配置文件中指定section下的所有option键值对
        # 并以字典类型返回给调用者
        '''
        注：使用self.cf.items(sectionName)获取到的配置文件中的options内容，
        均被转换成小写，如loginPage.frame被转换为了loginpage.frame
        :param sectionName:
        :return:
        '''
        optionsDict = dict(self.cf.items(sectionName))
        return optionsDict

    def getOptionValue(self, sectionName, optionName):
        # 获取指定section下的指定option的值
        value = self.cf.get(sectionName, optionName)
        return value


if __name__ == "__main__":
    pc = ParseConfigFile()
    print pc.getItemsSection("163mail_login")
    print pc.getOptionValue("163mail_login", "loginPage.frame")
