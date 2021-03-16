#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:fengg
@file:helper.py
@time:2020/09/14
"""
import json

import os
import xlrd


class Helper(object):
    '''公共方法'''

    def base_dir(self, filePath, folder='data'):
        '''
        返回公共路径
        :param filePath: 文件名称
        :param folder: 文件夹
        :return:
        '''
        return os.path.join(os.path.dirname(os.path.dirname(__file__)), folder, filePath)

    def readExcel(self, rowx, filePath='data.xlsx'):
        '''
        读取excel中数据并且返回
        :param rowx: xlsx文件名称
        :param filePath: 文件名称
        :return:
        '''
        book=xlrd.open_workbook(self.base_dir(filePath))
        sheet=book.sheet_by_index(0)
        return sheet.row_values(rowx)

    def getUrl(self, rowx):
        '''
        获取请求地址
        :param rowx:在excel中的行数
        :return:
        '''
        return self.readExcel(rowx)[1]

    def getData(self, rowx):
        '''
        获取数据并且返回
        :param rowx: 在excel中的行数
        :return:
        '''
        return json.loads(self.readExcel(rowx)[2])

if __name__ == "__main__":
    pass