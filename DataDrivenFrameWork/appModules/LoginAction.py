#!usr/bin/env python
#-*- coding:utf-8 -*-
"""
@author:fengg
@file: LoginAction.py
@time: 2020/07/11
"""
from pageObjects.LoginPage import LoginPage


class LoginAction():
    def __init__(self):
        print "login..."

    @staticmethod
    def login(driver, username, password):
        try:
            login = LoginPage(driver)
            # 将当前焦点切换到登录模块的frame中, 以便能进行后续登录操作
            login.switchToFrame()
            # 输入登录用户名
            login.userNameObj().sendkey(username)
            # 输入登录密码
            login.passWordObj().sendkey(password)
            # 单击登录按钮
            login.loginButton().click()
            # 切回到默认窗体
            login.switchToDefaultFrame()
        except Exception as e:
            raise e


if __name__ == "__main__":
    from selenium import webdriver
    import time
    # 启动Chrome
    driver = webdriver.Chrome(executable_path="F:\\Chrome\\chromedriver.exe")
    # 访问163邮箱首页
    driver.get("https://mail.163.com/")
    time.sleep(5)
    LoginAction.login(driver, username="xxx", password="xxx")
    time.sleep(5)
    driver.quit()
