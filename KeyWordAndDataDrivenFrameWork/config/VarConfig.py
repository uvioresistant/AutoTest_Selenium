#!usr/bin/env python
#-*- coding:utf-8 -*-
"""
@author:fengg
@file: VarConfig.py
@time: 2020/07/11
"""
import os


ieDriverFilePath = "c:\\IEDriverServer"
chromeDriverFilePath = "c:\\ChromeDriverServer"
firefoxDriverFilePath = "c:\\FirefoxDriverServer"


# 获取当前文件所在目录的父目录的绝对路径
parentDirPath = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 异常截图存放目录绝对路径
screenPicturesDir = parentDirPath + "\\exceptionPictures\\"