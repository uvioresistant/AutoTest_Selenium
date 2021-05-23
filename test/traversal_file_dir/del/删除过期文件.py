#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:fengg
@file:删除过期文件.py
@time:2021/03/04
"""
import os, glob, time


root = "G:\\work_file\\AutoTest_From_Git\\test\\traversal_file_dir\\del\\"
xDate = '2021-03-05'
print('-' * 50)
for folder in glob.glob(root):
    print(folder)
    for image in glob.glob(folder + '/*.jpg'):
        stats = os.stat(image)
        lastmodDate = time.localtime(stats[8])
        expDate = time.strptime(xDate, '%Y-%m-%d')
        print(image, time.strftime("%m/%d/%y", lastmodDate))
        # check if image-last-modified-date is outdated
        if expDate > lastmodDate:
            try:
                print("Removing", image, time.strftime("(older than %m/%d/%y)", expDate))
                os.remove(image)
            except OSError:
                print("Could not remove", image)
