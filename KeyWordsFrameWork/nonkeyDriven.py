# !/usr/bin/env python
# -- coding: utf-8 --
# title = '' 
# author = '20991' 
# mtime = '2020/7/25'
__author__ = 'YourName'

import sys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


print u"启动浏览器..."
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
wait = WebDriverWait(driver, 30)
# 检查id为x - URS - iframe的frame是否存在，存在则切换进frame控件
wait.until(EC.frame_to_be_available_and_switch_to_it((By.ID, "x - URS - iframe")))
# 获取用户名输入框
userName = driver.find_element_by_xpath('//input[@name="email"]')
# 输入用户名
userName.send_keys("xxx")
# 获取密码输入框
pwd = driver.find_element_by_xpath('//input[@name = "password"]')
# 输入密码
pwd.send_keys("xxx")
# 发送一个回车键
pwd.send_keys(Keys.RETURN)
print u"用户登录..."
# 等待5s,以便登录成功后的页面加载完成
time.sleep(5)
assert u"网易邮箱" in driver.title
print u"登录成功"
print u"写信..."
# 显示等待写信链接页面元素的出现"//span[text() = '写信']"
element = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="_mail_component_137_137"]/span[2]')))
# 单击写信链接
element.click()
# 写入收件人地址'//div[contains(@id, '_mail_emailinput)]/input'
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





def main(argv):
    """Do someting..."""
    return 0


if __name__ == '__main__':
    exit(main(sys.argv[1:]))