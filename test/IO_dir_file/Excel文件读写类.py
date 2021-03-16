#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:fengg
@file:Excel文件读写类.py
@time:2021/02/25
"""

'''
一、打开workbook
'''

import xlrd
wb = xlrd.open_workbook('myworkbook.xls')
# 检查表单名字
wb.sheet_names()
# 得到第一张表单，两种方式：索引和名字
sh = wb.sheet_by_index(0)
sh = wb.sheet_by_name(u'Sheet1')

# 递归打印出每行的信息
for rownum in range(sh.nrows):
    print sh.row_values(rownum)

# 如果只想返回第一列数据
first_column = sh.col_values(0)
# 通过索引读取数据,索引从零开始
cell_A1 = sh.cell(0, 0).value
cell_C4 = sh.cell(rowx=3, colx=2).value

'''
二、写excel，使用xlwt，可在Linux下保存Excel文件
'''
# 初始化workbook对象，添加一个workbook对象
import xlwt
wbk = xlwt.Workbook()
sheet = wbk.add_sheet('sheet 1')

# 创建表单后，写入数据
sheet.write(0, 1, 'test text')

# 保存文件(不需要close文件)
wbk.save('test.xls')

'''
三、深入探索
'''
# worksheet对象，当更改表单内容时，会有警告提示:
sheet.write(0, 0, 'test')
# 解决方式：使用cell_overwrite_ok = True来创建worksheet
sheet2 = wbk.add_sheet('sheet 2', cell_overwrite_ok=True)
sheet2.write(0, 0, 'some text')
sheet2.write(0, 0, 'this cell should overwrite')

# 定义格式:xlwt允许每个单元格或整行地设置格式，还允许添加链接及公式
# dates.py:展示如何设置不同的数据格式
# hyperlinks.py:展示如何创建超链接
# merged.py:展示如何合并单元格
# row_styles.py:展示如何应用Style到整行格子中
style = xlwt.XFStyle()

# 定义字体
font = xlwt.Font()
font.name = 'Times New Roman'
font.bold = True

# 设置类型的字体，应用到新创建的文件中
style.font = font

# 写入时使用这种类型
sheet.write(0, 0, 'some bold Times text', style)

'''
修改excel：
用xlrd读取excel是只读的，xlrd.open_workbook()方法返回xlrd.Book类型，不能对其进行操作
用xlwt.Workbook()返回的xlwt.Workbook类型的save（filepath)方法可以保存excel文件，即读取和生成Excel都非常容易处理
但已存在的Excel文件进行修改，需要xlutils(依赖于xlrd和xlwt)提供复制excel文件内容和修改文件的功能，
实际是在xlrd.Book和xlwt.Workbook之间建立了一个管道
'''
from xlrd import open_workbook
from xlutils.copy import copy

rb = open_workbook('1.xls')
# 通过sheet_by_index()获取的sheet没有write()方法
rs = rb.sheet_by_index(0)
wb = copy(rb)
# 通过get_sheet()获取的sheet有write()方法
ws = wb.get_sheet(0)
ws.write(0, 0, 'changed!')
wb.save('1.xls')

import xlrd
import xlwt
import xlutils.copy
import os.path


class XlsEngine():
    """
    for excel operation
    Usage:
    xlseng = XlsEngine('filePath')
    """

    def __init__(self, xlsname):
        """
        define class variable
        """
        self.xls_name = xlsname  # file name
        self.xlrd_object = None  # workbook object
        self.is_open_true = False  # file open flag

    def open(self):
        """
        open a xls file
        Usage: xlseng.open()
        """
        try:
            self.xlrd_object = xlrd.open_workbook(self.xls_name)
            self.is_open_true = True
            print('[%s, %s].' % (self.is_open_true, self.xlrd_object))
        except:
            self.is_open_true = False
            self.xlrd_object = None
            print('open %s faild.' % self.xls_name)

    def info(self):
        """
        show xls file information
        Usage: xlseng.info()
        """
        if self.is_open_true == True:
            for sheetname in self.xlrd_object.sheet_names():
                worksheet = self.xlrd_object.sheet_by_name(sheetname)
                print('%s:(%d row, %d col).' % (sheetname, worksheet.nrows, worksheet.ncols))
            else:
                print('file %s is not open.' % self.xls_name)

    def read_cell(self, sheetname='sheet1', rown=0, coln=0):
        """
        read file's a cell content
        Usage:xlseng.readcell('sheetname', rown, coln)
        """
        try:
            if self.is_open_true == True:
                worksheets = self.xlrd_object.sheet_names()
                if sheetname not in worksheets:
                    print('%s is not exit.' % sheetname)
                    return False
                worksheet = self.xlrd_object.sheet_by_name(sheetname)
                cell = worksheet.cell_value(rown, coln)
                print('[file:%s, sheet:%s, row:%s, col:%s]:%s.' % (self.xls_name, sheetname, rown, coln, cell))
            else:
                print('file %s is not open.' % self.xls_name)
        except:
            print('readcell is false! please check sheetn rown andcoln is right.')

    def read_row(self, sheetname='sheet1', rown=0):
        """
        read file's a row content
        Usage:
        xlseng.readrow('sheetname', rown)
        """
        try:
            if self.is_open_true == True:
                worksheets = self.xlrd_object.sheet_names()
                if sheetname not in worksheets:
                    print('%s is not exit.' % sheetname)
                    return False
                worksheet = self.xlrd_object.sheet_by_name(sheetname)
                row = worksheet.row_values(rown)
                print('[file:%s, sheet: %s, row: %s]: %s.' % (self.xls_name, sheetname, rown, row))
            else:
                print('file %s is not open.' % self.xls_name)
        except:
            print('readrow is false! please check sheetn rown is right.')

    def read_col(self, sheetname='sheet1', coln=0):
        """
        read file's a col content
        Usage:
        xlseng.readcol(sheetname',coln)
        """
        try:
            if self.is_open_true == True:
                worksheets = self.xlrd_object.sheet_by_names()
                if sheetname not in worksheets:
                    print('%s is not exit.' % sheetname)
                    return False
                worksheet = self.xlrd_object.sheet_by_name(sheetname)
                col = worksheet.col_values(coln)
                print('[file: %s, sheet: %s, col:%s]: %s.' % (self.xls_name, sheetname, coln, col))
            else:
                print('file %s is not open.' % self.xls_name)
        except:
            print('readcol is false! please check sheetn coln is right.')

    def write_cell(self, value='', sheetn=0, rown=0, coln=0):
        """
        write a cell to file, other cell is not change
        Usage:
        xlseng.writecell('str', sheetn, rown, coln)
        """
        if self.is_open_true == True:
            xlrd_objectc = xlutils.copy.copy(self.xlrd_object)
            worksheet = xlrd_objectc.get_sheet(sheetn)
            worksheet.write(rown, coln, value)
            xlrd_objectc.save(self.xls_name)
            print('writecell value:%s to [sheet:%s, row:%s, col:%s] is ture.' % (value, sheetn, rown, coln))
        else:
            print('file %s is not open.' % self.xls_name)

    def write_row(self, values='', sheetn=0, rown=0, coln=0):
        """
        write a row to file, other row and cell is not change
        Usage:
        xlseng.writerow('str1, str2, str3...strn', sheetn, rown.coln)
        """
        try:
            if self.is_open_true == True:
                xlrd_objectc = xlutils.copy.copy(self.xlrd_object)
                worksheet = xlrd_objectc.get_sheet(sheetn)
                values = values.split(',')
                for value in values:
                    worksheet.write(rown, coln, value)
                    coln += 1
                xlrd_objectc.save(self.xls_name)
                print('writerow values: %s to [sheet: %s, row:%s, col:%s] is ture.' % (values, sheetn, rown, coln))
            else:
                print('file %s is not open.' % self.xls_name)
        except:
            print('writerow is false! please check.')

    def write_col(self, values='', sheetn=0, rown=0, coln=0):
        """
        write a col to file, other col and cell is not change
        Usage:
        xlseng.writecol('str1, str2, str3...', sheetn, rown.coln)
        """
        try:
            if self.is_open_true == True:
                xlrd_objectc = xlutils.copy.copy(self.xlrd_object)
                worksheet = xlrd_objectc.get_sheet(sheetn)
                values = values.split(',')
                for value in values:
                    worksheet.write(rown, coln, value)
                    rown += 1
                xlrd_objectc.save(self.xls_name)
                print('writecol values:%s to [sheet:%s, row:%s, col:%s] is ture.' % (values, sheetn, rown, coln))
            else:
                print('file %s is not open.' % self.xls_name)
        except:
            print('writecol is false! please check.')

    def file_create(self, sheetnames='sheet1'):
        """
        create a empty xlsfile
        Usage:
        filecreate('sheetname1, sheetname2...')
        """
        try:
            if os.path.isfile(self.xls_name):
                print('%s is exit.' % self.xls_name)
                return False
            workbook = xlwt.Workbook()
            sheetnames = sheetnames.split(',')
            for sheetname in sheetnames:
                workbook.add_sheet(sheetname, cell_overwrite_ok=True)
            workbook.save(self.xls_name)
            print('%s is created' % self.xls_name)
        except:
            print('filerator is false! please check.')

    def addsheet(self, sheetnames='sheet1'):
        """
        add sheets to a exit xlsfile
        Usage:
        addsheet('sheetname1, sheetname2...
        """
        try:
            if self.is_open_true == True:
                worksheets = self.xlrd_object.sheet_names()
                xlrd_objectc = xlutils.copy.copy(self.xlrd_object)
                sheetnames = sheetnames.split(',')
                for sheetname in worksheets:
                    if sheetname in worksheets:
                        print("%s is exit." % sheetname)
                        return False
                for sheetname in sheetnames:
                    xlrd_objectc.add_sheet(sheetname, cell_overwrite_ok=True)
                xlrd_objectc.save(self.xls_name)
                print('addsheet is true.')
            else:
                print("file %s is not open \n" % self.xls_name)
        except:
            print('addsheet is false! please check.')

    # def chgsheet(self, sheetn, values):

    # def clear(self):


if __name__ == '__main__':
    # 初始化对象
    xlseng = XlsEngine("G:\\work_file\\AutoTest_From_Git\\test\IO_dir_file\\test2.xls")
    # 新建文件，可指定要新建的sheet页面名称，默认值新建sheet1
    xlseng.file_create('newSheet1, newSheet2, newSheet3')
    # 打开文件
    print("xlseng.open():")
    xlseng.open()
    # 添加sheet页
    print("\nxlseng.addsheet():")
    xlseng.addsheet("addSheet1, addSheet2, addSheet3")
    # 输出文件信息
    print("\nxlseng.info():")
    xlseng.info()
    # 读取sheet1页第3行第3列单元格数据(默认读取sheet1页，1行1列单元格数据)
    print("\nxlseng.readcell():")
    xlseng.read_cell('sheet1', 2, 2)
    # 读取sheet1页第2行的数据(默认读取sheet1页，1行1列单元格数据)
    print("\nxlseng.readrow():")
    xlseng.readrow('sheet1', 1)
    # 读取sheet1页第3列的数据(默认读取sheet1页第1列的数据)
    print("\nxlseng.readcol():")
    xlseng.read_col('sheet1', 2)
    # 向第一个sheet页的第2行第4列些字符串数据'I am writecell writed'
    print("\nxlseng.writecell():")
    xlseng.write_cell('I am writecell writed', 0, 1, 3)
    # 向第一个sheet页写一行数据，各列的值为'rowstr1, rowstr2, rowstr3', 从第3行第4列开始写入
    print("\nxlseng.writerow():")
    xlseng.write_row('ROWSTR1, ROWSTR2, ROWSTR3', 0, 2, 3)
    # 向第一个sheet页写一列数据，各行的值为'colstr1, colstr2, colstr3, colstr4', 从第4行第4列开始写入
    print("\nxlseng.writecol():")
    xlseng.write_row('ROWSTR1, ROWSTR2, ROWSTR3, ROWSTR4', 0, 3, 3)
