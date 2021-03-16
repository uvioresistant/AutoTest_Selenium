#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:fengg
@file:文件读写_对文件和存储器的读写.py
@time:2021/02/24
"""
# # 1.文件的写入和读取
# s = '''文件创建和读取'''
#
# # 创建一个文件，且写入字符
# f = file('test_file.txt', 'w')
# f.write(s)
# f.close()
#
# # 读取文件，逐行打印
# f = file('test_file.txt')
# while True:
#     line = f.readline()
#     # 如果line长度为0，说明文件已经读完了
#     if len(line) == 0:
#         break
#     # 默认换行符也读出来了，所以用逗号取代print函数的换行符
#     print line,
# f.close()

# 2.存储器的写入和读取
# using_pickle.py
# import pickle as p
# cPickle 比pickle快很多
import cPickle as p

list_pickle = [1,2,2,3]
pickle_file = 'pickle_file.data'

f = file(pickle_file, 'w')
# 写入数据
p.dump(list_pickle, f)  # dump和load将数据序列化后保存至文件中，再从文件中取出并反序列化备用
# pickle_file_1 = p.dumps(list_pickle)
f.close()

del list_pickle

f = file(pickle_file)
# 读取数据
stored_list = p.load(f)
# stored_list = p.loads(pickle_file_1) # dumps和loads将数据序列化后，以字符串的个数保存在内存中
print stored_list
f.close()

if __name__ == "__main__":
    pass
