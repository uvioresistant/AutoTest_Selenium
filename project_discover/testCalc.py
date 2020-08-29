#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:fengg
@file:testCalc.py
@time:2020/08/29
"""
import unittest
from Calc import Calc


class MyTest(unittest.TestCase):
    c = None

    @classmethod
    def setUpClass(cls):
        print u"单元测试前，创建Calc类的实例"
        cls.c = Calc()

    # 具体的测试用例，一定要以test开头
    def test_add(self):
        print "run add()"
        self.assertEqual(MyTest.c.add(1, 2, 12), 15, 'test add fail')

if __name__ == "__main__":
    pass