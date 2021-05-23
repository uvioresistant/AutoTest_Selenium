#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:fengg
@file:读写操作与shell变量交互执行.py
@time:2021/03/01
"""
import os


# py执行linux命令
os.system(':>./aa.py')
# 人机交互输入
S = raw_input("input:")
os.environ['S'] = str(S)
# 把字符串S写入文件
output = open('./aa.py', 'a')
output.write(S)
# 关闭文件
output.close()
# 获取文件内容
f = open('./aa.py', 'r')
read = f.read()
# 变量间的转换
os.environ['read'] = str(read)
os.system('$read')
f.close()
var = os.popen('ifconfig').read()
print var


if __name__ == "__main__":
    pass