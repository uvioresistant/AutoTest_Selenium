#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:fengg
@file:使用unittest和ddt进行数据驱动.py
@time:2021/02/23
"""
from selenium import webdriver
import unittest, time
import logging, traceback
import ddt
from selenium.common.exceptions import NoSuchElementException

# 初始化日志对象
logging.basicConfig(
    # 日志级别
    level=logging.INFO,
    # 日志格式
    # 时间、代码所在文件名、代码行号、日志级别名字、日志信息
    format='%(asctime)s %(filenames[line: %(lineno)d] % (levelname)s %(message)s',
    # 打印日志的时间
    datefmt='%a, %d %b %Y %H: %M: %S',
    # 日志文件存放的目录(目录必须存在)及日志文件名
    filename='G:\work_file\AutoTest_From_Git\DataDrivenFrameWork',
    # 打开日志文件的方式
    filemode='w'
)

@ddt.ddt
class TestDemo(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Chrome(executable_path="F:\Chrome\chromedriver")
    # @ddt.data接收一个可迭代类型，以此来判断需要执行的次数，多组测试数据间以逗号隔开，如@ddt.ddt(3,1,5,6),多个数据需存于列表中
    @ddt.data([u"神奇动物在哪里", u"叶次"],
              [u"疯狂动物城", u"古德温"],
              [u"大话西游月光宝盒", u"周星驰"])
    @ddt.unpack # 每组数据中的数据与测试方法中定义的形参个数即顺序一一对应，@unpack进行修饰，对测试数据进行解包，将每组数据中的第一个数据传给testdata，第二个数据传给expectdata
    def test_dataDrivenByObj(self, testdata, expectdata):
        url = "http://www.baidu.com"
        self.driver.get(url)
        self.driver.implicitly_wait(10)
        try:
            self.driver.find_element_by_id("kw").send_keys(testdata)
            self.driver.find_element_by_id("su").click()
            time.sleep(3)
            self.assertTrue(expectdata in self.driver.page_source)
        except NoSuchElementException, e:
            logging.error(u"查找的页面元素不存在，异常堆栈信息: " + str(traceback.format_exc()))
        except AssertionError, e:
            logging.info(u'搜索 %s ,期望 %s ,失败' % (testdata, expectdata))
        except Exception, e:
            logging.error(u'未知错误,错误信息:' + str(traceback.format_exc()))
        else:
            logging.info(u"搜索 %s, 期望 %s 通过" % (testdata, expectdata) )

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
