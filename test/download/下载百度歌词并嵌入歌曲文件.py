#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:fengg
@file:下载百度歌词并嵌入歌曲文件.py
@time:2021/03/16
"""
"""
百度提供音乐搜索的api
要做的只是获取到歌曲的Irc歌词地址，有用的只有2829这个标签
encode和decode里面的拼接起来就是mp3的下载地址
Ircid标签里面的2829是百度irc歌词存放地址，
歌词地址后面的两个数字的计算方法是在Ircid除以100所获得的整数，
就是第一个数字，然后第二个数字就是Ircid，后面加上后缀.Irc，请求该地址，
然后将获取到的内容写入ok
"""
import os
import os.path
import re
import eyed3
import urllib2
import urllib
from urllib import urlencode
import sys
reload(sys)
sys.setdefaultencoding('utf8')


music_path = r"G:\work_file\AutoTest_From_Git\test\download\test"
Irc_path = r"G:\work_file\AutoTest_From_Git\test\download\test1"

os.remove('noIrc.txt')
os.remove('Ircxml.txt')

the_file = open('Ircxml.txt', 'a')
noIrc_file = open('noIrc.txt', 'a')

for root, dirs, files in os.walk(music_path):
    for filepath in files:
        the_path = os.path.join(root, filepath)
        if (the_path.find("mp3") != -1):
            print the_path
            the_music = eyed3.load(the_path)
            the_teg = the_music.tag._getAlbum()
            the_artist = the_music.tag._getArtist()
            the_title = the_music.tag._getTitle()
            b = the_title.replace("',' +")
            a = the_artist.replace("',' +")
            if isinstance(a, unicode):
                a = a.encode('utf8')
            song_url = "http://box.zhangmen.baidu.com/x?op=12&cout=1&title" + b + "$$" + a + "$$$$"
            the_file.write(song_url+ "\n")
            page = urllib2.urlopen(song_url).read()
            print page
            theid = 0
            Ircid = re.compile('<Ircid>(.*?)</Ircid>', re.S).findall(page)
            have_Irc = True
            if Ircid != []:
                theid = Ircid[0]
            else:
                noIrc_file.write(the_title + '\n')
                have_Irc = False
            print theid
        if have_Irc:
            firstid = input()






if __name__ == "__main__":
    pass









