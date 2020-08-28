#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:fengg
@file:calc.py
@time:2020/08/28
"""


class Calc(object):
    def add(self, x, y, *d):
        result = x + y
        for i in d:
            result += i
        return result

    def sub(self, x, y, *d):
        result = x - y
        for i in d:
            result -= i
        return result

    @classmethod
    def mul(self, x, y, *d):
        result = x * y
        for i in d:
            result *= i
        return result

    @classmethod
    def div(self, x, y, *d):
        if y != 0:
            result = x / y
        else:
            return -1
        for i in d:
            if i != 0:
                result /= i
            else:
                return -1
        return result


if __name__ == "__main__":
    pass
