# !/usr/bin/env python
# -- coding: utf-8 --
# title = '' 
# author = '20991' 
# mtime = '2020/8/2'
__author__ = 'YourName'

from util.ObjectMap import *
from util.KeyBoardUtil import KeyboardKeys
from util.ClipboardUtil import Clipboard
from util.WaitUtil import WaitUtil
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
# from action.PageAction import *
import time
# from util.ParseExcel import ParseExcel
# from config.VarConfig import *
# from util.Log import *
# import traceback
#
#
# # 创建解析Excel对象
# excelObj = ParseExcel()
# # 将Excel数据文件加载到内存
# excelObj.loadWorkBook(dataFilePath)
#
#
# # 用例或用例步骤执行结束后，向Excel中写执行结果信息
# def writeTestResult(sheetObj, rowNo, colsNo, testResult, errorInfo=None, picPath=None):
#     # 测试通过结果信息为绿色，失败为红色
#     colorDict = {"pass": "green", "faild": "red"}
#     # 因为"测试用例"工作表和"用例步骤sheet表"中都有测试执行时间和测试结果列，定义此字典对象是为了区分具体应该写哪个工作表
#     colsDict = {
#         "testCase": [testCase_runTime, testCase_testResult],
#         "caseStep": [testStep_runTime, testStep_testResult]
#     }
#     try:
#         # 在测试步骤sheet中，写入测试时间
#         excelObj.writeCellCurrentTime(sheetObj, rowNo=rowNo, colsNo=colsDict[colsNo][0])
#         # 在测试步骤sheet中，写入测试结果
#         excelObj.writeCell(sheetObj, content=testResult, rowNo=rowNo, colsNo=colsDict[colsNo][1], style=colorDict[testResult])
#         if errorInfo and picPath:
#             # 在测试步骤sheet中，写入异常信息
#             excelObj.writeCell(sheetObj, content=errorInfo, rowNo=rowNo, colsNo=testStep_errorInfo)
#         else:
#             excelObj.writeCell(sheetObj, content=picPath, rowNo=rowNo, colsNo=testStep_errorPic)
#     except Exception, e:
#         error("写excel出错, ", traceback.print_exc())

def TestSendMailWithAttachment():
    # 创建Chrome浏览器的实例
    driver = webdriver.Chrome(executable_path="c:\\chromedriver")
    # 最大化浏览器窗口
    driver.maximize_window()
    print u"访问163邮箱登录页..."
    driver.get("http://mail.163.com")
    # 暂停5s，以便邮箱登录页面加载完成
    time.sleep(5)
    assert u"163网易免费邮 -- 你的专业电子邮局" in driver.title
    print u"访问163邮箱登录页成功"
    # 创建显示等待
    wait = WaitUtil(driver)
    # 检查id为x - URS - iframe的frame是否存在，存在则切换进frame控件
    wait.frameToBeAvailableAndSwitchToIt("id", "x-URS-iframe")
    print u"输入登录用户名"
    userName = getElement(driver, "xpath", '//input[@name="email"]')
    userName.send_keys("xxx")
    print u"输入登录密码"
    pwd = getElement(driver, "xpath", '//input[@name = "password"]')
    pwd.send_keys("xxx")
    print u"用户登录..."
    pwd.send_keys(Keys.ENTER)
    # 等待5s,以便登录成功后的页面加载完成
    time.sleep(5)
    assert u"网易邮箱" in driver.title
    print u"登录成功"
    print u"添加联系人..."
    # 显示等待通讯录链接页面元素的出现
    addressBook = wait.visibilityOfElementLocated("xpath", "//div[text()='通讯录']")
    # 单击写信链接
    addressBook.click()
    # 显式等待新建联系人按钮的出现
    newContact = wait.visibilityOfElementLocated("xpath", "//span[text()='新建联系人']")
    # 写入收件人地址'//div[contains(@id, '_mail_emailinput)]/input'
    newContact.click()
    # 显式等待输入联系人姓名输入框出现
    contactName = wait.visibilityOfElementLocated("xpath", "//a[@title='编辑详细姓名']、preceding-sibling::div/input")
    contactName.send_keys("lily")
    email = getElement(driver, "xpath", "//*[@id='iaddress_MAIL_wrap']//input")
    email.send_keys("lily@qq.com")
    # 设定为星标联系人
    getElement(driver, "xpath", "//span[text()='设为星标联系人']/preceding - sibling::span/b").click()
    mobile = getElement(driver, "xpath", "//*[@id='iaddress_TEL_wrap']//dd/input")


    driver.find_element_by_xpath('//*[@id="_mail_emailcontainer_0_315"]').send_keys("xxx")
    # 写入邮件主题 "//dir[@aria - label = '邮件主题输入框，请输入邮件主题']/input"
    driver.find_element_by_xpath('//*[@id="1595685703525_subjectInput"]').send_keys(u"新邮件")
    # 切换进frame控件 "iframe[@tabindex = 1]"
    driver.switch_to.frame(driver.find_element_by_xpath('//*[@id="_mail_editor_0_321"]/div[1]/div[2]/iframe'))
    editBox = driver.find_element_by_xpath("/html/body")
    editBox.send_keys(u"发送给光荣之路的一封信")
    driver.switch_to.default_content()
    print u"写信完成"
    # 写信完成 "//header//span[text() = '发送']"
    driver.find_element_by_xpath('//*[@id="_mail_button_8_322"]/span[2]').click()
    print u"开始发送邮件..."
    time.sleep(3)
    assert u"发送成功" in driver.page_source
    print u"邮件发送成功"
    driver.quit()
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
            # 因为用例sheet中第一行为标题行，无需执行
            # print i.value
            # 循环遍历"测试用例"表中的测试用例，执行被设置为执行的用例
            if i.value.lower() == "y":
                requiredCase += 1
                # 获取"测试用例"表中第idx+2行数据
                caseRow = excelObj.getRow(caseSheet, idx + 2)
                # 获取第idx+2行的"步骤sheet"单元格内容
                caseStepSheetName = caseRow[testCase_testStepSheetName - 1].value
                # print caseStepSheetName
                # 根据用例步骤名获取步骤sheet对象
                stepSheet = excelObj.getSheetByName(caseStepSheetName)
                # 获取步骤sheet中步骤数
                stepNum = excelObj.getRowsNumber(stepSheet)
                # print stepNum
                # 记录测试用例i的步骤成功数
                successfulSteps = 0
                info(u"开始执行用例 %s " % caseRow[testCase_testCaseName - 1].value)
                for step in xrange(2, stepNum + 1):
                    # 因为步骤sheet中的第一行为标题行，无需执行
                    # 获取步骤sheet中第step行对象
                    stepRow = excelObj.getRow(stepSheet, step)
                    # 获取关键字作为调用的函数名
                    keyWord = stepRow[testStep_keyWords - 1].value
                    # 获取操作元素定位方式作为调用的函数的参数
                    locationType = stepRow[testStep_locationType - 1].value
                    # 获取操作元素的定位表达式作为调用函数的参数
                    locatorExpressino = stepRow[testStep_locatorExpression - 1].value
                    # 获取操作值作为调用函数的参数
                    operateValue = stepRow[testStep_operateValue -1 ].value

                    # 将操作值为数字类型的数据转成字符串类型，方便字符串拼接
                    if isinstance(operateValue, long):
                        operateValue = str(operateValue)
                    # print keyWord, locationType, locatorExpressino, operateValue
                    expressionStr = ""
                    # 构造需要执行的python语句，
                    # 对应的是PageAction.py中的页面动作函数调用的字符串表示
                    if keyWord and operateValue and locationType is None and locatorExpressino is None:
                        expressionStr = keyWord.strip() + "(u'" + operateValue + "')"
                    elif keyWord and operateValue is None and locationType is None and locatorExpressino is None:
                        expressionStr = keyWord.strip() + "()"
                    elif keyWord and locationType and operateValue and locatorExpressino is None:
                        expressionStr = keyWord.strip() + "('" + locationType.strip() +"',u'" + operateValue + "')"
                    elif keyWord and locationType and locatorExpressino and operateValue:
                        expressionStr = keyWord.strip() + "', '" + locatorExpressino.replace("'", '"').strip()\
                                        + "',u'" + operateValue + "')"
                    elif keyWord and locationType and locatorExpressino and operateValue is None:
                        expressionStr = keyWord.strip() + "('" + locationType.strip() + "', '"\
                                        + locatorExpressino.replace("'", '"').strip() + "')"
                    # print expressionStr
                    try:
                        # 通过eval函数，将拼接的页面动作和函数调用的字符串
                        # 当成有效的python表达式执行 从而执行测试步骤的sheet中，关键字在ageAction.py中对应的映射方法
                        # 从而完成对页面元素的操作
                        eval(expressionStr)
                        # 在测试执行时间列写入执行时间
                        excelObj.writeCellCurrentTime(stepSheet, rowNo=step, colsNo=testStep_runTime)
                    except Exception as e:
                        # 截取异常屏幕图片
                        capturePic = capture_screen()
                        # 获取详细的异常堆栈信息
                        errorInfo = traceback.format_exc()
                        # 在测试步骤Sheet中写入失败信息
                        writeTestResult(
                            stepSheet, step, "caseStep",
                            "faild", errorInfo, capturePic
                        )
                        error(u"步骤 %s 执行失败" % stepRow[testStep_testStepDescribe - 1].value)
                    else:
                        # 在测试步骤Sheet中写入成功信息
                        writeTestResult(stepSheet, step, "caseStep", "pass")
                        # 每成功一步，successfulSteps变量自增1
                        successfulSteps += 1
                        info(u"步骤 %s 执行通过!" % stepRow[testStep_testStepDescribe -1].value)

                if successfulSteps == stepNum -1:
                    # 当测试用例sheet中所有的步骤都执行成功，可认为此测试用例执行通过，然后将所有成功信息写入测试用例表中，
                    # 否则写入失败信息
                    writeTestResult(caseSheet, idx+2, "testCase", "pass")
                    successfulCase +=1
                else:
                    writeTestResult(caseSheet, idx+2, "testCase", "faild")
                    debug("共%d条用例，%d需要被执行，本次执行通过%d条"\
                          % (len(isExecuteColumn)-1, requiredCase, successfulCase))
    except Exception as e:
        # 打印详细的异常堆栈信息
        error(traceback.print_exc())


if __name__ == '__main__':
    TestSendMailWithAttachment()
