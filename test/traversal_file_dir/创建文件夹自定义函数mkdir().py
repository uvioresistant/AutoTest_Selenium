#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:fengg
@file:创建文件夹自定义函数mkdir().py
@time:2021/03/03
"""
"""
主要涉及到三个函数：
1.os.path.exists(path): 判断一个目录是否存在
2.os.makedirs(path): 多层创建目录,和mkdir()的区别是：当父目录不存在的时候，os.mkdir不会创建，os.makedirs则会创建父目录
3.os.mkdir(path) 创建目录
"""
import os


def mkdir_myself(path):
    # 去除首位空格
    path = path.strip()
    # 去除尾部\符号
    path = path.rstrip("\\")
    # 判断路径是否存在
    isExists = os.path.exists(path)
    if not isExists:
        # 如果不存在则创建目录
        print(path + '创建成功')
        # 创建目录操作函数
        os.makedirs(path)
        return True
    else:
        # 如果目录存在则不创建，并提示目录已存在
        print(path+'目录已存在')
        return False


if __name__ == "__main__":
    # 定义要创建的目录
    mkpath = "G:\\work_file\\AutoTest_From_Git\\test\\traversal_file_dir\\del"
    mkdir_myself(mkpath)