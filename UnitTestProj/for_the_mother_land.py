#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:fengg
@file:for_the_mother_land.py
@time:2020/08/29
"""
import unittest
from selenium import webdriver
import time

class MotherLand(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="F:\\Chrome\\chromedriver")

    def testSoGou(self):
        self.driver.get("http://sogou.com")
        # 清空搜索输入框默认内容
        self.driver.find_element_by_id("query").clear()
        self.driver.find_element_by_id("query").send_keys(u"WebDriver")
        self.driver.find_element_by_id("stb").click()
        time.sleep(3)
        assert u"python" in self.driver.page_source, "页面中不存在要寻找的关键字!"

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()