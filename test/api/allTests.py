#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:fengg
@file:allTests.py
@time:2020/09/17
"""
import time
import HTMLTestRunner
import os
import unittest


def allTestCases():
    '''获取testCase包中所有的测试模块'''
    suite = unittest.defaultTestLoader.discover(
        start_dir=os.path.join(os.path.dirname(__file__), 'testCase'),
        pattern='test_*.py',
        top_level_dir=None
    )
    return suite


def getNowTime():
    '''获取当前时间'''
    return time.strftime('%Y_%m_%d %H_%M_%S')


def run():
    fp = open(os.path.join(os.path.dirname(__file__), 'report', getNowTime() + 'report.html'), 'wb')
    HTMLTestRunner.HTMLTestRunner(
        stream=fp,
        title='接口自动化测试报告',
        description='基于Python语言的接口自动化测试实战',
    ).run(allTestCases())


if __name__ == "__main__":
    pass
