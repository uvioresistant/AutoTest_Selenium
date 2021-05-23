#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:fengg
@file:遍历文件的3个方法.py
@time:2021/03/03
"""
# os.path.walk()是一个传统的用法
import os

s = os.sep  # 根据unix或win，s为\或/
root = "G:" + s + "||" + s  # 要遍历的目录


def func(args, dire, fis):  # 回调函数的定义
    for f in fis:
        fname = os.path.splitext(f)  # 分割文件名为名字
        new = fname[0] + 'b' + fname[1]  # 改名字
        os.rename(os.path.join(dire, f), os.path.join(dire, new))

    os.path.walk(root, func, ())  # 遍历


# os.walk()，此种方式可以递归遍历所有的文件，可以自顶向下，或自底向上遍历整个文件树，
# 返回一个含有3个元素的tuple：(dirpath, dirnames, filenames),返回一个generater，调用时一定要放到for循环中
import os

s = os.sep
root = "G:" + s + "||" + s

for rt, dirs, files in os.walk(root):
    for f in files:
        fname = os.path.splitext(f)
        new = fname[0] + 'b' + fname[1]
        os.rename(os.path.join(rt, f), os.path.join(rt, new))


# listdir，可使用os模块下的几个方法组合起来进行遍历
import os
s = os.sep
root = "G:" + s + "||" + s

for i in os.listdir(root):  # i是目录或文件名，不是完整的路径，使用时要结合os.path.join()方法还原完整路径
    if os.path.isfile(os.path.join(root, i)):
        print i

# 列出目录，然后判断是不是文件夹，不是的话，直接返回文件路径，是的话，递归调用
import os
def walk_dir2(dirname):
    for d in os.listdir(dirname):
        path = os.path.join(dirname, d)
        if os.path.isdir(path):
            for f in walk_dir2(path):
                yield f  # 由于函数中使用了yield,所以会被认为是一个generater，递归调用时也需要放到for循环中，否则函数并不会真正执行
            else:
                yield path

if __name__ == "__main__":
    pass
