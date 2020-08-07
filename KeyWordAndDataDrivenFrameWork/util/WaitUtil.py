#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:fengg
@file:WaitUtil.py
@time:2020/08/07
"""
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class WaitUtil(object):
    # 映射定位方式的字典对象
    def __init__(self, driver):
        self.locationTypeDict = {
            "xpath": By.XPATH,
            "id": By.ID,
            "name": By.NAME,
            "css_selector": By.CSS_SELECTOR,
            "class_name": By.CLASS_NAME,
            "tag_name": By.TAG_NAME,
            "link_text": By.LINK_TEXT,
            "partial_link_text": By.PARTIAL_LINK_TEXT
        }
        # 初始化driver对象
        self.driver = driver
        # 创建显式等待实例对象
        self.wait = WebDriverWait(self.driver, 30)

    def presenceOfElementLocated(self, locatorMethod, locatorExpression, *args):
        """显式等待页面元素出现在DOM中，但并不一定可见，存在则返回该页面元素对象"""
        try:
            if self.locationTypeDict.has_key(locatorMethod.lower()):
                element = self.wait.until(
                    EC.presence_of_all_elements_located((
                        self.locationTypeDict[locatorMethod.lower()],
                        locatorExpression)))
                return element
            else:
                raise TypeError(u"未找到定位方式，请确认定位方法是否正确")
        except Exception as e:
            raise e

    def frameToBeAvailableAndSwitchToIt(self, locationType, locatorExpression, *args):
        '''检查frame是否存在，存在则切换进frame控件中'''
        try:
            self.wait.until(EC.frame_to_be_available_and_switch_to_it
                            ((self.locationTypeDict[locationType.lower()], locatorExpression)))
        except Exception as e:
            raise e

    def visibilityOfElementLocated(self, locationType, locatorExpression, *args):
        '''显示等待页面元素出现在DOM中，并且可见，存在则返回该页面元素对象'''
        try:
            element = self.wait.until(
                EC.visibility_of_all_elements_located((
                    self.locationTypeDict[locationType.lower()], locatorExpression
                ))
            )
            return element
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