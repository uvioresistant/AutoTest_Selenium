#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:fengg
@file:使用os和os.walk遍历文件夹.py
@time:2021/03/03
"""
import os

if __name__ == '__main__':
    try:
        for root, dirs, files in os.walk("G:" + os.sep + 'Python'):
            print('---directory<' + root + '>')
            for d in dirs:
                print(d)
                for f in files:
                    print(f)
    except OSError as e:
        print(os.strerror(e.errno))
