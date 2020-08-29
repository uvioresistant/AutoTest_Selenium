#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:fengg
@file:Calc.py
@time:2020/08/29
"""
import unittest
import HTMLTestRunner
import math


class Calc(object):
    def add(self, x, y, *d):
        result = x + y
        for i in d:
            result += i
        return result

    def sub(self, x, y, *d):
        result = x - y
        for i in d:
            result -= i
        return result

    def mul(self, a, b):
        return a * b


class SuiteTestCalc(unittest.TestCase):
    def setUp(self):
        self.c = Calc()

    @unittest.skip("skipping")
    def test_Sub(self):
        print "sub"
        self.assertEqual(self.c.sub(100, 34, 6), 60, '求差结果错误')

    def testAdd(self):
        print "add"
        # 检测math模块是否存在pow属性
        self.assertEqual(self.c.add(1, 32, 56), 89, '求和结果错误！')


class SuiteTestPow(unittest.TestCase):
    def setUp(self):
        self.seq = range(10)

    def test_Pow(self):
        print "Pow"
        self.assertEqual(pow(6, 3), 216, '求幂结果错误')

    def test_hasattr(self):
        print "hasattr"
        # 检测math模块是否存在pow属性
        self.assertTrue(hasattr(math, 'pow'), '检测的属性不存在！')


if __name__ == "__main__":
    suite1 = unittest.TestLoader().loadTestsFromTestCase(SuiteTestCalc)
    suite2 = unittest.TestLoader().loadTestsFromTestCase(SuiteTestPow)
    suite = unittest.TestSuite([suite1, suite2])
    # 定义报告存放路径，支持相对路径
    filename = "G:\\work_file\\AutoTest_From_Git\\project_discover\\test.html"
    # 以二进制方式打开文件，准备写
    fp = file(filename, 'wb')
    # 使用HTMLTestRunner配置参数，输出报告路径、报告标题、描述
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='Report_title', description='Report_description')
    runner.run(suite)