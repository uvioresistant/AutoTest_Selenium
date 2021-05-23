#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:fengg
@file:ftp上传文件.py
@time:2021/03/09
"""
from ftplib import FTP
import os


def ftp_up(filename="20210309.rar"):
    IP = "103.240.150.104"
    user = "user"
    password = '5'
    filename = "zhihu.html"
    path = "G:\\work_file\\AutoTest_From_Git\\test\\upload\\test"
    ftp = FTP()  # 设置变量
    ftp.set_debuglevel(2)  # 打开调试级别2，显示详细信息
    ftp.connect(IP)  # 连接的用户名，密码
    ftp.login('admin', 'admin')  # 登录，匿名登录则用空串代替即可
    ftp.cwd("xxx/xxx/")  # 选择操作目录
    bufsize = 1024  # 设置缓冲块大小
    file_handler = open(filename, 'rb')  # 以读模式在本地打开文件
    print ftp.getwelcome()
    ftp.storbinary("STOR %s" % os.path.basename(filename))
    # 上传文件
    ftp.set_debuglevel(0)
    file_handler.close()
    ftp.quit()
    print "ftp up OK"


def ftp_down(filename="20210309.zip"):
    ftp = FTP()
    ftp.set_debuglevel(2)
    ftp.connect('192.168.0.1', '21')
    ftp.login('admin', 'admin')
    print ftp.getwelcome()  # 显示ftp服务器欢迎信息
    ftp.cwd("xxx/xxx/")  # 选择操作目录
    bufsize = 2048
    filename = "20210309.zip"
    file_handler = open(filename, 'wb').write
    ftp.retrbinary("RETR %s" % os.path.basename(filename))
    ftp.set_debuglevel(0)
    file_handler.close()
    ftp.quit()
    print "ftp down OK"


'''搭建ftp服务器server端'''
from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer

authorizer = DummyAuthorizer()  # 实例化DummyAuthorizer来创建ftp用户
authorizer.add_user('admin', '123456', r"G:\\work_file\\AutoTest_From_Git\\test\\upload\\test", perm='elradfmwMT')
# authorizer.add_anonymous('/home/nobody')  # 匿名登录
handler = FTPHandler
handler.authorizer = authorizer
server = FTPServer(('0.0.0.0', 2121), handler)  # 设置本地地址
server.serve_forever()

'''ftplib模块可实现简单ftp客户端'''
from ftplib import FTP

ftp = FTP()
ftp.set_debuglevel(2)
ftp.connect("IP", "port")
ftp.login("user", "password")
print ftp.getwelcome()
ftp.cmd("xxx/xxx")  # 进入远程目录
bifsize = 1024  # 设置的缓冲区大小
filename = "filename.txt"  # 需要下载的文件
file_handle = open(filename, "wb").write  # 写模式在本地打开文件
ftp.retrbinary("RETR filename.txt", file_handle, bufsize)  # 接收服务器上文件并写入本地文件
ftp.set_debuglevel(0)  # 关闭调试模式
ftp.quit()  # 退出ftp

from ftplib import FTP
import time
import tarfile
import os
from ftplib import FTP


def ftpconnect(host, username, password):
    ftp = FTP()
    ftp.connect(host, 21)
    ftp.login(username, password)  # 登录FTP服务器，所有参数都可选
    return ftp


# 从ftp下载文件
def downloadfile(ftp, remotepath, localpath):
    bufsize = 1024
    fp = open(localpath, 'wb')
    ftp.retrbinary('RETR' + remotepath, fp.write, bufsize)
    ftp.set_debuglevel(0)
    fp.close()


# 从本地上传文件到ftp
def uploadfile(ftp, remotepath, localpath):
    bufsize = 1024
    fp = open(localpath, 'rb')
    ftp.storbinary('STOR' + remotepath, fp, bufsize)
    ftp.set_debuglevel(0)
    fp.close()


if __name__ == "__main__":
    ftp = ftpconnect("113.105.139.xxx", "ftp***", "Guest***")
    downloadfile(ftp, "Faint.mp4", "G:\\work_file\\AutoTest_From_Git\\test\\upload\\test.mp4")
    # 调用本地播放器播放下载的视频
    os.system(
        'start "G:\\work_file\\AutoTest_From_Git\\test\\upload\\wmplayer.exe" "G:\\work_file\\AutoTest_From_Git\\test\\upload\\test.mp4"')
    uploadfile(ftp, "G:\\work_file\\AutoTest_From_Git\\test\\upload\\test.mp4", "test.mp4")



'''
ftp 按目录结构上传下载
'''
from ftplib import FTP
import time
import os


def __ftp_upload(ftp, local, remote, isDel=False):
    if os.path.isdir(local):
        for f in os.listdir(local):
            if os.path.isdir(local + f):
                try:
                    ftp.cwd(remote + f)
                except:
                    ftp.mkd(remote + f)
                print(local + f)
                __ftp_upload(ftp, local + f + '/', remote + f + '/', isDel)
            else:
                print(remote + f)
                print(local + f)
                fp = open(local + f, 'rb')
                ftp.storbinary('STOR' + remote + f, fp, 4096)
                fp.close()
                if (isDel == True):
                    os.remove(local)
        else:
            fp = open(local + f, 'rb')
            fp.storbinary('STOR' + remote + f, fp, 4096)
            fp.close()
            if (isDel == True):
                os.remove(local)


def ftp_upload(host, port, username, password, local, remote, isDel=False):
    ftp = FTP()
    try:
        ftp.connect(host, port)
        ftp.login(username, password)
    except:
        return False
    try:
        __ftp_upload(ftp, local, remote, False)
    except Exception, e:
        print e
    ftp.close()
    return True


def ftp_download(host, port, username, password, local, remote):
    ftp = FTP()
    ftp.connect(host, port)
    ftp.login(username, password)
    ret = False
    try:
        if os.path.isdir(local):
            for f in ftp.dir(remote):
                fp = open(local + f, 'wb')
                ftp.retrbinary('RETR' + remote + f, fp.write, 4096)
                fp.close()
        else:
            fp = open(local, 'wb')
            ftp.retrbinary('RETR' + remote, fp.write, 4096)
            fp.close()
    except Exception, e:
        print "download exception: \n ", e
        ftp.close()
        return ret


if __name__ == '__main__':
    host = '*.*.*.*'
    port = '21'
    username = 'xxx'
    password = 'xxx'
    ftp_upload(host, port, username, password, '/home/', '/home/ubuntu/test.txt', False)
    print 'download'
    ftp_download(host, port, username, password, '/home/', '/home/ubuntu/test.txt')





















