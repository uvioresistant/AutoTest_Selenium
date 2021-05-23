#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:fengg
@file:采集博客中上传的QQ截图.py
@time:2021/03/16
"""
import urllib2
from bs4 import BeautifulSoup
import re
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

baseurl = "//www.jb51.net/dont-worry.html"
# 起始地址是第一篇文章的地址，通过该文章的页面就可以使用BeautifulSoup模块来获取上一篇文章的地址
file = open(r"E:\123.txt", "a")


def pageloop(url):
    page = urllib2.urlopen(url)
    soup = BeautifulSoup(page)
    img = soup.findAll(['img'])
    if img == []:
        print "当前页面没有图片"
        return
    else:
        for my_img in img:
            link = my_img.get('src')
            print link
            pattern = re.compile(r"\QQ\S*[0-9]*png")
            bad_img = pattern.findall(str(link))
            if bad_img:
                print url
                file.write(link + '\n')
                file.write(url + '\n')


def get_then_exit_page(url):
    pageloop(url)
    page = urllib2.urlopen(url)
    soup = BeautifulSoup(page)
    for spanclass in soup.findAll(attrs={"class": "article-nav-prev"}):
        if spanclass.find('article-nav-prev') != -1:
            pattern = re.compile(r"//www.jb51.net/\S*html")
            pageurl = pattern.findall(str(spanclass))
            for i in pageurl:
                get_then_exit_page(i)


if __name__ == "__main__":
    get_then_exit_page(baseurl)
    print "the end!"
    file.close()




























