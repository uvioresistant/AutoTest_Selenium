#!usr/bin/env python
#-*- coding:utf-8 -*-
"""
@author:fengg
@file: VarConfig.py
@time: 2020/07/11
"""
import os


ieDriverFilePath = "c:\\IEDriverServer"
chromeDriverFilePath = "c:\\ChromeDriverServer"
firefoxDriverFilePath = "c:\\FirefoxDriverServer"


# 获取当前文件所在目录的父目录的绝对路径
parentDirPath = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 异常截图存放目录绝对路径
screenPicturesDir = parentDirPath + "\\exceptionPictures\\"
print screenPicturesDir

# 获取数据文件存放绝对路径
dataFilePath = parentDirPath + u"\\testData\\163邮箱发送邮件.xlsx"

# 测试数据文件中，测试用例表中部分列对应的数字序号
testCase_testCaseName = 2
testCase_frameWorkName = 4
testCase_testStepSheetName = 5
testCase_dataSourceSheetName = 6
testCase_isExecute = 7
testCase_runTime = 8
testCase_testResult = 9

# 用例步骤表中，部分列对应的数字序号
testStep_testStepDescribe = 2
testStep_keyWords = 3
testStep_locationType = 4
testStep_locatorExpression = 5
testStep_operateValue = 6
testStep_runTime = 7
testStep_testResult = 8
testStep_errorInfo = 9
testStep_errorPic = 10

# 数据源表中，是否执行列对应的数字编号
dataSource_isExecute = 7
dataSource_email = 3
dataSource_runTime = 8
dataSource_result = 9