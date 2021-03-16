#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:fengg
@file:py生成随机数据插入mysql.py
@time:2021/03/02
"""
import random as r
import pymysql

first = ('张', '王')
middle = ('芳', '军', '建')
last = ('明', '丽')
name = []
passwd1 = ('1234', '5678', '147', '258')
for i in range(101):
    name1 = r.choice(first) + r.choice(middle) + r.choice(last)  # 末尾有空格的名字
    name2 = name1.rstrip()  # 去掉末尾空格后的名字
    if name2 not in name:  # 名字存入列表中，且没有重名
        name.append(name2)
conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='123', db='test1')
cur = conn.cursor()
for i in range(len(name)): # 插入数据
    passwd = r.choice(passwd1) # 在密码列表中随机取一个
    cur.execute("insert into a2(name, passwd) value (%s, %s)", (name[i], passwd))
cur.execute("select * from a2")
for s in cur.fetchall():
    print(s)
conn.commit()
cur.close()
conn.close()