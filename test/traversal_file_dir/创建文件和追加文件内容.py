#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:fengg
@file:创建文件和追加文件内容.py
@time:2021/03/03
"""
# 一、用Py创建一个新文件，内容是从0~9的整数，每个数字占一行:
f = open('f.txt', 'w')
for i in range(0, 10): f.write(str(i) + '\n')
f.close()

# 二、文件内容追加，从0到9的10个随机整数:
import random

f = open('f.txt', 'a')
for i in range(0, 10): f.write(str(random.randint(0, 9)))
f.write('\n')
f.close()

# 三、文件内容追加，从0到9的随机整数，10个数字一行，共10行:
f = open('f.txt', 'a')
for i in range(0, 10):
    for i in range(0, 10): f.write(str(random.randint(0, 9)))
    f.write('\n')
f.close()

# 四、把标准输出定向到文件:
import sys

sys.stdout = open("stdout.txt", "w")

# 实例：查看22端口情况，并将结果写入a.txt
import os
import time
import sys

f = open('a.txt', 'a')
f.write(os.popen('netstat -nltp | grep 22').read())
f.close()

if __name__ == "__main__":
    pass
