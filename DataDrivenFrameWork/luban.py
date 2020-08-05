#!usr/bin/env python
#-*- coding:utf-8 -*-
"""
@author:fengg
@file: luban.py
@time: 2020/07/11
"""
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


# 创建Chrome浏览器的实例
driver = webdriver.Chrome(executable_path="H:\\chromedriver.exe")
# 设置隐式等待时间为3s
driver.implicitly_wait(3)
# 最大化浏览器窗口
driver.maximize_window()
# 访问鲁班登录页面
driver.get("http://128.196.108.10:8080/#/login")
# 暂停3s，等待登录页面加载完成
time.sleep(3)
# 获取用户名输入框
userName = driver.find_element_by_xpath('//*[@id="app"]/div/form/div[2]/div/div/input')
# 输入用户名
userName.send_keys("huangwk")
# 获取密码输入框
pwd = driver.find_element_by_xpath('//*[@id="app"]/div/form/div[3]/div/div/input')
# 输入密码
pwd.send_keys("abc123456")

# 单击"域名"按钮
driver.find_element_by_xpath('//*[@id="app"]/div/form/div[4]/div[1]/div/div[1]/div/input').click()
time.sleep(2)

# 单击"域名下拉显示"框
driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[1]/ul/li[3]/span"]').click()
time.sleep(2)


# 单击"租户英文名"按钮
driver.find_element_by_xpath('//*[@id="app"]/div/form/div[4]/div[2]/div/div/div/input').click()
time.sleep(2)

# 单击"租户英文名下拉显示"框
driver.find_element_by_xpath('/html/body/div[3]/div[1]/div[1]/ul/li[3]/span').click()
time.sleep(2)

# 单击"登录"
driver.find_element_by_xpath('//*[@id="app"]/div/form/button/span').click()
time.sleep(5)

driver.quit()