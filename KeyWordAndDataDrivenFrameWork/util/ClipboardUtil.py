#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:fengg
@file:ClipboardUtil.py
@time:2020/08/07
"""
# !/usr/bin/env python
# -- coding: utf-8 --
# title = ''
# author = '20991'
# mtime = '2020/8/2'
__author__ = 'YourName'

import win32clipboard as w
import win32con


class Clipboard(object):
    '''
    模拟Windows设置剪贴板
    '''
    # 读取剪贴板
    @staticmethod
    def getText():
        # 打开剪贴板
        w.OpenClipboard()
        # 获取剪贴板中的数据
        d = w.GetClipboardData(win32con.CF_TEXT)
        # 关闭剪贴板
        w.CloseClipboard()
        # 返回剪贴板数据给调用者
        return d

    # 设置剪贴板内容
    @staticmethod
    def setText(aString):
        # 打开剪贴板
        w.OpenClipboard()
        # 清空剪贴板
        w.EmptyClipboard()
        # 将数据aString写入剪贴板
        w.SetClipboardData(win32con.CF_UNICODETEXT, aString)
        # 关闭剪贴板
        w.CloseClipboard()


def main(argv):
    """Do someting..."""
    return 0
