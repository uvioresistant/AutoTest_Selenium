#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:fengg
@file:创建临时文件夹.py
@time:2021/03/03
"""
import tempfile, os


tempfd, tempname = tempfile.mkstemp('.suffix')
# os.fdopen(tempfd, 'w+')
os.write(tempfd, 'aString')
os.close(tempfd)
os.unlink(tempname)

if __name__ == "__main__":
    pass