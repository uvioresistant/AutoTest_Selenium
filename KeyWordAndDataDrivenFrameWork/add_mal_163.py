#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:fengg
@file:add_mal_163.py
@time:2020/08/07
"""
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
print u"启动浏览器成功"
print u"访问163邮箱登录页..."
# 暂停5s,以便邮箱登录页加载完成
wait = WebDriverWait(driver, 30)
# 检查id为x-URS-iframe的frame是否存在，存在则切换进frame控件
wait.until(EC.frame_to_be_available_and_switch_to_it((By.ID, "x-URS-iframe")))
# 获取用户名输入框
userName = driver.find_element_by_xpath('//input[@name="email"]')
# 输入用户名
userName.send_keys("xxx")
# 获取密码输入框 //*[@id="auto-id-1594456531826"]
pwd = driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/form/div/div[3]/div[2]/input[2]")
# 输入密码
pwd.send_keys("xxx")
# 发送一个回车键
pwd.send_keys(Keys.RETURN)
print u"用户登录..."
time.sleep(5)

assert u"网易邮箱" in driver.title
print u"登录成功"
print u"添加联系人..."
# 显示等待通讯录链接页面元素的出现
addressBook = wait.until(EC.visibility_of_all_elements_located((By.XPATH, "//div[text()='通讯录']")))
# 单击"通讯录"按钮
addressBook.click()

# 显示等待新建联系人按钮的出现
newContact = wait.until(EC.visibility_of_all_elements_located((By.XPATH, "//span[text()='新建联系人']")))
# 单击"新建联系人"按钮
addressBook.click()

# 显示等待新建联系人输入框的出现
contactName = wait.until(EC.visibility_of_all_elements_located
                         ((By.XPATH, "//a[@title='编辑详细姓名']/preceding-sibling::div/input")))
contactName.send_keys(u"lily")
# 输入联系人电子邮箱
driver.find_element_by_xpath("//*[@id='iaddress_MAIL_wrap']//input").send_keys(u"lily@qq.com")
driver.find_element_by_xpath("//span[text()='设为星标联系人']/preceding-sibling::span/b").click()
# 输入联系人手机号
driver.find_element_by_xpath("//*[id='iaddress_TEL_wrap']//dd/input").send_keys("185xxxxxxxx")
# 输入备注信息
driver.find_element_by_xpath('//*[@id="input_DETAIL"]').send_keys("朋友")
# 单击"确认"
driver.find_element_by_xpath('//*[@id="_mail_button_40_417"]/span').click()
time.sleep(2)

assert "lily@qq.com" in driver.page_source
print u"添加联系人成功"

print u"进入首页"
driver.find_element_by_xpath('//div[.="首页"]').click()
print u"写信..."
# 显示等待写信链接页面元素的出现
element = wait.until(EC.visibility_of_all_elements_located((By.XPATH, "//span[text()='写信']")))
# 单击写信链接
element.click()
# 写入收件人地址
driver.find_element_by_xpath("//div[contains(@id, '_mail_emailinput)]/input").send_keys("xxx@qq.com")
# 写入邮件主题
driver.find_element_by_xpath("//div[@aria-label='邮件主题输入框，请输入邮件主题").send_keys("发送给伟大的卫国战争的一封信")
# 切换进frame控件
driver.switch_to.frame(driver.find_element_by_xpath("//iframe[@tabindex=1]"))
editBox = driver.find_element_by_xpath("/html/body")
editBox.send_keys(u"发送给伟大的卫国战争的一封信")
driver.find_element_by_xpath("//header//span[text()='发送']").click()
print u"开始发送邮件..."
time.sleep(3)
assert u"发送成功" in driver.page_source
print u"邮件发送成功"
driver.quit()



if __name__ == "__main__":
    pass