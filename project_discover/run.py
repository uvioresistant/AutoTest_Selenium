#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:fengg
@file:run.py
@time:2020/08/29
"""
import unittest


if __name__ == "__main__":
    # 加载当前目录下所有有效的测试模块, "."表示当前目录
    testSuite = unittest.TestLoader().discover('.')
    unittest.TextTestRunner(verbosity=2).run(testSuite)