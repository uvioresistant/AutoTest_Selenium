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
from action.PageAction import *
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
    print u"启动Chrome浏览器"
    open_browser("chrome")
    maximize_browser()
    print u"访问163邮箱登录页..."
    visit_url("http://mail.163.com")
    sleep(5)
    assert_string_in_pagesource(u"163网易免费邮 -- 你的专业电子邮局")
    print u"输入登录用户名"
    input_string("xpath", '//input[@name="email"]', "xxx")
    print u"输入登录密码"
    input_string("xpath", '//input[@name = "password"]', "xxx")
    # 单击登录按钮
    click("id", "dologin")
    sleep(5)
    assert_title(u"网易邮箱")
    print u"登录成功"
    print u"添加联系人"
    # 显示等待通讯录链接页面元素的出现
    waitVisibilityOfElementLocated("xpath", "//div[text()='通讯录']")
    # 单击通讯录链接
    click("xpath", "//div[text()='通讯录']")
    # 单击新建联系人按钮
    click("xpath", "//div[text()='新建联系人']")
    # 输入联系人姓名
    input_string("xpath", "//a[@title='编辑详细姓名']/preceding-sibling::div/input", "lily")
    # 输入联系人邮箱
    input_string("xpath", "//*[@id='iaddress_MAIL_wrap']//input", "lily@qq.com")
    # 单击星标联系人复选框
    click("xpath", "//span[text()='设为星标联系人']/preceding-sibling::span/b")
    # 输入联系人手机号
    input_string("xpath", "//*[@id='iaddress_TEL_wrap']//dd//input", "183xxxxxxxx")
    # 输入备注信息
    input_string("xpath", "//textarea", u"朋友")
    # 单击"确定"按钮，保存新建联系人
    click("xpath", "//span[text()='确定']")
    time.sleep(1)
    assert_string_in_pagesource("lily@qq.com")
    print u"添加联系人成功"
    time.sleep(2)
    # 单击首页链接按钮，进入写信页面
    click("xpath", "//div[.='首页']")
    # 显式等待写信链接出现在页面上
    waitVisibilityOfElementLocated("xpath", "//span[text()='写信'")
    # 单击写信链接按钮，写入写信页面
    click("xpath", "//span[text()='写信'")
    print u"开始写信..."
    print u"输入收信人地址"
    input_string("xpath", "//div[contains(@id, '_mail_emailinput')]/input", "xxx")
    print u"输入邮件主题"
    input_string("xpath", "//div[@aria-label='邮件主题输入框，请输入邮件主题']/input", u"新邮件")
    print u"单击上传附件按钮"
    click("xpath", "//div[@title, '600首MP3']")
    # 等待2s，以便上传附件的窗体加载完成
    sleep(2)
    print u"上传附件"
    paste_string(u"d:\\a.txt")
    # 按Enter键，上传附件
    press_enter_key()
    waitVisibilityOfElementLocated("xpath", '//span[.="上传完成"]')
    print u"上传附件成功"
    # 切换进邮件正文的frame框体中
    waitFrameToBeAvailableAndSwitchToIt("xpath", "//iframe[@tabindex=1]")
    print u"输入邮件正文"
    input_string("xpath", "/html/body", "u发送给光荣之路的一封信")
    # 切出邮件正文的frame框,进入默认会话框体
    switch_to_default_content()
    print u"写信完成"
    print u"开始发送邮件..."
    click("xpath", "//header//span[text()='发送']")
    time.sleep(3)
    assert_string_in_pagesource(u"发送成功")
    print u"邮件发送成功"
    close_browser()


if __name__ == '__main__':
    TestSendMailWithAttachment()
