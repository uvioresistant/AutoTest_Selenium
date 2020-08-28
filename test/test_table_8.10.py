#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:fengg
@file:test_table_8.10.py
@time:2020/08/21
"""
from selenium import webdriver

driver = webdriver.Chrome(executable_path="F:\\Chrome\\chromedriver")
driver.get(r"G:\work_file\AutoTest_From_Git\test\test_html.html")
# 通过id定位获取整个表格对象
table = driver.find_element_by_id("table")
# 通过标签名获取表格中的所有行对象
trList = table.find_elements_by_tag_name("tr")
assert len(trList) == 5, "表格行数不符!"
for row in trList:
    # 遍历行对象，获取每一行中所有列对象
    # tdList = row.find_elements_by_tag_name("td")
    tdList = row.find_elements(by="tag name", value="td")

    # print tdList,123123123
    for col in tdList:
        # 遍历表格中的列，打印单元格内容
        print col.text + "\t"

cell = driver.find_element_by_xpath("//*[@id='table']/tbody/tr[2]/td[2]")
print cell.text, 23232323
cell = driver.find_element_by_xpath("//td[contains(., '化妆')]/input[1]")
print cell, 33333333444444444

driver.quit()

if __name__ == "__main__":
    pass