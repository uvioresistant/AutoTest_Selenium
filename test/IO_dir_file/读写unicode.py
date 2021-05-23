#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:fengg
@file:读写unicode.py
@time:2021/03/01
"""
import os
import codecs


def writefile(fn, v_ls):
    f = codecs.open(fn, 'wb', 'utf-8')
    for i in v_ls:
        f.write(i + os.linesep)
    f.close()

def readfile(fn):
    f = codecs.open(fn, 'r', 'utf-8')
    ls = [line.strip() for line in f]
    f.close()
    for i in ls:
        print(i)


if __name__ == "__main__":
    fn = u'11.txt'
    ls = [u'1.python', u'2.how to pythonic', u'3.python cook', u'python编程']
    writefile(fn,ls)
    readfile(fn)