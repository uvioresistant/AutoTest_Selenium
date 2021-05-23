#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:fengg
@file:test.py
@time:2021/03/10
"""
import struct


def float_to_bits(f):
    s = struct.pack(">f", f)
    return struct.unpack(">l", s)

# print(2 + 3.19)
# 5.1899999999999995
# print(2 + 3.29)
# 5.29


if __name__ == "__main__":
    print(float_to_bits(2)[0], 121212121)
    print(bin(float_to_bits(2)[0]), 121212121)

    print(float_to_bits(3.29)[0], 111111111)
    print(bin(float_to_bits(3.29)[0]), 111111111)

    print(float_to_bits(3.29 + 2)[0], 4444444444444)
    print(bin(float_to_bits(3.29 + 2)[0]), 4444444444444)

    print(float_to_bits(3.19)[0], 222222222222222)
    print(bin(float_to_bits(3.19)[0]), 222222222222222)
    print(float_to_bits(3.69)[0], 3333333333)
    print(bin(float_to_bits(3.69)[0]), 3333333333333)