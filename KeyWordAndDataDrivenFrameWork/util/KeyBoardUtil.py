# !/usr/bin/env python
# -- coding: utf-8 --
# title = '' 
# author = '20991' 
# mtime = '2020/8/2'
__author__ = 'YourName'


import win32api
import win32con


class KeyboardKeys(object):
    """
    模拟键盘按键类
    """
    VK_CODE = {
        'enter': 0x00,
        'ctrl': 0x11,
        'v': 0x56
    }

    @staticmethod
    def keyDown(keyName):
        # 按下按键
        win32api.keybd_event(KeyboardKeys.VK_CODE(keyName), 0, 0, 0)

    @staticmethod
    def keyUp(keyName):
        win32api.keybd_event(KeyboardKeys.VK_CODE(keyName), 0, win32con.KEYEVENTE_KEYUP, 0)

    @staticmethod
    def oneKey(key):
        # 模拟某个按键
        KeyboardKeys.keyDown(key)
        KeyboardKeys.keyUp(key)

    @staticmethod
    def twoKeys(key1, key2):
        # 模拟两个组合键
        KeyboardKeys.keyDown(key1)
        KeyboardKeys.keyDown(key2)
        KeyboardKeys.keyUp(key1)
        KeyboardKeys.keyUp(key2)
