#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:fengg
@file:test_WebDriver API.py
@time:2020/08/25
"""
from selenium import webdriver
import unittest
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
import time

import win32api
import win32con
import time

# backspace'	0x08
# tab	0x09
# clear	0x0C
# enter	0x0D
# shift	0x10
# ctrl	0x11
# alt	0x12
# pause	0x13
# caps_lock	0x14
# esc	0x1B
# spacebar	0x20
# page_up	0x21
# page_down	0x22
# end	0x23
# home	0x24
# left_arrow	0x25
# up_arrow	0x26
# right_arrow	0x27
# down_rrow	0x28
# select	0x29
# print	0x2A
# execute	0x2B
# print_screen	0x2C
# ins	0x2D
# del	0x2E
# help	0x2F
# 0	0x30
# 1	0x31
# 2	0x32
# 3	0x33
# 4	0x34
# 5	0x35
# 6	0x36
# 7	0x37
# 8	0x38
# 9	0x39
# a	0x41
# b	0x42
# c	0x43
# d	0x44
# e	0x45
# f	0x46
# g	0x47
# h	0x48
# i	0x49
# j	0x4A
# k	0x4B
# l	0x4C
# m	0x4D
# n	0x4E
# o	0x4F
# p	0x50
# q	0x51
# r	0x52
# s	0x53
# t	0x54
# u	0x55
# v	0x56
# w	0x57
# x	0x58
# y	0x59
# z	0x5A

VK_CODE = {
    'enter': 0x0D,
    'ctrl': 0x11,
    'a': 0x41,
    'v': 0x56,
    'x': 0x58
}


# 键盘键按下
def keyDown(keyName):
    win32api.keybd_event(VK_CODE[keyName], 0, 0, 0)


# 键盘键抬起
def keyUp(keyName):
    win32api.keybd_event(VK_CODE[keyName], 0, win32con.KEYEVENTF_KEYUP, 0)


from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
import win32clipboard as w
import win32con
import time


# 读取剪切板
def getText():
    w.OpenClipboard()
    d = w.GetClipboardData(win32con.CF_TEXT)
    w.CloseClipboard()
    return d


# 设置剪贴板内容
def setText(aString):
    w.OpenClipboard()
    w.EmptyClipboard()
    w.SetClipboardData(win32con.CF_UNICODETEXT, aString)
    w.CloseClipboard()


class VisitSogouByChrome(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="F:\\Chrome\\chromedriver")

    @unittest.skip("skipping")
    def test_visitSougou(self):
        self.driver.get("http://www.sougou.com")
        print self.driver.current_url

    @unittest.skip("skipping")
    def test_visitURL(self):
        visitURL = "http://www.sougou.com"
        self.driver.get(visitURL)
        assert self.driver.title.find(u"搜狗搜索引擎") >= 0, "assert error"

    @unittest.skip("skipping")
    def test_visitRecentURL(self):
        firstVisitURL = "http://www.sogou.com"
        secondVisitURL = "http://www.baidu.com"
        self.driver.get(firstVisitURL)
        self.driver.get(secondVisitURL)
        # 返回上一次访问过的搜狗首页
        self.driver.back()
        # 再次回到百度首页
        self.driver.forward()

    @unittest.skip("skipping")
    def test_refreshCurrentPage(self):
        url = "http://www.sougou.com"
        self.driver.get(url)
        # 刷新当前页面
        self.driver.refresh()

    @unittest.skip("skipping")
    def test_maximizeWindow(self):
        url = "http://www.baicu.com"
        self.driver.get(url)
        # 最大化浏览器窗口，以便占满整个电脑屏幕
        self.driver.maximize_window()

    @unittest.skip("skipping")
    def test_window_position(self):
        """
        1) 获取的位置是浏览器左上角所在的屏幕上的位置
        2) get_window_position()和set_window_position()在部分浏览器部分版本失效
        :return: x，y坐标值
        """
        url = "http://www.baidu.com"
        self.driver.get(url)
        # 获取当前浏览器在屏幕上的位置，返回的是字典对象
        position = self.driver.get_window_position()
        print "当前浏览器所在位置的横坐标:", position['x']
        print "当前浏览器所在位置的纵坐标:", position['y']
        # 设置当前浏览器在屏幕上的位置
        self.driver.set_window_position(y=200, x=400)
        # 设置浏览器的位置后，再次获取浏览器的位置信息
        print self.driver.get_window_position()

    @unittest.skip("skipping")
    def test_window_size(self):
        url = "http://www.baidu.com"
        self.driver.get(url)
        # 获取浏览器窗口的大小，返回字典类型
        sizeDict = self.driver.get_window_size()
        print "当前浏览器窗口的宽: ", sizeDict['width']
        print "当前浏览器窗口的高: ", sizeDict['height']
        # 设置浏览器窗口的大小
        self.driver.set_window_size(width=200, height=400, windowHandle='current')
        # 设置窗口大小后，再次获取窗口大小信息
        print self.driver.get_window_size(windowHandle='current')

    @unittest.skip("skipping")
    def test_getTitle(self):
        url = "http://www.baidu.com"
        self.driver.get(url)
        # 调用driver 的title属性值，获取页面的title属性值
        title = self.driver.title
        print "当前网页的title属性值为: ", title
        # 断言页面的title属性值是否是"百度一下，你就知道"
        self.assertEqual(title, u"百度一下，你就知道", "页面title属性值错误!")

    @unittest.skip("skipping")
    def test_getPageSource(self):
        url = "http://www.sogou.com"
        self.driver.get(url)
        # 调用driver的page_souce属性获取页面源码
        pageSource = self.driver.page_source
        print pageSource
        # 断言页面源码中是否包含"新闻"两个关键字，判断页面内容是否正确
        self.assertTrue(u"新闻" in pageSource, "页面源码中未找到'新闻'关键字")

    @unittest.skip("skipping")
    def test_getCurrentPageUrl(self):
        url = "http://www.sogou.com"
        self.driver.get(url)
        # 获取当前页面的URL
        currentPageUrl = self.driver.current_url
        print currentPageUrl
        self.assertEqual(currentPageUrl, "https://www.sogou.com/", "当前网页网址非预期")

    @unittest.skip("skipping")
    def test_operateWindowHandle(self):
        url = "http://www.baidu.com"
        self.driver.get(url)
        now_handle = self.driver.current_window_handle
        # 百度搜索输入框输入"selenium"
        self.driver.find_element_by_id("kw").send_keys("w3cschool")
        self.driver.find_element_by_id("su").click()
        import time
        self.driver.find_element_by_xpath("//div[@id='1']//a[text()='w3']").click()
        time.sleep(5)
        # driver.window_handles以列表对象返回所有打开窗口的句柄，包括主窗口
        all_handles = self.driver.window_handles
        # 通过driver.window_handles[-1]来获取当前窗口的句柄
        print "+++", self.driver.window_handles[-1]
        # 循环遍历所有新打开的窗口句柄，也就是说不包括主窗口
        for handle in all_handles:
            if handle != now_handle:
                # 输出待选择的窗口句柄
                '''
                此方法在selenium3.x后官方不推荐
                self.driver.switch_to_window(handle)
                '''
                self.driver.switch_to.window(handle)
        self.driver.find_element_by_link_text('HTML5').click()
        time.sleep(3)
        # 关闭当前的窗口
        self.driver.close()
        time.sleep(3)
        # 打印主窗口句柄
        print now_handle
        # 返回主窗口
        self.driver.switch_to.window(now_handle)
        time.sleep(2)
        self.driver.find_element_by_id("kw").click()
        self.driver.find_element_by_id("kw").send_keys(u"伟大的卫国战争")
        self.driver.find_element_by_id("su").click()
        time.sleep(5)

    @unittest.skip("skipping")
    def test_getBasicInfo(self):
        url = "http://www.baidu.com"
        self.driver.get(url)

    @unittest.skip("skipping")
    def test_clickButton(self):
        url = "G:\\work_file\\AutoTest_From_Git\\test\\test_html.html"
        self.driver.get(url)
        inputBox = self.driver.find_element_by_id("inputBox")
        # 导入支持双击操作的模块
        from selenium.webdriver import ActionChains
        # 开始模拟鼠标双击操作
        action_chains = ActionChains(self.driver)
        action_chains.double_click(inputBox).perform()
        time.sleep(3)

    @unittest.skip("skipping")
    def test_printSelectText(self):
        url = "G:\\work_file\\AutoTest_From_Git\\test\\test_html.html"
        self.driver.get(url)
        select = self.driver.find_element_by_name("fruit")
        all_options = select.find_elements_by_tag_name("option")
        for option in all_options:
            print "选项显示的文本:", option.text
            print "选项值为: ", option.get_attribute("value")
            option.click()
            time.sleep(1)

    @unittest.skip("skipping")
    def test_operateDropList(self):
        url = "G:\\work_file\\AutoTest_From_Git\\test\\test_html.html"
        self.driver.get(url)
        from selenium.webdriver.support.ui import Select
        select_element = Select(self.driver.find_element_by_xpath("//select"))
        # 打印默认选中项的文本
        print select_element.first_selected_option.text
        # 获取所有选择项的页面元素对象
        all_options = select_element.options
        # 打印选项总个数
        print len(all_options)
        '''
        is_enabled(): 判断元素是否可操作
        is_selected(): 判断元素是否被选中
        '''
        if all_options[1].is_enabled() and not all_options[1].is_selected():
            # 方法一: 通过序号选择第二个元素,序号从0开始
            select_element.select_by_index(1)
            # 打印已选中项的文本
            print select_element.all_selected_options[0].text
            # assertEqual()方法断言当前选中的是否是"西瓜"
            self.assertEqual(select_element.all_selected_options[0].text, u"西瓜")
        time.sleep(2)
        # 方法二：通过选项的显示文本选择文本为"猕猴桃"选项
        select_element.select_by_visible_text("猕猴桃")
        # 断言已选中项的文本是否是"猕猴桃"
        self.assertEqual(select_element.all_selected_options[0].text, u"猕猴桃")
        time.sleep(2)
        # 方法三：通过选项的value属性值选择value="shanzha"选项
        select_element.select_by_value("shanzha")
        print select_element.all_selected_options[0].text
        self.assertEqual(select_element.all_selected_options[0].text, u"山楂")

    def test_checkSelectText(self):
        url = "G:\\work_file\\AutoTest_From_Git\\test\\test_html.html"
        self.driver.get(url)
        from selenium.webdriver.support.ui import Select
        # 获取select页面元素对象
        select_element = Select(self.driver.find_element_by_xpath("//select"))
        # 获取所有选择项的页面元素对象
        actual_options = select_element.options
        # 声明一个list对象，存储下拉列表中所期望出现的文字内容
        expect_optionList = [u"桃子", u"西瓜", u"橘子", u"猕猴桃", u"山楂", u"荔枝"]
        # 使用map()函数获取页面中下拉列表展示的内容组成的列表对象
        actual_optionsList = map(lambda option: option.text, actual_options)
        # 断言期望列表对象和实际列表对象是否完全一致
        self.assertListEqual(expect_optionList, actual_optionsList)

    @unittest.skip("skipping")
    def test_Handleconfirm(self):
        from selenium.common.exceptions import NoAlertPresentException
        import time
        url = "G:\\work_file\\AutoTest_From_Git\\test\\test_html.html"
        self.driver.get(url)
        # 通过id属性值查找页面上的按钮元素
        button = self.driver.find_element_by_id("button")
        # 单击按钮元素，弹出confirm提示框，显示“这是一个confirm弹出框"以及"确定""取消"按钮
        button.click()
        try:
            # driver.switch_to.alert方法来获取alert对象
            alert = self.driver.switch_to.alert
            time.sleep(2)
            # 使用alert.text属性获取confirm框中的内容，并断言文字内容是否是"这是一个confirm弹出框"
            self.assertEqual(alert.text, u"这是一个confirm弹出框")
            # 调用alert.accept()，模拟鼠标单击confirm弹窗上的“确定”按钮
            alert.accept()
            # 模拟单击confirm上的"取消"按钮
            # alert.dismiss()

        except NoAlertPresentException, e:
            self.fail('尝试操作的confirm框未被找到')
            print e

    @unittest.skip("skipping")
    def testHandlePrompt(self):
        url = "G:\\work_file\\AutoTest_From_Git\\test\\test_html.html"
        self.driver.get(url)
        element = self.driver.find_element_by_id("button")
        element.click()
        import time
        time.sleep(1)
        # 使用alert.switch_to.alert获取Alert对象
        alert = self.driver.switch_to.alert
        # 使用alert.text获取prompt框上面的文字，断言文字内容是否和"这是一个prompt弹出框"一致
        self.assertEqual(u"这是一个prompt弹出框", alert.text)
        time.sleep(1)
        alert.send_keys(u"伟大的卫国战争")
        time.sleep(1)
        # 使用alert的accept方法，单击prompt框的"确定"按钮，关闭prompt框
        alert.accept()
        # 使用alert的dismiss方法，单击prompt框上是"取消"按钮，关闭prompt框
        # alert.dismiss()

    @unittest.skip("skipping")
    def test_Cookie(self):
        url = "http://www.sogou.com"
        self.driver.get(url)
        # 得到当前页面下所有的Cookies, 并输出它们所在域、name、value、有效期和路径
        cookies = self.driver.get_cookies()
        for cookie in cookies:
            print "%s -> %s -> %s -> %s -> %s" % (cookie['domain'], cookie["name"],
                                                  cookie["value"], cookie["expiry"], cookie["path"])
        # 根据Cookie的name值获取该条Cookie信息，获取name值为'SUV'的Cookie信息
        ck = self.driver.get_cookie("SUV")
        print "%s -> %s -> %s -> %s -> %s" % (cookie['domain'], cookie["name"],
                                              cookie["value"], cookie["expiry"], cookie["path"])

        # 删除cookie有两种方法
        # 第一种：通过Cookie的name属性，删除name值为"ABTEST"的Cookie信息
        print self.driver.delete_cookie("ABTEST")

        # 第二种: 一次性删除全部Cookie信息
        self.driver.delete_all_cookies()
        # 删除全部Cookie后，再次查看Cookies,确认是否已被全部删除
        cookies = self.driver.get_cookies()
        print cookies

        # 添加自定义Cookie信息
        self.driver.add_cookie({"name": "gloryroadTrain", 'value': '14792342341423'})
        # 查看添加的Cookie信息
        cookie = self.driver.get_cookie("gloryroadTrain")
        print cookie

    @unittest.skip("skipping")
    def test_simulationCombinationKeys(self):
        url = "G:\\work_file\\AutoTest_From_Git\\test\\test_html.html"
        self.driver.get(url)
        # 将焦点切换到搜索输入框中
        input = self.driver.find_element_by_id("kw")
        input.click()
        input.send_keys(u"伟大的卫国战争")
        time.sleep(2)
        # 执行Ctrl + a
        ActionChains(self.driver).key_down(Keys.CONTROL).send_keys('a').key_up(Keys.CONTROL).perform()
        time.sleep(2)
        # 执行Ctrl + x
        ActionChains(self.driver).key_down(Keys.CONTROL).send_keys('x').key_up(Keys.CONTROL).perform()
        self.driver.get(url)
        self.driver.find_element_by_id("kw").click()
        # 模拟Ctrl + v，将从剪切板中获取到的内容，粘贴到搜索输入框中
        ActionChains(self.driver).key_down(Keys.CONTROL).send_keys('v').key_up(Keys.CONTROL).perform()
        self.driver.find_element_by_id('su').click()
        time.sleep(3)

    @unittest.skip("skipping")
    def test_simulationCombinationKeysByWin32(self):
        url = "http://www.sogou.com"
        self.driver.get(url)
        # 找到搜索输入框元素
        searchBox = self.driver.find_element_by_id("query")
        # 将焦点切换到搜索输入框中
        searchBox.click()
        # 搜索输入框中输入"伟大的卫国战争"
        searchBox.send_keys(u"伟大的卫国战争")
        time.sleep(2)
        # 模拟Ctrl + a，选中输入框中所有的内容
        keyDown('Ctrl')
        keyDown('A')
        # 释放Ctrl + a
        keyUp('A')
        keyUp('Ctrl')
        # 模拟Ctrl + X剪切所选中的内容
        keyDown('Ctrl')
        keyDown('X')
        keyUp('X')
        keyUp('Ctrl')
        self.driver.get("http://www.baidu.com")
        # 将焦点切换到搜索框中
        self.driver.find_element_by_id("kw").click()
        # 模拟Ctrl + V, 进行粘贴
        keyDown('Ctrl')
        keyDown('V')
        keyUp('V')
        keyUp('Ctrl')
        # 模拟回车键
        keyDown('enter')
        keyUp('enter')
        time.sleep(5)

    @unittest.skip("skipping")
    def test_copyAndPaste(self):
        url = "http://www.baidu.com"
        self.driver.get(url)
        content = u'伟大的卫国战争'
        # 将content变量中的内容设置到剪贴板中
        setText(content)
        # 从剪贴板中获取刚设置到剪贴板中的内容
        getContent = getText()
        print getContent.decode("gbk").encode("utf-8")
        # 将焦点切换到搜索输入框中
        self.driver.find_element_by_id("kw").click()
        # 模拟Ctrl + V组合键，将从剪贴板中获取到的内容粘贴到搜索输入框中
        # key_down(Keys.CONTROL)表按下Ctrl键，send_keys('v')类似模拟了V键，组合起来就是Ctrl + V,
        # key_up(Keys.CONTROL)表示释放Ctrl键
        ActionChains(self.driver).key_down(Keys.CONTROL).send_keys('v').key_up(Keys.CONTROL).perform()
        self.driver.find_element_by_id('su').click()
        time.sleep(3)

    def tearDown(self):
        self.driver.quit()


from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
import time
import unittest

# class setPageLoadTime(unittest.TestCase):
#     def setup(self):
#         self.driver = webdriver.Chrome(executable_path="F:\\Chrome\\chromedriver")
#
#     def test_PageLoadTime(self):
#         # 设定页面加载限制时间为4s
#         self.driver.set_page_load_timeout(4)
#         self.driver.maximize_window()
#         try:
#             startTime = time.time()
#             self.driver.get("http://mail.163.com")
#         except TimeoutException:
#             print u'页面加载操作设定时间，超时'
#             # 当页面加载超时，通过执行JS来停止加载，然后继续执行后续动作
#         end = time.time() - startTime
#         print end
#         # 切换进frame控件
#         self.driver.switch_to.frame("x-URS-iframe")
#         # 获取用户名输入框
#         userName = self.driver.find_element_by_xpath("//input[@name='email']")
#         # 输入用户名
#         userName.send_keys("xxx")
#         # 获取密码输入框
#         pwd = self.driver.find_element_by_xpath("//input[@name='password']")
#         # 输入密码
#         pwd.send_keys("xxx")
#         # 发送一个Enter键
#         pwd.send_keys(Keys.RETURN)
#
#     def tearDown(self):
#         self.driver.quit()


if __name__ == "__main__":
    # unittest.main()
    testCases = unittest.TestLoader().loadTestsFromTestCase(VisitSogouByChrome)
    suite = unittest.TestSuite(testCases)
    unittest.TextTestRunner(verbosity=2).run(suite)
