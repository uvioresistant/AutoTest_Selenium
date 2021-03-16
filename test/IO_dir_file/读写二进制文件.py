#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:fengg
@file:读写二进制文件.py
@time:2021/03/01
"""

# file提供了一个read和write函数，且读写的都是字符串，如只读写char等一个字节的还行，要读写如int，double等多字节数据就不方便了
# 使用struct模块中的pack和unpack函数进行读写
from struct import *
# file = open(r"G:\\work_file\\AutoTest_From_Git\\test\\IO_dir_file\\lol.txt", "wb")
# file.write(pack("idh", 12345, 67.89, 15))
# file.close()

# 再将其读进来
file = open(r"G:\\work_file\\AutoTest_From_Git\\test\\IO_dir_file\\lol.txt", "rb") # wb和rb中的b，一定不可以少
(a, b, c) = unpack("idh", file.read(8+8+2)) # 操作过程中需要注意数据的size，
print a, b, c
file.close()

myfile = open("G:\\work_file\\AutoTest_From_Git\\test\\IO_dir_file\\11.txt", "rb").read(1)
print unpack('c', myfile)
print unpack('b', myfile)

if __name__ == "__main__":
    pass