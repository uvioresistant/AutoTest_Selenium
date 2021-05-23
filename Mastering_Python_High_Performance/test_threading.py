#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:fengg
@file:test_threading.py
@time:2020/11/11
"""
import thread
import time

# 打印时间5次，每次延迟"delay"秒
def print_time(threadName, delay):
    count = 0
    while count < 5:
        time.sleep(delay)
        count +=1
        print "%s: %s" % (threadName, time.ctime(time.time()))


# 创建两个线程
try:
    thread.start_new_thread(print_time, ("Thread-1", 2, ))
    thread.start_new_thread(print_time, ("Thread-2", 4, ))
except:
    print "Error: unable to start thread"

# 让程序持续运行，否则线程会小时
while 1:
    pass


# if __name__ == "__main__":
#     pass