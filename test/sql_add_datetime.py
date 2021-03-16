#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:fengg
@file:sql_add_datetime.py
@time:2021/02/23
"""
import sys
import time
import re
from datetime import timedelta, datetime


def get_date(date, time_interval):
    """
    :param date:  字符类型时间 年月日 "20200101"
    :param time_interval: 间隔的时间 整型 前1天 为负数 -1 后1天 为正数 1
    :return: fmt_date: 格式化字符串类型时间 年月日 "2020-01-01"
    """
    start_date = datetime.strptime(date, '%Y%m%d')
    now_date = timedelta(days=time_interval)
    stop_date = start_date + now_date
    fmt_date = stop_date.strptime("%Y-%m-%d")
    return fmt_date


sqlFile = open("G:\\work_file\\AutoTest_From_Git\\fenqu.sql") # 输入文件
outPutfile = open("G:\\work_file\\AutoTest_From_Git\\fenqu_add_180.sql", "w")
sqlLine = sqlFile.readlines()
partition_map = {}  # 首字段为"partition"的
# 按行读写


af = datetime.now()
after_month = af.strftime("%Y-%m-%d")
after_month_table = af.strftime("%Y%m%d")
# 日期递增1，遍历整个文件中需要递增的内容
for sqlLine_single in sqlLine:
    pattern = re.compile(r'^partition')
    if pattern.match(sqlLine_single):
        sqlSplit = sqlLine_single.split(" ")
        sqlLine_single_table = sqlLine_single.replace(sqlSplit[1][3:11], after_month_table)
        sqlLine_single = sqlLine_single_table.replace(sqlSplit[4][14:24], after_month)
        af = af + timedelta(days=1)
        after_month = af.strftime("%Y-%m-%d")
        after_month_table = af.strftime("%Y%m%d")
        outPutfile.write(sqlLine_single)
    else:
        outPutfile.write(sqlLine_single)
sqlFile.close()
outPutfile.close()

# 按行读写
# while line:
#     lineSplit = line.split(" ") # 拆分字段
#     print line
#     line = file.readline()
#     # 日期修改为后180天
#     dt = lineSplit[1]
#     myday = datetime(int(dt[0:4]), int(dt[4:6]), int(dt[6:8])) + timedelta(days=180)
#     dt = myday.strftime("%Y-%m-%d")
#     lineSplit[1] = str(dt)
#
#     # 以日期为键，其余为值
#     if lineSplit[0] == "app":
#         app_map[lineSplit[1]] = lineSplit[0] + " " + lineSplit[2] + " " + lineSplit[3]
#         print "@@@@@@@@@@@"+app_map[lineSplit[1]]
#     elif lineSplit[0] == "input":
#         input_map[lineSplit[1]] = lineSplit[0] + " " + lineSplit[2] + " " + lineSplit[3]
# file.close()
#
# merge_map = {} # 字段联结
# for input_key, input_value in input_map.items():
#     if input_key in app_map.keys():
#         merge_map[input_key] = input_value[0:-1] + " " + app_map[input_key]
#     else:
#         print input_key + "************"
#     merge_map[input_key] = input_value[0:-1] + " " + "app"+ " " + "0" + " " + "0" + " " + "0" + "\n"
#
# # 按格式输出
# for merge_key, merge_value in merge_map.items():
#     merge = merge_key + " " + merge_value
#     outputfile.write(merge)
#     print merge_key + " " + merge_value
#
# outputfile.close()

# if __name__ == "__main__":
#     pass