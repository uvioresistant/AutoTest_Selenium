# !/usr/bin/env python
# -- coding: utf-8 --
# title = '' 
# author = '20991' 
# mtime = '2020/7/25'
__author__ = 'YourName'

import sys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class WaitUtil(object):

    def __init__(self, driver):
        self.locationTypeDict = {
            "xpath": By.XPATH,
            "id": By.ID,
            "name": By.NAME,
            "class_name": By.CLASS_NAME,
            "tag_name": By.TAG_NAME,
            "link_test": By.LINK_TEXT,
            "partial_link_text": By.PARTIAL_LINK_TEXT
        }
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 30)

    def presenceOfElementLocated(self, locatorMethod, locatorExpression, *arg):
        """显式等待页面元素出现在DOM中，但并不一定可见，存在则返回该页面元素对象"""
        try:
            if self.locationTypeDict.has_key(locatorMethod.lower()):
                self.wait.until(
                    EC.presence_of_all_elements_located((
                        self.locationTypeDict[locatorMethod.lower()],
                        locatorExpression)))
        except Exception as e:
            raise e

    def frameToBeAvailableAndSwitchToIt(self, locationType, locatorExpression, *arg):
        '''检查frame是否存在，存在则切换进frame控件中'''
        try:
            self.wait.until(EC.frame_to_be_available_and_switch_to_it((self.locationTypeDict[locationType.lower()],
                                                                       locatorExpression)))
        except Exception as e:
            raise e

    def visibilityOfElementLocated(self, locationType, locatorExpression, *arg):
        '''显示等待页面元素出现在DOM中，并且可见，存在则返回该页面元素对象'''
        try:
            self.wait.until(
                EC.visibility_of_all_elements_located((
                    self.locationTypeDict[locationType.lower()], locatorExpression
                ))
            )
        except Exception as e:
            raise e


if __name__ == '__main__':
    from selenium import webdriver
    driver = webdriver.Chrome(executable_path="c:\\chromedriver")
    driver.get("http://mail.163.com")
    waitUtil = WaitUtil(driver)
    waitUtil.frameToBeAvailableAndSwitchToIt("id", "x-URS-iframe")
    waitUtil.visibilityOfElementLocated("xpath", "//input[@name='email']")
    waitUtil.presenceOfElementLocated("xpath", "//input[@name='email']")
    driver.quit()