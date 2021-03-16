#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:fengg
@file:删除特定文件.py
@time:2021/03/03
"""
import os


def del_files(path):
    for root, dirs, files in os.walk(path):
        for name in files:
            if name.endswith(".CR2"):
                os.remove(os.path.join(root, name))
                print("Delete File: " + os.path.join(root, name))


if __name__ == "__main__":
    path = "G:\\work_file\\AutoTest_From_Git\\test\\traversal_file_dir\\del"
    del_files(path)
