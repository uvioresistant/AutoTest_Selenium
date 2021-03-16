#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:fengg
@file:test_user.py
@time:2020/09/10
"""
import unittest
import requests
import time as t
import os
import json
from page.user import *
from utils.helper import *


class TestUserApi(unittest.TestCase, Helper):
    @classmethod
    def setUpClass(cls):
        t.sleep(1)

    @classmethod
    def tearDownClass(cls):
        pass

    def statusCode(self, r):
        '''对HTTP状态码和业务状态码校验'''
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()['status'], 0)

    def test_user_api_001(self):
        '''登录业务:登录系统'''
        r = post(
            self.getUrl(1), self.getData(1))
        self.statusCode(r)
        self.assertEqual(r.json()['data']['name'], '666666')
        with open(self.base_dir('token'), 'w') as f:
            f.write(r.json()['data']['token'])

    @property
    def getToken(self):
        '''获取登录成功后的token'''
        with open(self.base_dir('token'), 'r') as f:
            return f.read()

    def setToken(self, rowx):
        '''对excel中的请求参数token重新赋值'''
        dict1 = self.getData(rowx)
        dict1['token'] = self.getToken
        return dict1

    def test_user_api_002(self):
        '''登录业务:查看登录成功后的用户信息'''
        r = post(self.getUrl(2), self.setToken(2))
        self.statusCode(r)
        self.assertEqual(r.json()['data']['username'], '6666')

    def test_user_api_003(self):
        '''用户管理业务：添加用户'''
        r=post(self.getUrl(3), self.setToken(3))
        self.statusCode(r)

    def test_user_api_004(self):
        '''用户管理业务：用户查询'''
        r=post(self.getUrl(4), self.setToken(4))
        self.statusCode(r)
        self.assertEqual(r.json()['data']['recods'][0]['name'], '66666')

    @property
    def getUserID(self):
        '''获取用户的ID'''
        r = post(self.getUrl(4), self.setToken(4))
        return r.json()['data']['records'][0]['id']

    def setTokenUserID(self, rowx):
        '''对excel中的请求参数token重新赋值'''
        dict1 = self.getData(rowx)
        dict1['token'] = self.getToken
        return dict1

    def test_user_api_002(self):
        '''登录业务:查看登录成功后的用户信息'''
        r = post(self.getUrl(2), self.setToken(2))
        self.statusCode(r)
        self.assertEqual(r.json()['data']['username'], '6666')

    def test_user_api_003(self):
        '''用户管理业务：添加用户'''
        r = post(self.getUrl(3), self.setToken(3))
        self.statusCode(r)

    def test_user_api_004(self):
        '''用户管理业务：用户查询'''
        r = post(self.getUrl(4), self.setToken(4))
        self.statusCode(r)
        self.assertEqual(r.json()['data']['recods'][0]['name'], '66666')

    @property
    def getUserID(self):
        '''获取用户的ID'''
        r = post(self.getUrl(4), self.setToken(4))
        return r.json()['data']['records'][0]['id']

    def setTokenUserId(self, rowx):
        '''
        对excel中的请求参数token,用户ID重新赋值
        :param rowx: 在excel中的行数
        '''
        dict1=self.getData(rowx)
        dict1['token']=self.getToken
        dict1['id']=self.getUserID
        return dict1

    def test_user_api_005(self):
        '''用户管理业务：冻结用户'''
        r = post(self.getUrl(5), self.setTokenUserID(5))
        self.statusCode(r)

    def test_user_api_006(self):
        '''用户管理业务：验证用户已冻结'''
        r = post(self.getUrl(4), self.setToken(4))
        self.statusCode(r)
        self.assertEqual(r.json()['data']['records'][0]['status'],1)

    def test_user_api_007(self):
        '''用户管理业务：激活用户'''
        r=post(self.getUrl(6), self.setToken(6))
        self.statusCode(r)
        self.assertEqual(r.json()['data']['records'][0]['status'], 0)

    def test_user_api_008(self):
        '''用户管理业务：验证用户已激活'''
        r = post(self.getUrl(4), self.setToken(4))
        self.statusCode(r)
        self.assertEqual(r.json()['data']['records'][0]['status'], 0)


    def test_user_api_009(self):
        '''用户管理业务: 删除用户'''
        r = post(self.getUrl(7), self.setTokenUserID(7))
        self.statusCode(r)

    def test_user_api_010(self):
        '''用户管理业务:验证用户已删除'''
        r = post(self.getUrl(4), self.setToken(4))
        self.statusCode(r)
        self.assertEqual(r.json()['data']['tn'], 0)


if __name__ == "__main__":
    unittest.main(verbosity=2)
