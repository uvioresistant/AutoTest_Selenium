#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:fengg
@file:不同编码读写txt文件.py
@time:2021/03/01
"""
import os


# 将执行文件当前目录及文件名写入到name.txt文件中，以utf-8格数保存
filenames = os.listdir(os.getcwd())
out = file("name.txt", "w")
for filename in filenames:
    out.write(filename.decode("gb2312").encode("utf-8"))
out.close()

# 采用ANSI编码保存：out.write(filename)

# 打开文件并写入：引用codecs模块
import codecs
file = codecs.open("lol.txt", "w", "utf-8")
file.write(u"我")
file.close()

# 读取ANSI编码的文本文件和utf-8编码的文件
# print open("Test.txt").read() # 读取ANSI编码文件

# 读取utf-8编码文件(无BOM),把文件改成UTF-8,会出现乱码，需解码
# import codecs
# print open("Test.txt").read().decode("utf-8")

# 读取utf-8编码文件(有BOM):BOM---某些软件保存一个以UTF-8编码的文件时，默认会在文件开始的地方插入三个不可见的字符(0xEF 0xBB 0xBF,即BOM)
# 有些软件可以控制是否插入BOM，如果在有BOM的情况下，读取时需要自己去掉这些字符
import codecs
data = open("Test.txt").read()
if data[:3] == codecs.BOM_UTF8:
    data = data[3:]
print data.decode("utf-8")

# 处理uiniode中文字符串时，必须首先对它调用encode函数，转换成其他编码输出
data = open("test.txt").read() # 打开utf-8个数文件并读取utf-8字符串后
u=data.decode("utf-8")  # 解码变成unicode对象，但会把附加的三个字符同样进行转换，变成一个unicode字符，该字符不能被打印
print u[1:] # 为了正常显示，采用u[1:]的方式，过滤到第一个字符

# 设置py默认编码
import sys
reload(sys)
sys.setdefaultencoding("gb2312")
print sys.getdefaultencoding()

# 如何永久将默认编码设置为utf-8？有两种方法
# 1.第一个方法(不推荐):编辑site.py，修改setencoding()函数，强制设置为utf-8
# 2.第一个方法(推荐):增加一个名为sitecustomize.py,推荐存放路径为site-packages目录下，
# sitecustomize.py在site.py被import执行的，因为sys.setdefaultencoding()是在site.py的最后删除的，可以在sitecustomize.py使用sys.setdefaultencoding()
# 既然sitecustomize.py层被自动加载，所以除了设置编码外，也可设置一些其他的东西，如字符串的编码 s1='中文',字符串将按照文件编码处理
# 如果unicode编码，有以下三种方式:
s = u'中文'
s1 = unicode('中文', 'gbk')   # unicode是内置函数，第二个参数指示源字符串的编码格式
s2 = s.decode('gbk')   # decode是任何str具有的方法，将str转换成unicode格式，参数指示源字符串的编码格式；
s3 = s2.encode('utf-8') # encode是任何str具有的方法，encode将str转换成参数指定的格式






if __name__ == "__main__":
    pass