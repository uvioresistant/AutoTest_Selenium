#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:fengg
@file:ObjectMap.py
@time:2020/08/07
"""
from selenium.webdriver.support.ui import WebDriverWait

# 获取单个页面元素对象
def getElement(driver, locationType, locatorExpression):
    try:
        element = WebDriverWait(driver, 30).until(lambda x: x.find_element(by=locationType, value=locatorExpression))
        return element
    except Exception as e:
        raise e

# 获取多个相同页面元素对象，以list返回
def getElements(driver, locationType, locatorExpression):
    try:
        elements = WebDriverWait(driver, 30).until(lambda x: x.find_element(by=locationType, value=locatorExpression))
        return elements
    except Exception as e:
        raise e


if __name__ == '__main__':
    from selenium import webdriver
    # 进行单元测试
    driver = webdriver.Firefox(executable_path="c:\\geckodriver.exe")
    driver.get("http://www.baidu.com")
    searchBox = getElement(driver, "id", "kw")
    # 打印页面对象的标签名
    print searchBox.tag_name
    aList = getElement(driver, "tag name", "a")
    print len(aList)
    driver.quit()