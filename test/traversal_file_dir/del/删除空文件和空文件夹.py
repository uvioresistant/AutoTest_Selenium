#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:fengg
@file:删除空文件和空文件夹.py
@time:2021/03/03
"""
import os, sys


def remove_empty_dir(path):
    print(path)
    while (path[-1] == "\\"):
        path = path[:-1]
    print(path)
    a = {}
    for root, dirs, files in os.walk(path, False):
        if len(files) == 0:
            a[root] = 0
        else:
            for file in files:  # 对文件列表进行扫描
                try:
                    fn = os.path.join(root, file)  # 将路径名和文件名拼接起来
                    size = os.path.getsize(fn)  # 获取文件名大小
                    if size != 0:
                        b = root
                        while (b != path):
                            a[b] = 1
                            b = b.partition("\\")[0]  # 保存上一级目录名
                        a[path] = 1
                    else:
                        try:
                            os.remove(fn)  # 删除文件名为空的文件
                            a[root] = 0
                        except WindowsError:
                            b = root
                            while (b != path):
                                a[b] = 1
                                b = b.partition("\\")[0]
                                a[path] = 1
                except WindowsError:
                    b = root
                    while (b != path):
                        a[b] = 1
                        b = b.partition("\\")[0]
                        a[path] = 1
                        if a[root]:
                            break
    empty_dirs = []
    for i, j in a.items():
        if j == 0:
            print(i)
            empty_dirs.sort(reverse=True)
    for i in empty_dirs:
        try:
            os.rmdir(i)  # 删除目录
            print("%s 删除了!!" % i)
        except WindowsError:
            print("%s 删不掉!!" % i)


if __name__ == "__main__":
    remove_empty_dir("G:\\work_file\\AutoTest_From_Git\\test\\traversal_file_dir\\del\\testtest\\")
