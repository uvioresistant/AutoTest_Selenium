#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:fengg
@file:test_OOP.py
@time:2020/09/27
"""


class C2(object):
    print 'C2'


class C3(object):
    print 'C3'


class C1(C2, C3):
    def __init__(self, who):
        self.name = who


    # def setname(self, who):
    #     self.name = who

class Person:
    def getName(self):
        if not valid():
            raise TypeError('cannot fetch name')
        else:
            return self.getName().transform()

        def setName(self, value):
            if not valid(value):
                raise TypeError('cannot change name')
            else:
                self.name = transform(value)

person = Person()
person.getName()
person.setName('value')


class Reader:
    def read(self):
        pass
    def other(self):
        pass


class FileReader(Reader):
    def read(self):
        pass


class SocketReader(Reader):
    def read(self):
        pass

def processor(reader, converter, writer):
    while True:
        data = reader.read()
        if not data: break
        data = converter(data)
        writer.write(data)


processor(FileReader(...), Converter, FileWriter(...))



I1 = C1('bob')
I2 = C1('mel')
print(I1.name)
# I1.setname('bob')
# I2.setname('sue1')










if __name__ == "__main__":
    pass
