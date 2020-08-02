#!usr/bin/env python
#-*- coding:utf-8 -*-
"""
@author:fengg
@file: mail_126.py
@time: 2020/07/11
"""
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


# 创建Chrome浏览器的实例
driver = webdriver.Chrome(executable_path="F:\\Chrome\\chromedriver.exe")
# 设置隐式等待时间为10s
driver.implicitly_wait(10)
# 最大化浏览器窗口
driver.maximize_window()

# 访问126邮箱登录页面
driver.get("https://mail.163.com/")
# 暂停5s，等待登录页面加载完成
time.sleep(5)
# 切换进frame控件
driver.switch_to.frame("x - URS - iframe")
# 获取用户名输入框 //*[@id="auto-id-1594456531823"]
userName = driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[2]/form/div/div[1]/div[2]/input')
# 输入用户名
userName.send_keys("xxx")
# 获取密码输入框 //*[@id="auto-id-1594456531826"]
pwd = driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/form/div/div[3]/div[2]/input[2]")
# 输入密码
pwd.send_keys("xxx")
# 发送一个回车键
pwd.send_keys(Keys.RETURN)

# 等待10s，登录成功后的页面加载完成
time.sleep(10)
# 单击"通讯录"按钮 /html/body/header/nav/div[1]/ul/li[2]/div[3]
driver.find_element_by_xpath('//*[@id="_mail_tabitem_1_4text"]').click()
time.sleep(2)
# 单击“新建联系人”按钮 /html/body/div[2]/div[1]/div[3]/header/div/div[1]/div/span[2]
driver.find_element_by_xpath('//*[@id="_mail_button_16_259"]/span[2]')
time.sleep(2)

# 输入联系人姓名 /html/body/div[9]/div[2]/div/div/div[1]/div/div[1]/dl[1]/dd/div/input
driver.find_element_by_xpath('//*[@id="input_N"]').send_keys(u"lucy")
# 输入联系人电子邮箱 /html/body/div[9]/div[2]/div/div/div[1]/div/div[1]/div[1]/dl/dd/div/input
driver.find_element_by_xpath('//*[@id="_mail_input_6_301"]/input').send_keys(u"xxx@qq.com")
driver.find_element_by_xpath('//*[@id="fly79"]').click()
time.sleep(2)
# 输入联系人手机号
driver.find_element_by_xpath('//*[@id="_mail_input_7_306"]/input').send_keys("13511111111")
time.sleep(2)
# 输入备注信息
driver.find_element_by_xpath('//*[@id="input_DETAIL"]').send_keys("朋友")
# 单击"确认"
driver.find_element_by_xpath('//*[@id="_mail_button_40_417"]/span').click()
time.sleep(2)

driver.quit()

# 将上面程序改成数据驱动测试框架


def func():
    pass


class Main():
    def __init__(self):
        pass


if __name__ == "__main__":
    pass