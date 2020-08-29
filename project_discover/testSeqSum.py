#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:fengg
@file:testSeqSum.py
@time:2020/08/29
"""
import unittest


class MyTestCase(unittest.TestCase):
    def testEqual(self):
        seq = range(11)
        self.assertEqual(sum(seq), 55, "断言列表元素之和结果错误")


if __name__ == "__main__":
    pass