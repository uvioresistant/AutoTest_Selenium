#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:fengg
@file:创建迅雷任务及创建多个文件.py
@time:2021/03/03
"""
"""
其实不是真的创建了批量任务，而是用py创建一个文本文件，每行一个要下载的链接，
然后打开迅雷，复制文本文件的内容，迅雷检测到剪切板变化，弹出下载全部链接的对话框
py分析网页，如下载某页中的全部pdf链接
"""
from __future__ import unicode_literals
from bs import BeautifulSoup
import requests
import codecs

r = requests.get('you url')
s = BeautifulSoup(r.text)
links = s.findall('a')
pdfs = []
for link in links:
    href = link.get('href')
    if href.endswith('.pdf'):
        pdfs.append(href)
    with open('you file', 'w', 'gbk') as f:
        for pdf in pdfs:
            f.write(pdf + '\r\n')

# 使用py创建多个文件
import os
import time


def nsfile(s):
    '''The number of new expected documents'''
    b = os.path.exists("G:\\work_file\\AutoTest_From_Git\\test\\traversal_file_dir\\遍历文件夹并删除特定格式文件.py")
    if b:
        print("File Exist!")
    else:
        os.mkdir("G:\\work_file\\AutoTest_From_Git\\test\\traversal_file_dir\\遍历文件夹并删除特定格式文件.py")
    # 生成文件
    for i in range(1, s + 1):
        localTime = time.strftime("%Y%m%d%H%M%S", time.localtime())
        filename = "G:\\work_file\\AutoTest_From_Git\\test\\traversal_file_dir\\" + localTime + ".txt"
        f = open(filename, 'ab')
        test_note = '测试文件'
        f.write(test_note)
        f.close()
    # 输出第几个文件和对应的文件名称
        print("file" + "" + str(i) + ":" + str(localTime) + ".txt")
        time.sleep(1)
    print("ALL Down")
    time.sleep(1)


if __name__ == "__main__":
    s = input("请输入需要生成的文件数: ")
    nsfile(s)
