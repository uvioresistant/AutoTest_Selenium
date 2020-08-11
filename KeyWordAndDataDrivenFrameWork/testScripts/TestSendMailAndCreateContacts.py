#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:fengg
@file:TestSendMailAndCreateContacts.py
@time:2020/08/11
"""
from . import *
from . import CreateContacts
from WriteTestResult import writeTestResult


def TestSendMailAndCreateContacts():
    try:
        # 根据Excel文件中的sheet名获取sheet对象
        caseSheet = excelObj.getSheetByName(u"测试用例")
        # 获取测试用例sheet中是否执行列对象
        isExecuteColumn = excelObj.getColumn(caseSheet, testCase_isExecute)
        # 记录执行成功的测试用例个数
        successfulCase = 0
        # 记录需要执行的用例个数
        requiredCase = 0
        for idx, i in enumerate(isExecuteColumn[1:]):
            # 因为用例sheet中第一行为标题行，无须执行
            caseName = excelObj.getCellOfValue(caseSheet, rowNo=idx+2, colsNo=testCase_testCaseName)
            # 循环遍历"测试用例"表中的测试用例，执行被设置为执行的用例
            if i.value.lower() == 'y':
                requiredCase += 1
                # 获取测试用例表中，第idx+1行中用例执行时所使用的框架类型
                useFrameWorkName = excelObj.getCellOfValue(caseSheet, rowNo=idx+2, colsNo=testCase_frameWorkName)
                # 获取测试用例表中，第idx+1行中执行用例的步骤sheet名
                stepSheetName = excelObj.getCellOfValue(caseSheet, rowNo=idx+2, colsNo=testCase_testStepSheetName)
                print "----", stepSheetName
                if useFrameWorkName == u"数据":
                    print u"*****调用数据驱动******"
                    # 获取测试用例表中，第idx+1行，执行框架为数据驱动的用例所使用的数据sheet名
                    dataSheetName = excelObj.getCellOfValue(caseSheet, rowNo=idx+2, colsNo=testCase_dataSourceSheetName)
                    # 获取第idx+1行测试用例的步骤sheet对象
                    stepSheetObj = excelObj.getSheetByName((stepSheetName))
                    # 获取第idx+1行测试用例使用的数据sheet对象
                    dataSheetObj = excelObj.getSheetByName(dataSheetName)
                    # 通过数据驱动框架执行添加联系人
                    result = CreateContacts.dataDriverFun(dataSheetObj, stepSheetObj)
                    if result:
                        print u"用例%s 执行成功" % caseName
                        successfulCase += 1
                        writeTestResult(caseSheet, rowNo=idx+2, colsNo="testCase", testResult="pass")
                    else:
                        print u"用例%s 执行失败" % caseName
                        writeTestResult(caseSheet, rowNo=idx+2, colsNo="testCase", testResult="faild")
                elif useFrameWorkName == u"关键字":
                    print u"*****调用关键字驱动******"
                    caseStepObj = excelObj.getSheetByName(stepSheetName)
                    stepNums = excelObj.getRowsNumber(caseStepObj)
                    successfulSteps = 0
                    print u"测试用例共%s步" % stepNums
                    for index in xrange(2, stepNums + 1):
                        # 因为用例sheet中第一行为标题行，无须执行
                        stepRow = excelObj.getRow(caseStepObj, index)
                        # 获取关键字作为调用的函数名
                        keyWord = stepRow[testStep_keyWords - 1].value
                        # 获取操作元素定位方式作为调用的函数的参数
                        locationType = stepRow[testStep_locationType - 1].value
                        # 获取操作元素的定位表达式作为调用函数的参数
                        locatorExpression = stepRow[testStep_locatorExpression - 1].value
                        # 获取操作值作为调用函数的参数
                        operateValue = stepRow[testStep_operateValue - 1].value
                        if isinstance(operateValue, long):
                            # 如果operateValue值为数字型，将其转换为字符串，方便字符串拼接
                            operateValue = str(operateValue)
                        # 构造需要执行的python表达式，此表达式对应的是PageAction.py的页面动作函数调用的字符串表示
                        tmpStr = "'%s', '%s'" % (locationType.lower(),
                                                 locatorExpression.replace("'", '"')
                                                 ) if locationType and locatorExpression else ""
                        if tmpStr:
                            tmpStr += ", u" + operateValue + "'" if operateValue else ""
                        else:
                            tmpStr += "u'" + operateValue + "'" if operateValue else ""
                        runStr = keyWord + "(" + tmpStr + ")"
                        try:
                            # 通过eval函数，将拼接的页面动作函数，使用调用的字符串表示，当成有效的Python表达式执行，
                            # 从而执行测试步骤的sheet中关键字在ageAction.py中对应的映射方法，来完成对页面元素的操作
                                eval(runStr)
                        except Exception as e:
                            print u"执行步骤 %s 发生异常" % stepRow[testStep_testStepDescribe - 1].value
                            # 截图异常屏幕图片
                            capturePic = capture_screen()
                            # 获取详细的异常堆栈信息
                            errorInfo = traceback.format_exc()
                            writeTestResult(caseStepObj, rowNo=index, colsNo="caseStep", testResult="faild",
                                            errorInfo=str(errorInfo), picPath=capturePic)
                        else:
                            successfulSteps += 1
                            print u"执行步骤 %s 成功" % stepRow[testStep_testStepDescribe - 1].value
                            writeTestResult(caseStepObj, rowNo=index, colsNo="caseStep", testResult="pass")

                    if successfulSteps == stepNums - 1:
                        successfulCase += 1
                        print u"用例%s执行通过" % caseName
                        writeTestResult(caseSheet, rowNo=idx + 2, colsNo="testCase", testResult="pass")
                    else:
                        print u"用例%s执行失败" % caseName
                        writeTestResult(caseSheet, rowNo=idx + 2, colsNo="testCase", testResult="faild")
                        # 清空不需要执行用例的执行时间和执行结果，异常信息，异常图片单元格
                        writeTestResult(caseSheet, rowNo=idx+2, colsNo="testCase", testResult="faild")
        print u"共%d条用例, %d条需要被执行，成功执行%d条" % (len(isExecuteColumn) - 1, requiredCase, successfulCase)
    except Exception as e:
            print traceback.print_exc()


if __name__ == "__main__":
    pass