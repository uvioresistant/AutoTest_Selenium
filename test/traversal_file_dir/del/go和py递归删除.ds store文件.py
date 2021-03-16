#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:fengg
@file:go和py递归删除.ds store文件.py
@time:2021/03/09
"""
import os, sys


def walk(path):
    print("cd dir" + path)
    for item in os.listdir(path):
        try:
            if(item == ".DS_Store"):
                global count
                count = count + 1
                print "find file .Ds_Store"
            else:
                if(os.path.isdir(path + "/" + item)):
                    print " " + path + "/" + item + " is "
                    walk(path+ "/" + item)
                else:
                    print " " + path + "/" + item + " is "
        except OSError, e:
            print e


if __name__ == "__main__":
    count = 0
    if(len(sys.argv)>1):
        root_dir = sys.argv[1]
    else:
        root_dir = os.getcwd()
    walk(root_dir)
    print "\n total number: " + str(count)