#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:fengg
@file:获得文件创建时间和修改时间.py
@time:2021/03/03
"""
import os.path
import time
import exceptions


class TypeError(Exception):
    pass


if __name__ == "__main__":
    if (len(os.sys.argv) < 1):
        raise TypeError()
    else:
        print("os.sys.argv[0]: %s" % os.sys.argv[0])
    f = os.sys.argv[0]
    mtime = time.ctime(os.path.getmtime(f))
    ctime = time.ctime(os.path.getctime(f))
    print("Last modified: %s, last created time: %s" (mtime, ctime))