#!usr/bin/env python
#-*- coding:utf-8 -*-
"""
@author:fengg
@file: AddContactPersonAction.py
@time: 2020/07/20
"""
from pageObjects.HomePage import HomePage
from pageObjects.AddressBookPage import AddressBookPage
import traceback
import time


class AddContactPerson(object):

    def __init__(self):
        print "add contact person."

    @staticmethod
    def add(driver, contactName, contactEmail, isStar, contactPhone, contactComment):
        try:
            # 创建主页实例对象
            hp = HomePage(driver)
            hp.addressLink().click()
            time.sleep(3)
            # 创建添加联系人页实例对象
            apb = AddressBookPage(driver)
            apb.createContactPersonButton().click()
            if contactName:
                # 非必填项
                apb.contactPersonName().send_keys(contactName)
                # 必填项
                apb.contactPersonEmail().send_keys(contactEmail)
                if isStar == u"是":
                    apb.starContacts().click()
                if contactPhone:
                    # 非必填项
                    apb.contactPersonMobile().send_keys(contactPhone)
                if contactComment:
                    apb.contactPersonComment().send_keys(contactComment)
                apb.saveContacePerson().click()
        except Exception as e:
            # 打印堆栈异常信息
            print traceback.print_exc()
            raise e


if __name__ == "__main__":
   from LoginAction import LoginAction
   from selenium import webdriver
   import time
   # 启动Firefox浏览器
   driver = webdriver.Chrome(executable_path="c:\\choromedriver")
   # 访问163邮箱首页
   driver.get("http://mail.163.com")
   # driver.maximize_window()
   time.sleep(5)
   LoginAction.login(driver, "xxx", "xxx")
   time.sleep(5)
   AddContactPerson.add(driver, u"张三", "zs@qq.com", u"是", "", "")
   time.sleep(3)
   assert u"张三" in driver.page_source
   driver.quit()
