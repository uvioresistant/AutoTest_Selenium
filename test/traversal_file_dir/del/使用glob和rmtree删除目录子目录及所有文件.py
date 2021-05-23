#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:fengg
@file:使用glob和rmtree删除目录子目录及所有文件.py
@time:2021/03/05
"""
import shutil


def retreeExceptionHandler(path, excinfo):
    print("Error" + path)
    print(excinfo[1])

shutil.rmtree(path, ignore_errors=False)


# 使用rmdir和remove等价于rmtree:
import sys, os
ERROR_STR = '''Error removing %(path)s, %(error)s'''


def rmGeneric(path, __func__):
    try:
        __func__(path)
        print 'Removed', path
    except OSError, (errno, strerror):
        print ERROR_STR % {'path': path, 'error': strerror}

def removeall(path):
    if not os.path.isdir(path):
        return
    files = os.listdir(path)
    for x in files:
        fullpath = os.path.join(path, x)
        if os.path.isfile(fullpath):
            f = os.remove
            rmGeneric(fullpath, f)
        elif os.path.isdir(fullpath):
            removeall(fullpath)
            f = os.rmdir
            rmGeneric(fullpath, f)


if __name__ == "__main__":
    path = "G:\\work_file\\AutoTest_From_Git\\test\\traversal_file_dir\\del\\Temp\\Temporary Internet Files"
    removeall(path)





















