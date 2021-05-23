#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:fengg
@file:删除指定类型(或非指定)的文件.py
@time:2021/03/04
"""
# 删除目录下非源码文件
import os
import string


def del_files(dir, topdown=True):
    for root, dirs, files in os.walk(dir, topdown):
        for name in files:
            pathname = os.path.splitext(os.path.join(root, name))
            if pathname[1] != ".py" and pathname[1] != ".cpp" and pathname[1] != ".h":
                os.remove(os.path.join(root, name))
                print(os.path.join(root, name))


if __name__ == "__main__":
    dir = os.getcwd() + "\\Temp"
    print(dir)
    del_files(dir)
    os.removedirs(dir)

