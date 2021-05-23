#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:fengg
@file:test_HighWebDriver.py
@time:2020/08/27
"""
import os

import win32clipboard as w
import win32con
import win32api
from selenium import webdriver
from selenium.common.exceptions import WebDriverException, TimeoutException, NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
import unittest
import traceback
import time

# 用于设置剪切板内容
def setText(aString):
    w.OpenClipboard()
    w.EmptyClipboard()
    w.SetClipboardData(win32con.CF_UNICODETEXT, aString)
    w.CloseClipboard()

# 键盘按键映射字典
VK_CODE = {
    'enter': 0x0D,
    'ctrl': 0x11,
    'v': 0x56
}

# 键盘按下
def keyDown(keyName):
    win32api.keybd_event(VK_CODE[keyName], 0, 0, 0)
# 键盘抬起
def keyUp(keyName):
    win32api.keybd_event(VK_CODE[keyName], 0, win32con.KEYEVENTF_KEYUP, 0)


class TestDemo(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="F:\\Chrome\\chromedriver")

    # 11.1.使用JS操作元素
    @unittest.skip("skipping")
    def test_executeScript(self):
        url = "http://www.baidu.com"
        self.driver.get(url)
        # 构造JS查找百度首页的搜索输入框的代码字符串
        searchInputBoxJS = "document.getElementById('kw').value='伟大的卫国战争';"
        # 构造JS查找百度首页的搜索按钮的代码字符串
        searchButtonJS = "document.getElementById('su').click()"
        try:
            # 通过JS代码在百度首页搜索输入框中输入'伟大的卫国战争'
            self.driver.execute_script(searchInputBoxJS)
            time.sleep(2)
            # 通过JS代码单击百度首页上的搜索按钮
            self.driver.execute_script(searchButtonJS)
            time.sleep(2)
            self.assertTrue(u"百度百科" in self.driver.page_source)
        except WebDriverException, e:
            print u"在页面中没有找到要操作的页面元素", traceback.print_exc()
        except AssertionError, e:
            print u"页面不存在断言的关键字串"
        except Exception, e:
            print traceback.print_exc()

    # 11.2.操作Web页面的滚动条
    @unittest.skip("skipping")
    def test_scroll(self):
        url = "http://www.seleniumhq.org/"
        try:
            self.driver.get(url)
            # 使用JS的scrollTo和document.body.scrollHeight参数,将页面的滚动条滑动到页面的最下方
            self.driver.execute_script("window.scrollTo(100, document.body.scrollHeight);")
            time.sleep(3)

            # 使用JS的scrollIntoView将被遮挡的元素滚动到可见屏幕上
            # scrollIntoView(true)表示将元素滚动屏幕中间
            # scrollIntoView(false)表示将元素滚动到屏幕底部
            self.driver.execute_script("document.getElementById('choice').scrollIntoView(true);")
            # 停顿3s，用于人工验证滚动条是否滑动到指定的位置
            time.sleep(3)

            # 使用JS的scrollBy方法，使用0和400横纵坐标参数,将页面纵向向下滚动400像素
            self.driver.execute_script("window.scrollBy(0,400);")
            # 停顿3s，用于人工验证滚动条是否滑动到指定的位置
            time.sleep(3)
        except Exception, e:
            print traceback.print_exc()

    # 11.6.自动下载某个文件
    @unittest.skip("skipping")
    def test_download(self):
        def setUp(self):
            self.driver = webdriver.Chrome(executable_path="F:\\Chrome\\chromedriver")
            profile = webdriver.FirefoxProfile()
            # 指定下载路径，默认只会创建一级目录，如果指定了多级不存在的目录，将会下载到默认路径
            profile.set_preference('browser.download.dir', 'd:\\iDownload')
            # 将browser.download.folderList设置为2，表示将文件下载到指定路径
            # 设置成2表示使用自定义下载路径；
            # 设置成0表示下载到桌面;
            # 设置成1表示下载到默认路径
            profile.set_preference('browser.download.folerList', 2)
            # browser.helperApps.alwaysAsk.force对于未知的MIME类型文件会弹出窗口让用户处理，
            # 默认值为True，设定为False表示不会记录打开未知MIME类型文件的方式
            profile.set_preference("browser.helperApps.alwaysAsk.force", False)
            # 在开始下载时是否显示下载管理器
            profile.set_preference('browser.download.manager.showWhenStarting', False)
            # 设定为False会把下载框进行隐藏
            profile.set_preference("browser.download.manager.useWindow", False)
            # 默认值为True,设定为False表示不获取焦点
            profile.set_preference("browser.download.manager.focusWhenStarting", False)
            # 下载.exe问价你弹出警告，默认值是True,设定为False则不会弹出警告框
            profile.set_preference("browser.download.manager.alertOnEXEOpen", False)
            # browser.helperApps.neverAsk.openFile表示直接打开下载文件，不显示确认框默认值为空字符串，
            # 下行代码行设定了多个文件的MIME类型，例如application/exe, 表示.exe类型的文件，application/excel表示Excel类型的文件
            profile.set_preference("browser.helperApps.neverAsk.openFile", "application/pdf")
            # 对所给出文件类型不再弹出提示框进行询问，直接保存到本地磁盘
            # profile.download.manager.showAlertOnComplete设定下载文件结束后是否显示下载完成提示框，默认为True，
            # 设定为False表示下载完成后不显示下载完成提示框
            profile.set_preference("browser.download.manager.showAlertOnComplete", False)
            # browser.download.manager.closeWhenDone设定下载结束后是否自动
            # 关闭下载框，默认值为True，设定为False表示不关闭下载管理器
            profile.set_preference("browser.download.manager.closeWhenDone", False)
            # 启动浏览器时，通过firefox_profile参数
            # 将自动配置添加到FirefoxProfile对象中
            self.driver = webdriver.Firefox(executable_path="F:\\Chrome\\chromedriver", firefox_profile=profile)

        def test_dataPicker(self):
            # 访问WebDriver驱动Firefox的驱动文件下载网址
            url1 = "https://github.com/mozilla/geckodriver/releases"
            self.driver.get(url1)
            # 选择下载ZIP类型文件，使用application/zip指代此类型文件
            self.driver.find_element_by_xpath('//strong[.="geckodriver-v0.11.1-win64.zip"]').click()
            # 等待加载下载文件
            time.sleep(10)

            # 访问Python2.7.12文件下载页面，下载拓展名为msi的文件
            # 使用application/octet-stream来指明此类文件类型
            url = "https://www.python.org/downloads/release/p ython-2712/"
            self.driver.get(url)
            # 找到Python2.7.12下载页面中链接文件为"Windowx x68 - 64 MSI installer"的链接页面元素，
            # 单击进行无人干预的下载Python2.7.12解释器文件
            self.driver.find_element_by_link_text("Windows x86-64MSI installer").click()
            # 等待文件下载完成，根据各自的网路带宽情况设定等待相应的时间
            time.sleep(100)

    # 11.7.自动上传附件
    # 11.7.1.使用WebDriver的send_keys方法上传文件
    def test_uploadFileBySendKeys(self):
        url = "d:\\uploadFile.html"
        # 访问自定义网页
        self.driver.get(url)
        try:
            wait = WebDriverWait(self.driver, 10, 0.2)
            # 显示等待判断被测试页面上的上传文件按钮是否处于可被单机状态
            wait.until(EC.element_to_be_clickable((By.ID, 'file')))
        except TimeoutException, e:
            print traceback.print_exc()
        except NoSuchElementException, e:
            print traceback.print_exc()
        except Exception, e:
            print traceback.print_exc()
        else:
            # 查找页面上ID属性值为"file"的文件上传框
            fileBox = self.driver.find_element_by_id("file")
            # 在文件上传框的路径框里输入要上传的文件路径"c:\\test.txt"
            fileBox.send_keys("c:\\test.txt")
            # 暂停查看上传的文件
            time.sleep(4)
            # 找到页面上ID属性值为"filesubmit"的文件提交按钮对象
            fileSubmitButton = self.driver.find_element_by_id("filesubmit")
            # 单击提交按钮，完成文件上传操作
            fileSubmitButton.click()
            # 因为文件上传需要时间，所以可以添加显示等待场景，
            # 判断文件上传成功后，页面是否跳转到文件上传成功的页面。
            # 通过EC.title_is()方法判断跳转后的页面的Title值是否符合期望，如果匹配，将继续执行后续代码

            # 如果实现了parse_file.jsp页面，且可以成功调转，可断言文件上传成功
            wait.until(EC.title_is(u"文件上传成功"))

    # 11.7.2.使用模拟键盘操作：实现上传文件
    def test_uploadFileByKeyboard(self):
        url = "d:\\uploadFile.html"
        self.driver.get(url)
        try:
            wait = WebDriverWait(self.driver, 10, 0.2)
            # 显示等待判断被测试页面上的上传文件按钮是否处于可被单机状态
            wait.until(EC.element_to_be_clickable((By.ID, 'file')))
        except TimeoutException, e:
            print traceback.print_exc()
        except NoSuchElementException, e:
            print traceback.print_exc()
        except Exception, e:
            print traceback.print_exc()
        else:
            # 将即将要上传的文件名及路径设置到剪贴板中
            setText(u"c:\\test.txt")
            # 查找页面上ID属性值为"file"的文件上传框,并单击调出选择文件上传框
            self.driver.find_element_by_id("file").click()
            time.sleep(2)
            # 模拟键盘按下Ctrl + V组合键
            keyDown("Ctrl")
            keyDown("V")
            # 模拟键盘释放Ctrl+V组合键
            keyUp("V")
            keyDown("Ctrl")
            time.sleep(1)
            # 模拟键盘按下回车键
            keyDown("enter")
            # 模拟键盘释放回车键
            keyUp("enter")
            # 暂停查看上传的文件
            time.sleep(2)
            # 找到页面上ID属性值为"filesubmit"的文件提交按钮对象
            fileSubmitButton = self.driver.find_element_by_id("filesubmit")
            # 单击提交按钮，完成文件上传操作
            fileSubmitButton.click()
            # 因为文件上传需要时间，所以可以添加显示等待场景，
            # 判断文件上传成功后，页面是否跳转到文件上传成功的页面。
            # 通过EC.title_is()方法判断跳转后的页面的Title值是否符合期望，如果匹配，将继续执行后续代码
            # 如果实现了parse_file.jsp页面，且可以成功调转，可断言文件上传成功
            wait.until(EC.title_is(u"文件上传成功"))

    # 11.7.3.使用第三方工具AutoIt上传文件
    '''
    编辑操作文件上传框体的AutoIt脚本：
    1)执行“开始”->"所有程序"->AutoIt v3->SciTE->SciTE,启动AutoIt的文本编辑器
    2)在编辑器中输入脚本:
    # include <Constants.au3>
    
    Send("c:\\test.txt")    # 表示使用键盘输入"c:\test.txt"
    Send("{ENTER}")         # 表示按Enter键
    Send("{ENTER}")
    # 调用两次Enter，主要是解决OS默认的输入法是中文输入法，输入"c:\\test.txt"后，
    # 必须按一次Enter才能将输入的内容写入路径输入框中，再按一次Enter，等价于单击文件打开窗体的"打开"按钮
    3)将AutoIt脚本保存为文件名为"test.au3"的文件并存放在D盘中
    4)执行"开始"->"所有程序"->AutoIt v3->Compile script to.exe(x64),调出AutoIt脚本转换成exe文件的界面
    5)在Source路径框汇总选择保存的AutoIt脚本"test.au3"文件，Destination选择.exe单选项，在输入框中设置好生成的exe文件保存路径
    6)单击Convert按钮，把AutoIt脚本"test.au3"文件转换为"test.exe"
    '''
    def test_uploadFileByAutoIt(self):
        url = "d:\\uploadFile.html"
        self.driver.get(url)
        try:
            wait = WebDriverWait(self.driver, 10, 0.2)
            # 显示等待判断被测试页面上的上传文件按钮是否处于可被单击状态
            wait.until(EC.element_to_be_clickable((By.ID, 'file')))
        except TimeoutException, e:
            print traceback.print_exc()
        except NoSuchElementException, e:
            print traceback.print_exc()
        except Exception, e:
            print traceback.print_exc()
        else:
            # 查找页面上ID属性值为"file"的文件上传框,并单击调出选择文件上传框
            self.driver.find_element_by_id("file").click()
            # 执行test.exe文件
            os.system(("d:\\book\\test.exe"))
            # AutoIt脚本转换后的可执行文件test.exe执行速度比较慢，等待5s
            time.sleep(5)
            # 找到页面上ID属性值为"filesubmit"的文件提交按钮对象
            fileSubmitButton = self.driver.find_element_by_id("filesubmit")
            # 单击提交按钮，完成文件上传操作
            fileSubmitButton.click()
            # 因为文件上传需要时间，所以可以添加显示等待场景，
            # 判断文件上传成功后，页面是否跳转到文件上传成功的页面。
            # 通过EC.title_is()方法判断跳转后的页面的Title值是否符合期望，如果匹配，将继续执行后续代码
            # 如果实现了parse_file.jsp页面，且可以成功调转，可断言文件上传成功
            wait.until(EC.title_is(u"文件上传成功"))


    # 11.8.右键另存为下载文件
    '''
    AutoItScript文件准备
    新建一个名为loadFile.au3的AutoItScript编辑器：
    ;ControlFocus("title", "text", controlID)
    ;表示将焦点切换到标题为title窗体中的controlID上
    ;Edit1表示第一个可以编辑的实例
    ;title表示弹出的Win窗体标题，不同浏览器标题可能不一样
    ControlFocus("请输入要保存的文件名...","","Edit1")
    ;等待10秒以便Win窗口加载成功
    WinWait("[CLASS: # 32770]", "", 10)
    
    ;将焦点切换到Edit1输入框中
    ControlFocus("另存为", "", "Edit1")
    
    ;等待2秒
    Sleep(2000)
    
    ;将要下载的文件名及路径写入Edit1编辑框中
    ControlSetText("另存为", "", "Edit1", "d:\iDownload\Firefox setup 35.0b8.exe")
    
    Sleep(2000)
    
    ;单击窗体中的第一个按钮，就是保存按钮
    ControlClick("另存为", "Button1")
    保存后将该文件编译成exe文件，并存放到本地磁盘
    '''
    def test_dataPickerByRightKey(self):
        # 定义将要访问的网址
        url = "http://ftp.mozilla.org/pub/mozilla.org//firefox/releases/35.0b8/win32/zh-CN/"
        self.driver.get(url)
        self.driver.maximize_window()
        time.sleep(5)
        a = self.driver.find_element_by_link_text("Firefox Setup 35.0b8.exe")
        time.sleep(2)
        # 在找到的链接元素上模拟单击鼠标右键，以便调出选择"另存为"选项的菜单
        ActionChains(self.driver).context_click(a).perform()
        time.sleep(2)
        for i in range(4):
            # 循环按4次下箭头，将焦点切换到"另存为"选项上，不同浏览器此选项的位置可能不同
            a.send_keys(Keys.DOWN)
            keyDown("down_arrow")
            keyUp("down_arrow")
            print i
            time.sleep(2)
        time.sleep(2)
        # 当焦点切换到"另存为"选项后，模拟按回车键，调出保存下载文件路径的Win窗体
        keyDown("enter")
        keyUp("enter")
        time.sleep(3)
        # 通过执行AutoIt编写的操作弹窗的win文件保存窗体，完成文件保存路径的设置
        os.system("d:\\book\\loadFile.exe")
        time.sleep(100)

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()