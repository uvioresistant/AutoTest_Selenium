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
import time


def TestSendMailWithAttachment():
    # 创建Chrome浏览器的实例
    driver = webdriver.Chrome(executable_path="c:\\chromedriver")
    # 最大化浏览器窗口
    driver.maximize_window()
    print u"启动浏览器成功"
    print u"访问163邮箱登录页..."
    driver.get("http://mail.163.com")
    # 暂停5s，以便邮箱登录页面加载完成
    time.sleep(5)
    assert u"163网易" in driver.title
    print u"访问163邮箱登录页成功"

    wait = WaitUtil(driver)
    wait.frame_available_and_switch_to_it("id", "x-URS-iframe")
    print u"输入登录用户名"
    username = getElement(driver, "xpath", "//input[@name='email]")
    username.send_keys("xxx")
    print u"输入登录密码"
    passwd = getElement(driver, "xpath", "//input[@name='passwd']")
    passwd.send_keys("xxx")
    print u"登录..."
    passwd.send_keys(Keys.ENTER)
    # 等待5s, 以便登录成功后的页面加载完成
    time.sleep(5)
    assert u"网易邮箱" in driver.title
    print u"登录成功"

    element = wait.visibility_element_located("xpath", "//span[text() = '写信'")
    element.click()
    print u"写信"
    receiver = getElement(driver, "xpath",
                          "//div[contains(@id, '_mail_emailinput')]/input")
    # 输入收信人地址
    receiver.send_keys(u"xxx")
    subject = getElement(driver, "xpath",
                         "//div[@aria-label='邮件主题输入框，请输入邮件主题]/input")
    # 输入邮件主题
    subject.send_keys(u"新邮件")
    # 设置剪贴板内容
    Clipboard.setText(r"d:\\a.txt")
    # 获取剪贴板内容
    attachment = getElement(driver, "xpath",
                            "//div[contains(@title, '600首MP3')]")
    # 单击上传附件链接
    attachment.click()
    time.sleep(3)
    # 在上传附件Windows弹窗中粘贴剪贴板中的内容
    KeyboardKeys.twoKeys("ctrl", "v")
    # 模拟回车键，以便加载要上传的附件
    KeyboardKeys.oneKey("enter")
    # 切换进邮件正文的frame
    wait.frame_available_and_switch_to_it("xpath", "//iframe[@tabindex=1]")
    body = getElement(driver, "xpath", "/html/body")
    # 输入邮件正文
    body.send_keys(u"发给光荣之路的一封信")
    # 切出邮件正文的frame框
    driver.switch_to.default_content()
    print u"写信完成"
    getElement(driver, "xpath", "")






































def main(argv):
    """Do someting..."""
    return 0


if __name__ == '__main__':
    exit(main(sys.argv[1:]))