#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:fengg
@file:testFact.py.py
@time:2020/08/29
"""

import unittest
from Calc import Calc


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.num = 5

    def testFactorial(self):
        # 生成一个递增序列
        seq = range(1, self.num + 1)
        # 求阶乘
        res = reduce(lambda x, y: x * y, seq)
        # 断言阶乘结果
        self.assertEqual(res, 120, '断言阶乘结果错误!')


if __name__ == "__main__":
    pass
