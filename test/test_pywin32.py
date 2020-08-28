#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:fengg
@file:test_pywin32.py
@time:2020/08/17
"""
import win32api, win32con, win32file
import os


def SimpleFileDemo(filepath, filename):
    testName = os.path.join(win32api.GetTempFileName(filepath, filename), "win32file_demo_test_file")
    if os.path.exists(testName): os.unlink(testName)
    handle = win32file.CreateFile(testName,
                                  win32file.GENERIC_WRITE,
                                  0,
                                  None,
                                  win32con.CREATE_NEW,
                                  0,
                                  None)
    test_data = "hello\0there".encode("ascii")
    win32file.WriteFile(handle, test_data)
    handle.close()
    handle = win32file.CreateFile(testName, win32file.GENERIC_READ, 0, None, win32con.OPEN_EXISTING, 0, None)
    rc, data = win32file.ReadFile(handle, 1024)
    handle.close()
    if data == test_data:
        print "Successful wrote and read a file"
    else:
        raise Exception("Got different data back???")
    os.unlink(testName)


if __name__ == "__main__":
    SimpleFileDemo("G:\work_file\AutoTest_From_Git", "test")