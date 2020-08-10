#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:fengg
@file:CreateContacts.py
@time:2020/08/10
"""
from . import *
from WriteTestResult import writeTestResult

def dataDriverFun(dataSourceSheetObj, stepSheetObj):
    try:
        # 获取数据源表中是否执行列对象
        dataIsExecuteColumn = excelObj.getColumn(dataSourceSheetObj, dataSource_isExecute)
        # 获取数据源表中"电子邮箱"列对象
        emailColumn = excelObj.getColumn(dataSourceSheetObj, dataSource_email)
        # 获取测试步骤表中存在数据区域的行数
        stepRowNums = excelObj.getRowsNumber(stepSheetObj)
        # 记录成功执行的数据条数
        successDatas = 0
        # 记录被设置为执行的数据条数
        requiredDatas = 0
        for idx, data in enumerate(dataIsExecuteColumn[1:]):
            # 遍历数据源表，准备进行数据驱动测试
            # 因为第一行是标题行,所以从第二行开始遍历
            if data.value == "y":
                print u"开始添加联系人 %s " % emailColumn[idx + 1].value
                requiredDatas += 1
                # 定义记录执行成功步骤数变量
                successStep = 0
                for index in xrange(2, stepRowNums +1):
                    # 获取数据驱动测试步骤表中
                    # 第index行对象
                    rowObj = excelObj.getRow(stepSheetObj, index)
                    # 获取关键字作为调用的函数名
                    keyWord = rowObj[testStep_keyWords - 1].value
                    # 获取操作元素定位方式作为调用的函数的参数
                    locatorExpression = rowObj[testStep_locatorExpression - 1].value
                    # 获取操作值作为调用函数的参数
                    operateValue = rowObj[testStep_operateValue -1].value
                    if isinstance(operateValue, long):
                        operateValue = str(operateValue)
                    if operateValue and operateValue.isalpha():
                        # 如果operateValue变量不为空，说明有操作值，从数据源表中根据坐标获取对应单元格的数据
                        coordinate = operateValue + str(idx +2)
    except Exception as e:
        raise e

if __name__ == "__main__":
    pass