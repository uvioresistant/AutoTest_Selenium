#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:fengg
@file:遍历指定文件及文件夹.py
@time:2021/03/02
"""
import os, time


# 将文件属性中的时间改为2020-1-1 00:00:00 格式
def format_time(local_time):
    endtime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(local_time))
    return endtime


def searchdir(arg, dirname, names):
    for filespath in names:
        # 得到文件路径
        fullpath = os.path.join(dirname, filespath)
        # 得到文件属性
        statinfo = os.stat(fullpath)
        # 文件大小
        sizefile = statinfo.st_size
        # 创建时间
        createtime = format_time(statinfo.st_ctime)
        # 修改时间
        maketime = format_time(statinfo.st_mtime)
        # 浏览时间
        readtime = format_time(statinfo.st_mtime)
        # 判断是文件夹还是文件
        if os.path.isdir(fullpath):
            filestat = 'DIR'
        else:
            filestat = 'FILE'
        open('G:\\work_file\\AutoTest_From_Git\\test\\traversal_file_dir\\test.txt', 'r+').write(
            '[%s] 路径: %s '
            '文件大小(B): %s '
            '创建时间: %s '
            '修改时间: %s '
            '浏览时间: %s\r\n' % (filestat, fullpath, sizefile, createtime, maketime, readtime))

if __name__ == "__main__":
    # paths = "G:\\work_file\\AutoTest_From_Git\\test\\traversal_file_dir\\"
    paths = "G:\\work_file\\AutoTest_From_Git\\test"
    os.path.walk(paths, searchdir, ())
