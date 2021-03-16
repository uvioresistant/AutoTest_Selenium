#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:fengg
@file:user.py
@time:2020/09/08
"""
import requests


def getHeaders():
    '''返回请求头'''
    headers = {
        'Content-Type': 'application/json; charset=UTF-8',
        'Parkingwang-Client-Source': 'ParkingWangAPIClientWeb'
    }
    return headers


def post(url, data):
    '''
    对post请求二次封装
    :param url: 请求地址
    :param data: 请求参数
    :return:
    '''
    r = requests.post(
        url=url,
        json=data,
        headers=getHeaders(),
        timeout=6
    )
    return r


if __name__ == "__main__":
    pass
