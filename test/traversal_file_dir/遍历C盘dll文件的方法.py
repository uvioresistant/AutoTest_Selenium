#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:fengg
@file:遍历C盘dll文件的方法.py
@time:2021/03/03
"""
import os
import fnmatch


def main():
    f = open('dll_list.txt', 'w')
    for root, dirs, files in os.walk("c:\\"):
        for name in files:
            if fnmatch.fnmatch(name, '*.dll'):
                f.write(os.path.join(root, name))
                f.write('\n')
    f.close()
    print 'done'


if __name__ == "__main__":
    main()
