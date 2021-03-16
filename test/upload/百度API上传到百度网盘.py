#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:fengg
@file:百度API上传到百度网盘.py
@time:2021/03/16
"""
import urllib
import urllib2


__author__ = 'Administrator'
from poster.encode import multipart_encode
from poster.streaminghttp import register_openers


register_openers()


def upload(fileName):
    datagen, headers = multipart_encode({"file": open("G:\\work_file\\AutoTest_From_Git\test\\upload\\test\\%s" % fileName, "rb")})
    baseurl = "https://pcs.baidu.com/rest/2.0/pcs/file?"
    args = {
        "method": "upload",
        "access_token": "a7bxxxxx",
        "path": "/apps/ResourceSharing/%s" %fileName
    }
    encode_args = urllib.urlencode(args)
    url = baseurl + encode_args

if __name__ == "__main__":
    upload("host.txt")