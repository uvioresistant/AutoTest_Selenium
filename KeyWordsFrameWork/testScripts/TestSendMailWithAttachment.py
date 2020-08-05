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


def TestSendMailWithAttachment():
    # # 创建Chrome浏览器的实例
    # driver = webdriver.Chrome(executable_path="c:\\chromedriver")
    # # 最大化浏览器窗口
    # driver.maximize_window()
    # print u"启动浏览器成功"
    # print u"访问163邮箱登录页..."
    # driver.get("http://mail.163.com")
    # # 暂停5s，以便邮箱登录页面加载完成
    # time.sleep(5)
    # assert u"163网易" in driver.title
    # print u"访问163邮箱登录页成功"
    #
    # wait = WaitUtil(driver)
    # wait.frame_available_and_switch_to_it("id", "x-URS-iframe")
    # print u"输入登录用户名"
    # username = getElement(driver, "xpath", "//input[@name='email]")
    # username.send_keys("xxx")
    # print u"输入登录密码"
    # passwd = getElement(driver, "xpath", "//input[@name='passwd']")
    # passwd.send_keys("xxx")
    # print u"登录..."
    # passwd.send_keys(Keys.ENTER)
    # # 等待5s, 以便登录成功后的页面加载完成
    # time.sleep(5)
    # assert u"网易邮箱" in driver.title
    # print u"登录成功"
    #
    # element = wait.visibility_element_located("xpath", "//span[text() = '写信'")
    # element.click()
    # print u"写信"
    # receiver = getElement(driver, "xpath",
    #                       "//div[contains(@id, '_mail_emailinput')]/input")
    # # 输入收信人地址
    # receiver.send_keys(u"xxx")
    # subject = getElement(driver, "xpath",
    #                      "//div[@aria-label='邮件主题输入框，请输入邮件主题]/input")
    # # 输入邮件主题
    # subject.send_keys(u"新邮件")
    # # 设置剪贴板内容
    # Clipboard.setText(r"d:\\a.txt")
    # # 获取剪贴板内容
    # attachment = getElement(driver, "xpath",
    #                         "//div[contains(@title, '600首MP3')]")
    # # 单击上传附件链接
    # attachment.click()
    # time.sleep(3)
    # # 在上传附件Windows弹窗中粘贴剪贴板中的内容
    # KeyboardKeys.twoKeys("ctrl", "v")
    # # 模拟回车键，以便加载要上传的附件
    # KeyboardKeys.oneKey("enter")
    # # 切换进邮件正文的frame
    # wait.frame_available_and_switch_to_it("xpath", "//iframe[@tabindex=1]")
    # body = getElement(driver, "xpath", "/html/body")
    # # 输入邮件正文
    # body.send_keys(u"发给光荣之路的一封信")
    # # 切出邮件正文的frame框
    # driver.switch_to.default_content()
    # print u"写信完成"
    # getElement(driver, "xpath", "//header//span[text()='发送']").click()
    # print u"开始发送邮件..."
    # time.sleep(3)
    # assert u"发送成功" in driver.page_source
    # print u"邮件发送成功"
    # driver.quit()

    print u"启动chrome浏览器"
    open_browser("chrome")
    maximize_browser()
    print u"访问163邮箱登录页"
    visit_url("http://mail.163.com")
    sleep(5)
    assert_string_in_pagesource(u"163")
    print u"访问163邮箱登录页成功"
    waitFrameToBeAvailableAndSwitchToIt("id", "x-URS-iframe")
    print u"输入登录用户名"
    input_string("xpath", "//input[@name='email']", "xxx")
    print u"输入登录密码"
    input_string("xpath", "//input[@name='password']", "xxx")
    click("id", "dologin")
    sleep(5)
    assert_title(u"网易邮箱")
    print u"登录成功"
    waitvisibilityOfElementLocated("xpath", "//span[text()='写信']")
    click("xpath", "//span[text()='写信']")
    print u"开始写信"
    print u"输入收件人地址"
    input_string("xpath",
                 "//div[contains(@id, '_mail_emailinput)]/input",
                 "xxx")
    print u"输入邮件主题"
    input_string("xpath",
                 "//div[@aria-label = '邮件主题输入框，请输入邮件主题']/input",
                 u"新邮件")
    print u"单击上传附件按钮"
    click("xpath", "//div[contains(@title, '600首MP3')]")
    sleep(3)
    print u"上传附件"
    paste_string(u"d:\\a.txt")
    press_enter_key()
    waitFrameToBeAvailableAndSwitchToIt("xpath", "//iframe[@tabindex=1]")
    print u"写入邮件正文"
    input_string("xpath", "/html/body", u"发给光荣之路的一封信")
    switch_to_default_content()
    print u"写信完成"
    print u"开始发送邮件..."
    click("xpath", "//header//span[text() = '发送']")
    time.sleep(3)
    assert_string_in_pagesource(u"发送成功")
    print u"邮件发送成功"
    close_browser()


if __name__ == '__main__':
    TestSendMailWithAttachment()
