#!usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author:fengg
@file: ObjectMap.py
@time: 2020/07/11
"""
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait


# 获取单个页面元素对象
def getElement(driver, locateType, locatorExpression):
    '''
    :param driver:
    :param locateType:
    :param locatorExpression:
    :return:
    '''
    try:
        element = WebDriverWait(driver, 10).until(lambda x: x.find_element(by=locateType, value=locatorExpression))
        return element
    except Exception as e:
        raise 0


# 获取多个相同页面元素对象，以list返回
def getElements(driver, locateType, locatorExpression):
    '''
    :param driver:
    :param locateType:
    :param locatorExpression:
    :return:
    '''
    try:
        elements = WebDriverWait(driver, 10).until(lambda x: x.find_elements(by=locateType, value=locatorExpression))
        return elements
    except Exception as e:
        raise e


if __name__ == "__main__":
    # 进行单元测试
    driver = webdriver.Chrome(executable_path="F:\\Chrome\\chromedriver.exe")
    driver.get("https://www.baidu.com")
    searchBox = getElement(driver, "id", "kw")
    # 打印页面对象的标签名
    print searchBox.tag_name
    aList = getElements(driver, "tag name", "a")
    print len(aList)
    driver.quit()
