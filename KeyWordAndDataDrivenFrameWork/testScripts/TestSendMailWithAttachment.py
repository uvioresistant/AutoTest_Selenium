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
    # 输入联系人手机号
    mobile.send_keys("183xxxxxxxx")
    # 输入备注信息
    getElement(driver, "xpath", "//textarea").send_keys(u"朋友")
    # 单击"确定"按钮，保存新建联系人
    getElement(driver, "xpath", "//span[text()='确定']").click()
    time.sleep(1)
    assert u"lily@qq.com" in driver.page_source
    print u"添加联系人成功"
    time.sleep(2)
    print u"写信..."
    receiver = getElement(driver, "xpath", "//div[contains(@id, '_mail_emailinput')]/input")
    # 输入收信人地址
    receiver.send_keys("xxx")
    subject = getElement(driver, "xpath", "//div[@aria-label='邮件主题输入框，请输入邮件主题']/input")
    # 输入邮件主题
    subject.send_keys(u"新邮件")
    # 设置剪贴板内容
    Clipboard.setText(u"d:\\a.txt")
    # 获取剪贴板内容
    Clipboard.getText()
    attachment = getElement(driver, "xpath", "//div[contains(@title, '600首MP3')]")
    # 点击上传附件链接
    attachment.click()
    time.sleep(3)
    # 在上传附件Windos弹窗中粘贴剪贴板中的内容
    KeyboardKeys.twoKeys("ctrl", "v")
    # 模拟回车键，以便加载要上传的附件
    KeyboardKeys.oneKey("enter")
    # 切换进邮件正文的frame
    wait.frameToBeAvailableAndSwitchToIt("xpath", "//iframe[@tabindex=1]")
    body = getElement(driver, "xpath", "/html/body")
    # 输入邮件正文
    body.send_keys(u"发送给光荣之路的一封信")
    # 切出邮件正文的frame框
    driver.switch_to.default_content()
    print u"写信完成"
    # 写信完成 "//header//span[text() = '发送']"

    getElement(driver, "xpath", "//header//span[text()='发送']").click()
    print u"开始发送邮件..."
    time.sleep(3)
    assert u"发送成功" in driver.page_source
    print u"邮件发送成功"
    driver.quit()


if __name__ == '__main__':
    TestSendMailWithAttachment()
