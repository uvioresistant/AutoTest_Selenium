#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:fengg
@file:py+django文件下载.py
@time:2021/03/16
"""

# 后台处理函数
def downloadFile(req):
    filename = basePath + req.GET['url']
    def file_iterator(file_name, chunk_size=512):
        with open(file_name) as f:
            while True:
                c = f.read(chunk_size)
                if c:
                    yield c
                else:
                    break
        response = StreamingHttpResponse(file_iterator(filename))
        response['Content-Type'] = 'application/octet-stream'
        response['Content-Dispostion'] = 'attachment;filename="{0}"'.format(filename)
    return response


# 前台使用函数
# 1.a标签调用函数传入路径
# <a href='/downloadFile/url=路径'>

# 2.button标签调用jq方法调用后台函数
# <input type='button' class='download'>

# 下载按钮点击事件
# $("body").on("click", ".download", function(){3 location.href="/downloadFile/?url=" + 路径;});




if __name__ == "__main__":
    pass





















