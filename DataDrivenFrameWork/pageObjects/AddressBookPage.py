#!usr/bin/env python
#-*- coding:utf-8 -*-
"""
@author:fengg
@file: AddressBookPage.py
@time: 2020/07/12
"""
from util.ObjectMap import *
from util.ParseConfigurationFile import ParseConfigFile


def func():
    pass


class AddressBookPage(object):

    def __init__(self):
        self.driver = driver
        self.parseCF = ParseConfigFile()
        self.addContactsOptions = self.parseCF.getItemsSection("163mail_addContactsPage")
        print self.addContactsOptions

    def createContactPersonButton(self):
        # 获取新建联系人按钮
        try:
            # 从定位表达式配置文件中，读取定位新建联系人按钮的定位方式和表达式
            locateType, locatorExpression = self.addContactsOptions["addContactsPage.createContactsBtn".lower()].split(">")
            # 获取新建联系人按钮页面元素，并返回给调用者
            elementObj = getElement(self.driver, locateType, locatorExpression)
            return elementObj
        except Exception as e:
            raise e

    def contactPersonName(self):
        # 获取新建联系人界面中的姓名输入框
        try:
            # 从定位表达式配置文件中，读取联系人姓名输入框的定位方式和表达式
            locateType, locatorExpression = self.addContactsOptions["addContactsPage.contactPersonName".lower()].split(">")
            # 获取新建联系人界面的，姓名输入框页面元素，并返回给调用者
            elementObj = getElement(self.driver, locateType, locatorExpression)
            return elementObj
        except Exception as e:
            raise e

    def contactPersonEmail(self):
        # 获取新建联系人界面中的电子邮件输入框
        try:
            # 从定位表达式配置文件中，读取联系人邮箱输入框的定位方式和表达式
            locateType, locatorExpression = self.addContactsOptions["addContactsPage.contactPersonEmail".lower()].split(">")
            # 获取新建联系人界面的，邮箱输入框页面元素，并返回给调用者
            elementObj = getElement(self.driver, locateType, locatorExpression)
            return elementObj
        except Exception as e:
            raise e

    def starContacts(self):
        # 获取新建联系人界面中的星标联系人选择框
        try:
            # 从定位表达式配置文件中，读取星标联系人姓名复选框的定位方式和表达式
            locateType, locatorExpression = self.addContactsOptions["addContactsPage.starContacts".lower()].split(">")
            # 获取新建联系人界面的，邮箱输入框页面元素，并返回给调用者
            elementObj = getElement(self.driver, locateType, locatorExpression)
            return elementObj
        except Exception as e:
            raise e

    def contactPersonMobile(self):
        # 获取新建联系人界面中的星标联系人选择框
        try:
            # 从定位表达式配置文件中，读取联系人手机号输入框的定位方式和表达式
            locateType, locatorExpression = self.addContactsOptions["addContactsPage.contactsPersonMobile".lower()].split(">")
            # 获取新建联系人界面的，邮箱输入框页面元素，并返回给调用者
            elementObj = getElement(self.driver, locateType, locatorExpression)
            return elementObj
        except Exception as e:
            raise e

    def contactPersonComment(self):
        # 获取新建联系人界面中的联系人备注信息输入框
        try:
            # 从定位表达式配置文件中，读取联系人备注信息输入框的定位方式和表达式
            locateType, locatorExpression = self.addContactsOptions["addContactsPage.contactsPersonComment".lower()].split(">")
            # 获取新建联系人界面的，联系人备注信息输入框页面元素，并返回给调用者
            elementObj = getElement(self.driver, locateType, locatorExpression)
            return elementObj
        except Exception as e:
            raise e

    def saveContacePerson(self):
        # 获取新建联系人界面中的保存联系人按钮
        try:
            # 从定位表达式配置文件中，读取保存联系人按钮的定位方式和表达式
            locateType, locatorExpression = self.addContactsOptions["addContactsPage.saveContacePerson".lower()].split(">")
            # 获取新建联系人界面的，联系人备注信息输入框页面元素，并返回给调用者
            elementObj = getElement(self.driver, locateType, locatorExpression)
            return elementObj
        except Exception as e:
            raise e



if __name__ == "__main__":
    pass