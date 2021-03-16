#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:fengg
@file:用py删除java文件头上版权信息.py
@time:2021/03/09
"""
import os
import sys


def delHeader(filepath):
    if os.path.exists(filepath):
        file = open(filepath)
        lines = file.readlines()
        beforeTag = True
        writer = open(filepath, 'w')
        for line in lines:
            if 'package' in line:
                beforeTag = False
                if beforeTag == False:
                    writer.write(line)


if __name__ == "__main__":
    path = "G:\\work_file\\AutoTest_From_Git\\test\\traversal_file_dir\\del\\Temp\\Temporary Internet Files"
    list = os.walk(path, True)
    for dir in list:
        files = dir[2]
        for file in files:
            if '.java' in file:
                filepath = os.path.join(dir[0], file)
                print filepath
                delHeader(filepath)
    print 'Complete!!!!!'
