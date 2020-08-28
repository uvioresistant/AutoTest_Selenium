#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:fengg
@file:test_HighWebDriver.py
@time:2020/08/27
"""
from selenium import webdriver
from selenium.common.exceptions import WebDriverException
import unittest
import traceback
import time

class TestDemo(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path= "F:\\Chrome\\chromedriver")

    def test_executeScript(self):
        url = "http://www.baidu.com"
        self.driver.get(url)
        # 构造JS查找百度首页的搜索输入框的代码字符串
        searchInputBoxJS = "document.getElementById('kw').value='伟大的卫国战争';"
        # 构造JS查找百度首页的搜索按钮的代码字符串
        searchButtonJS = "document.getElementById('su').click()"
        try:
            # 通过JS代码在百度首页搜索输入框中输入'伟大的卫国战争'
            self.driver.execute_script(searchInputBoxJS)
            time.sleep(2)
            # 通过JS代码单击百度首页上的搜索按钮
            self.driver.execute_script(searchButtonJS)
            time.sleep(2)
            self.assertTrue(u"百度百科" in self.driver.page_source)
        except WebDriverException, e:
            print u"在页面中没有找到要操作的页面元素", traceback.print_exc()
        except AssertionError, e:
            print u"页面不存在断言的关键字串"
        except Exception, e:
            print traceback.print_exc()

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()