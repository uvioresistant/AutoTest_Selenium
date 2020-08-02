#!usr/bin/env python
#-*- coding:utf-8 -*-
"""
@author:fengg
@file: LoginPage.py
@time: 2020/07/11
"""
# import time
#
# from selenium import webdriver
# from util.ObjectMap import getElement, getElements
#
#
# def func():
#     pass
#
#
# class LoginPage():
#     def __init__(self, driver):
#         self.driver = driver
#
#     def switchToFrame(self):
#         self.driver.switch_to.frame("x - URS - iframe")
#
#     def switchToDefaultFrame(self):
#         self.driver.switch_to.default_content()
#
#     def userNameObj(self):
#         try:
#             # 获取登录页面的用户名输入框页面对象，并返回给调用者
#             elementObj = getElement(self.driver, "xpath", '//*[@id="auto-id-1594456531823"]')
#             return elementObj
#         except Exception as e:
#             raise e
#
#     def passWordObj(self):
#         try:
#             # 获取登录页面的密码输入框页面对象，并返回给调用者
#             elementObj = getElement(self.driver, "xpath", '//*[@id="auto-id-1594456531826"]')
#             return elementObj
#         except Exception as e:
#             raise e
#
#     def loginButton(self):
#         try:
#             # 获取登录页面的登录按钮输入框页面对象，并返回给调用者
#             elementObj = getElement(self.driver, 'id', 'dologin')
#             return elementObj
#         except Exception as e:
#             raise e


from util.ObjectMap import *
from util.ParseConfigurationFile import ParseConfigFile


def func():
    pass


class LoginPage(object):
    def __init__(self, driver):
        self.driver = driver
        self.parseCF = ParseConfigFile()
        self.loginOptions = self.parseCF.getItemsSection("163mail_login")
        print self.loginOptions

    def switchToFrame(self):
        try:
            # 从定位表达式配置文件中读取frame的定位表达式
            locatorExpression = self.loginOptions["loginPage.frame".lower()].split(">")[1]
            self.driver.switch_to.frame(locatorExpression)
        except Exception as e:
            raise e

    def switchToDefaultFrame(self):
        try:
            self.driver.switch_to.default_content()
        except Exception as e:
            raise e

    def userNameObj(self):
        try:
            # 从定位表达式配置文件中，读取定位用户名输入框的定位方式和表达式
            locateType, locatorExpression = self.loginOptions["loginPage.username".lower()].split(">")
            # 获取登录页面的用户名输入框页面对象，并返回给调用者
            elementObj = getElement(self.driver, locateType, locatorExpression)
            return elementObj
        except Exception as e:
            raise e

    def passWordObj(self):
        try:
            # 从定位表达式配置文件中读取定位密码输入框的定位方式和表达式
            locateType, locatorExpression = self.loginOptions["loginPage.password".lower().split(">")]
            # 获取登录页面的密码输入框页面对象，并返回给调用者
            elementObj = getElement(self.driver, locateType, locatorExpression)
            return elementObj
        except Exception as e:
            raise e

    def loginButton(self):
        try:
            # 从定位表达式配置文件中读取定位登录按钮的定位方式和表达式
            locateType, locatorExpression = self.loginOptions["loginPage.loginbutton".lower().split(">")]
            # 获取登录页面的登录按钮输入框页面对象，并返回给调用者
            elementObj = getElement(self.driver, locateType, locatorExpression)
            return elementObj
        except Exception as e:
            raise e



if __name__ == "__main__":
    # 测试代码
    from selenium import webdriver
    import time
    driver = webdriver.Chrome(executable_path="F:\\Chrome\\chromedriver.exe")
    driver.get("https://mail.163.com/")
    time.sleep(5)
    login = LoginPage(driver)
    login.switchToFrame()
    # 输入登录用户名
    login.userNameObj().send_keys("xxxx")
    # 输入登录密码
    login.passWordObj().send_keys("xxxx")
    login.loginButton().click()
    login.switchToDefaultFrame()
    assert u"未读邮件" in driver.page_source
    driver.quit()


