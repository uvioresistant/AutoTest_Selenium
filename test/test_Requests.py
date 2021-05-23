#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:fengg
@file:test_Requests.py
@time:2020/09/07
"""
import shutil
import unittest
import requests
import json
import urllib3

urllib3.disable_warnings()

# def getHeaders():
#     headers = {
#         'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
#         'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'
#     }
#     return headers
#
# dict1 = {'phone': '8613412341234', 'password': 'asdfghjkl', ' oneMonth': 1}
#
#
# def chouTi():
#     r=requests.post(
#         url='https://dig/chouti.com/login',
#         data=dict1,
#         headers=getHeaders(),
#         verify=False
#     )
#     print json.dumps(r.json(), indent=True)


# def getHeaders():
#     headers = {
#         'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
#         'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'
#     }
#     return headers
#
# dict1 = {'source': 'common', 'password': ''}
#
#
# def login():
#     r = requests.post(
#         url='https://118.111.111.145:9999/v5/login',
#         # data=json.dumps(dict1),
#         json=dict1,
#         headers=getHeaders(),
#         # verify=False
#     )
#     print json.dumps(r.json(), indent=True, ensure_ascii=False)


# r = requests.get("https://cart.taobao.com/trail_mini_cart.htm",
#                  params={'callback': 'MiniCart.setData', 't': '1526048972328'},
#                  headers={
#                      'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
#                      'Content-Type': 'application/json',
#                      'Referer': 'https://hao123.com'
#                  })
#
# print '返回的响应数据内容: \n{0}'.format(r.text)
#
# print '请求的URL为: \n{0}'.format(r.url)
#
# print 'HTTP协议返回的状态码: \n{0}'.format(r.status_code)
# print '返回的Headers信息: \n{0}'.format(r.headers)
# print '返回的cookies信息为: \n{0}'.format(r.cookies)

# def getHeaders():
#     headers = {
#         'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
#         'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'
#     }
#     return headers
#
#
# dict1 = {'username': '666666', 'source': 'common', 'password': '823dssa183f2812312d121...'}
#
#
# def getUrl():
#     return 'https://118.111.111.145:9999'
#
#
# def login():
#     r = requests.post(
#         url=getUrl() + '/v5/login',
#         # data=json.dumps(dict1),
#         json=dict1,
#         headers=getHeaders(),
#         # verify=False
#     )
#     return r.json()['data']['token']
#
# def infoGet():
#     r = requests.post(
#         url=getUrl() + '/v5/infoGet',
#         json={'token': login()},
#         headers=getHeaders(),
#     )
#     return r.json()['data']['token']
#
#
# def loginData():
#     dict1 = {"username": "66666", "souce":"common", "password": "823dssa183f2812312d121..."}
#     return dict1
#
#
# class Api(unittest.TestCase):
#     def statusCode(self, r):
#         self.assertEqual(r.json()['status'], 0)
#         self.assertEqual(r.status_code, 200)
#
#     def test_api_001(self):
#         '''登录系统'''
#         r=requests.post(
#             url=getUrl()+'/v5/login',
#             json=loginData(), headers=getHeaders()
#         )
#         with open('token', 'w') as f:
#             f.write(r.json()['data']['token'])
#
#
#     def getToken(self):
#         '''读取token文件内容'''
#         with open('token', 'r') as f:
#             return f.read()
#
#     def test_api_002(self):
#         '''获取用户信息'''
#         r = requests.post(
#             url=getUrl()+'v5/infoGet',
#             json={'token':self.getToken()},
#             headers=getHeaders()
#         )
#         self.statusCode(r=r)
from requests.auth import HTTPBasicAuth

r = requests.get(
    url='http://localhost:5000/hotel/username/',
    # 鉴权的处理
    auth=HTTPBasicAuth('wuya', 'admin')
)
print r.text

r = requests.get(
    url='http://www.baicu.com/',
    timeout=0.01
)
print r.text


def login():
    s = requests.Session()
    r = s.post(
        url='https://www.epwk.com/index.php?do=login',
        data=getData(),
        headers=getHeaders()
    )
    return s


def employer():
    r = requests.post(
        url='http://i.epwk.com/home/employer/index.html',
        data={'model': 'xsrw', 'status': 'all'},
        headers=getHeaders(),
    )
    print r.text


def getUrl():
    return 'https://118.111.111.145:9999'


def infoGet():
    r = requests.post(
        url=getUrl() + '/v5/infoGet',
        json={'token': login()},
        headers=getHeaders(),
    )
    return r.json()['data']['token']


def loginData():
    dict1 = {"username": "66666", "souce": "common", "password": "823dssa183f2812312d121..."}
    return dict1


class Api(unittest.TestCase):
    def statusCode(self, r):
        self.assertEqual(r.json()['status'], 0)
        self.assertEqual(r.status_code, 200)

    def test_api_001(self):
        '''登录系统'''
        r = requests.post(
            url=getUrl() + '/v5/login',
            json=loginData(), headers=getHeaders()
        )
        with open('token', 'w') as f:
            f.write(r.json()['data']['token'])

    def getToken(self):
        '''读取token文件内容'''
        with open('token', 'r') as f:
            return f.read()

    def test_api_002(self):
        '''获取用户信息'''
        r = requests.post(
            url=getUrl() + 'v5/infoGet',
            json={'token': self.getToken()},
            headers=getHeaders()
        )
        self.statusCode(r=r)


def getData():
    dict1 = {'formhash': 'b4ba6e', 'txt_account': '13484545195', 'pwd_password': '60e52c87966078c0b3fab7debb0fc892',
             'login_type': 3, 'ckb_cookie': 0, 'hdn_refer': 'http://www.epwk.com/',
             'txt_code': '', 'pre': 'login', 'inajax': 1}
    return dict1


class SessionTest(unittest.TestCase):
    def s(self):
        '''实例化Session的对象'''
        return requests.Session()

    def test_login(self):
        '''登录到威客'''
        r = self.s().post(
            url='https://www.epwk.com/index.php?do=login',
            data=getData(),
            headers=getHeaders()
        )
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()['status'], 1)
        self.assertEqual(r.json()['data']['mobile'], '1341115195')

    def test_task(self):
        '''我的发布任务'''
        r = self.s().post(
            url='http://i.epwk.com/home/employer/index.html',
            data={'model': 'xsrw', 'status': 'all'},
            headers=getHeaders()
        )
        self.assertEqual(r.status_code, 200)


def getHeaders():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
        'Content-Type': 'application/json; charset=UTF-8',
        'Parkingwang-Client-Source': 'ParkingWangAPIClientWeb'
    }
    return headers


def login():
    dict1 = {"username": "66666", "souce": "common", "password": "823dssa183f2812312d121..."}
    return dict1
    r = requests.post(
        url='https://118.111.111.145:9999/v5/login',
        json=dict1,
        headers=getHeaders()
    )
    return r.json()['data']['token']


def download(filepath):
    r = requests.get(
        url='https://118.111.111.145:9999/v4/download?per_page=10&shop_id=&mode=&status=&type=&ex_type=&vp1=&page=1&stime=&etime=&token={0}&down=issue'.format(
            login()),
        headers={'Content-Type': 'application/vnd.ms-excel; charset=utf8'}
    )
    # 判断是否请求成功,如果请求成功,把数据写入到指定的excel文件中
    if r.status_code == 200:
        # 二进制的方式把数据写入到文件中
        with open(filepath, 'wb') as f:
            r.raw.decode_content = True
            shutil.copyfileobj(r.raw, f)
    return '下载文件成功'


def loginData():
    '''登录请求参数'''
    data = {
        'email': '13411115195',
        'icode': '',
        'origURL': 'http://www.renren.com/home',
        'domain': 'renren.com',
        'key_id': 1,
        'captcha_type': 'web_login',
        'password': '8d9a71152914141jfsdfwer23ct1d134',
        'rkey': 'b4cdc5accld36171e3de73dd4676208e',
        'f': 'http%3A%2F%2Fname.renren.com%2F'
    }
    return data

def login():
    r = requests.post(
        url='http://www.renren.com/ajaxLogin/login?1=1&uniqueTimestamp=201894216799',
        data=loginData(),
        headers={'Content-Type': 'application/x-www-form-urlencoded'}
    )
    return r.cookies

def uploadData():
    '''上传文件请求参数'''
    data = {
        "upload": "提交",
        "__channel": "renren",
        "privacyParams": '{"sourceControl": 99}',
        'hostid': '967004081',
        'requestToken': '-1124080368',
        '_rtk': '88c0e36a'
    }
    return data

def upload():
    '''上传文件方法'''
    r = requests.post(
        url='http://upload.renren.com/upload.fcgi?pagetype=addpublishersingle&hostid=967004081&'
        'callback=window.parent.handlePhotoData&uploadid=profile_publisher_photo_1540215890321',
        data=uploadData(),
        headers={'Conteny-Type': 'multipart/form-data'},
        files={"file": {"wx.jpg", open("c:/wx.jpg", "wb"), "image/jpeg", {}}},
        cookies=login()
    )
    print r.status_code
    print r.text


if __name__ == "__main__":
    upload()
    # download('c:/xuya.xlsx')
    # unittest.main(verbosity=2)
    # employer()
    # infoGet()
    # login()
    # chouTi()
