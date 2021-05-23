#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:fengg
@file:使用mysql批量插入.py
@time:2021/03/02
"""
import os
import mysql.connector

config = {
    'user': 'root',
    'password': '****',
    'host': '127.0.0.1',
    'database': 'test',
    'raise_on_warnings': True,
}
cnx = mysql.connector.connect(**config)


class ReadFile:
    def readLines(self):
        f = open("E:/data/2020-3-2.txt", "r", 1, "utf-8")
        i = 0
        list = []
        for line in f:
            strs = line.split("\t")
            if len(strs) != 5:
                continue
            data = (strs[0], strs[1], strs[2], strs[3], strs[4].read())
            list.append(data)
            cursor = cnx.cursor()
            sql = "insert into data_test(uid, log_date, fr, is_log)"
            if i > 5000:
                cursor.executemany(sql, list)
                cnx.commit()
                print("插入")
                i = 0
                list.clear()
            i = i + 1
        if i > 0:
            cursor.executemany(sql, list)
            cnx.commit()
        cnx.close()
        f.close()
        print("ok")

    def listFiles(self):
        d = os.listdir("E:/data/")
        return d


if __name__ == "__main__":
    readFile = ReadFile()
    readFile.readLines()
