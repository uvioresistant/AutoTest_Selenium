#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:fengg
@file:遍历zip文件输出名称时乱码的解决方法.py
@time:2021/03/03
"""
"""
win中使用py2.7遍历zip后，输出文件名等信息，console打印的中文及一些标点出现乱码，win的编码为cp936，
print()函数要提前编码成win能识别的编码
"""
import zipfile


def listzipfilesinfo(path):
    z = zipfile.ZipFile(path, 'r')
    try:
        for filename in z.namelist():
            bytes = z.read(filename)
            print('File:%s Size:%s' % (unicode(filename, 'cp936').decode('utf-8'), len(bytes)))  # decode可以去掉
    finally:
        z.close()


if __name__ == "__main__":
    listzipfilesinfo('G:\\work_file\\AutoTest_From_Git\\test\\traversal_file_dir\\test.zip')
