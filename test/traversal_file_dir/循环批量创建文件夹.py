#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:fengg
@file:循环批量创建文件夹.py
@time:2021/03/03
"""
import os


base = "G:\\work_file\\AutoTest_From_Git\\test\\traversal_file_dir"
i = 1
for j in range(100):
    file_name = base + str(i)
    os.mkdir(file_name)
    i = i + 1


if __name__ == "__main__":
    pass