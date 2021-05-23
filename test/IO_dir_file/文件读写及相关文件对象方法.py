#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:fengg
@file:文件读写及相关文件对象方法.py
@time:2021/02/24
"""

# py文件读写的内建函数是open或file, file_hander(文件句柄/对象)=open(filename, mode)
# * mode:
#     r 只读, 文件不存在报错
#     r+ 读写，文件不存在报错，不删除源文件，从头写入
#     w 只写，先删除源文件，再重新写入，如果文件没有则创建
#     w+ 读写，先删除源文件，再重新写入，如果文件没有则创建
#     a 只写，追加写，如果文件没有则创建
#     a+ 读写，追加写，如果文件没有则创建

# # 读文件
# fo = open("test_file.txt")
# fo.read()
# fo.close()
#
# # 写文件
# fnew = open("new.txt", 'w') # 没有则创建
# fnew.write('hello \n i am dave!!!!!!!!!') # 此时数据还只是在缓存区中，没有真正落到文件上
# fnew.close() # 关闭文件，数据会从缓冲区写到文件中
# # 使用r+参数:
# fnew = open("new.txt", 'r+')
# # >>> fnew_1.read()
# fnew.write("000") # 发现000替换开头字母，因为上面读取操作使用了指针，再写就写在后面，而这次是从头写入
# fnew.close()
#
# for i in open("new.txt"):   # 用open可以返回迭代类型的变量，可以逐行读取数据
#     print i
#
# # FileObject.readline([size]):每次读取文件的一行，size指每行每次读取size个字节，直到行的末尾，超出范围会读取空字符串
# f1 = open("new.txt")
# print f1.readline()
# f1.close()
#
# # FileObject.readlines:返回一个列表
# f1 = open("new.txt")
# print f1.readlines()
# f1.close()
#
# # FileObject.next:返回当前行，并将文件指针到下一行，超出范围会给予警示，停止迭代
f1 = open("new.txt")
print f1.next(), 111111111
# print f1.next(), 2222222222
f1.close()

# FileObject.write:write和后面writelines在写入前是否清除原来的数据，取决于打开文件的模式
# FileObject,writelines(List):多行写，效率比write高，速度更快，少量写入可以使用write
# L = ["python\n", "python\n", "python\n"]
# f1 = open("new.txt", 'a')
# f1.writelines(L)
# f1.close()

# FileObject.seek(偏移量,选项):可以在文件中移动文件指针到不同位置，默认值为0，表示从文件开头算起(绝对偏移量)，1代表从当前位置算起，2代表从文件末尾算起
# f1 = open("new.txt", 'r+')
# print f1.read(), 123
# f1.seek(0,0) # 指针指到开头，再读
# print f1.read(), 234
# f1.seek(-5, 2) # 指针指到末尾，再读
# print f1.read(), 345


# FileObject.flush() 刷新缓冲区，将缓冲区的数据立刻写入文件，同时清空缓冲区，不需被动等待输出缓冲区写入---文件关闭后会自动刷新缓冲区，有时需要在关闭前刷新，使用flush()
# f1 = open("new.txt", "a+")
#
# f1.write("测试两下")
# f1.flush()
# f1.seek(0,0)
# print f1.read(), 1111111111111111
# f1.close()




if __name__ == "__main__":
    pass