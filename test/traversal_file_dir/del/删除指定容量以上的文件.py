#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:fengg
@file:删除指定容量以上的文件.py
@time:2021/03/05
"""
import os, sys
from stat import *


BIG_FILE_THRESHOLD = 1000000
dict1 = {}  # filesize做key, filename做value
dict2 = {}  # filesize做key, filename做value


def treewalk(path):
    try:
        for i in os.listdir(path):
            mode = os.stat(path + "/" + i).st_mode
            if S_ISDIR(mode) == True:
                filename = path + "/" + i
                filesize = os.stat(filename).st_size
                if filesize > BIG_FILE_THRESHOLD:
                    if filesize in dict1:
                        dict2[filename] = filesize
                        dict2[dict1[filesize]] = filesize
                    else:
                        dict1[filesize] = filename
                else:
                    treewalk(path + "/" + i)
    except WindowsError:
        pass


def printdict(finaldict):
    for i_size in finaldict.values():
        print(i_size)
        for j_name in finaldict.keys():
            if finaldict[j_name] == i_size:
                print(j_name)
        print("\n")


if __name__ == "__main__":
    treewalk(sys.argv[1])
    printdict(dict2)