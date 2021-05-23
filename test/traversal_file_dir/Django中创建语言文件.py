#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:fengg
@file:Django中创建语言文件.py
@time:2021/03/03
"""
'''
如果应用需要支持一个Django中没有的地域，至少需要做一个Django core的最小翻译
消息文件：
第一步:为一种语言创建一个信息文件。信息文件是包含了某一语言翻译字符串和这些字符串的翻译的一个文本文件
信息文件以.po为后缀名
Django中带有一个工具，bin/make-messages.py，完成了这些文件的创建和维护工作运行以下命令来创建或更新一个信息文件:
django-admin.py makemessages -l de
其中de是所创建的信息文件的语言代码，以本地格式给出的，这段脚本应在三处之一运行：
* Django项目根目录
* Django应用的根目录
* django根目录，通过$PYTHONPATH链接/位于该路径的某处

# 这段脚本遍历项目源树/应用程序源树，且提取出所有为翻译而被标记的字符串。在locale/LANG/LC_MESSAGES目录下创建了一个信息文件django.po
django-admin.py makemessages检测每一个有.html扩展名的文件，重载缺省值，使用--extension/-e 指定文件扩展名来检测,用逗号或-e来分隔多项扩展名
django-admin.py makemessages -l de -e html, txt -e xml
当创建JS翻译目录时，需要使用特殊的Django域：not -e js

# 如果没安装gettext组件，make-messages.py将会创建空白文件，安装gettext组件/只是复制英语信息文件来作为一个起点，只是一个空白文件

# Win下，需安装GNU gettext共用程序，以便django-admin makemessages可以工作

# 每个.po文件包含一小部分的元数据，如翻译维护人员的联系信息，而文件的大部分内容是简单的翻译字符串和对应语言翻译结果的映射关系的列表


'''


if __name__ == "__main__":
    pass