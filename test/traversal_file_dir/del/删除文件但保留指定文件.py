#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:fengg
@file:删除文件但保留指定文件.py
@time:2021/03/04
"""
import os
import os.path


def DeleteFiles(path, fileList):
    '''
    :param path: 指定更新文件的存放目录
    :param fileList: 通过list存放希望保留的文件，及该文件路径
    :return:
    '''
    for parent, dirnames, filenames in os.walk(path):
        FullPathList = []
        DestPathList = []
        for x in fileList:
            DestPath = path + x
            DestPathList.append(DestPath)
        for filename in filenames:
            FullPath = os.path.join(parent, filename)
            FullPathList.append(FullPath)
        for xlist in FullPathList:
            if xlist not in DestPathList:
                os.remove(xlist)


if __name__ == "__main__":
    DeleteFiles("G:\\work_file\\AutoTest_From_Git\\test\\traversal_file_dir\\del\\Temp\\", ["Temporary Internet Files\\test2.py", "Temporary Internet Files\\test.py"])