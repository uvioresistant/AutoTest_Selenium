#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:fengg
@file:删除window垃圾文件.py
@time:2021/03/03
"""
import os


# 递归删除文件，里面和下面的函数用try是抛出删除正在使用的零时文件出错
def delfile(path):
    for file in os.listdir(path):
        if os.path.isfile(os.path.join(path, file)):
            try:
                print("\n删除垃圾文件: %s" % (os.path.join(path, file)))
                os.remove(os.path.join(path, file))
            except Exception as e:
                raise e
        elif os.path.isdir(os.path.join(path, file)):
            delfile(os.path.join(path, file))
        else:
            pass


def deldir(pa):
    for i in os.listdir(pa):
        if os.path.isdir(os.path.join(pa, i)):
            if len(os.listdir(os.path.join(pa, i))) > 0:
                deldir(os.path.join(pa, i))
                try:
                    os.rmdir(os.path.join(pa, i))
                except:
                    pass
            else:
                try:
                    print("\n删除文件夹: %s" % (os.path.join(pa, i)))
                    os.rmdir(os.path.join(pa, i))
                except:
                    pass


if __name__ == "__main__":
    workpath = 'G:\\work_file\\AutoTest_From_Git\\test\\traversal_file_dir\\del\\'
    # if os.name == 'nt':
    #     if 'HOMEPATH' in os.environ:
    #         home = os.environ['HOMEDRIVE'] + os.environ['HOMEPATH']
    #     else:
    #         home = os.environ['HOMEPATH']
    #     workpath = os.path.join(home, 'Local Settings')
    delfile(os.path.join(workpath, 'Temp'))
    delfile(os.path.join(workpath, 'Temporary Internet Files'))
    deldir(os.path.join(workpath, 'Temp'))
    deldir(os.path.join(workpath, 'Temporary Internet Files'))
    print("系统产生的临时垃圾文件清理完毕")
