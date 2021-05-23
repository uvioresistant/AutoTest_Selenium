#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:fengg
@file:删除nginx缓存文件.py
@time:2021/03/09
"""
import sys, os
import hashlib


if len(sys.argv) < 2:
    print("未输入地址")
    sys.exit()

path = "G:\\work_file\\AutoTest_From_Git\\test\\traversal_file_dir\\del\\Temp\\Temporary Internet Files"    # 缓存目录
md5v = hashlib.md5(sys.argv[1].encode(encoding='utf-8'))
onep = md5v[31:32]
twop = md5v[29:31]
filename = path + "/" + onep + "/" + twop + "/" + md5v
if os.path.isfile(filename):
    if os.remove(filename) == None:
        print(filename + "==>清楚成功" )
    else:
        print("清除失败")
else:
    print("没有这个缓存文件")



if __name__ == "__main__":
    pass