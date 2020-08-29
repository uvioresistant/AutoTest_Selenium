#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:fengg
@file:test_unittest.py
@time:2020/08/28
"""
import sys
import unittest
import random


class TestSequenceFunctions(unittest.TestCase):
    a = 1

    def setUp(self):
        # 初始化一个递增序列
        self.seq = list(range(10))

    @unittest.skip("skipping")  # 无条件忽略该测试方法
    def test_shuffle(self):
        # 随机打乱原seq的顺序
        random.shuffle(self.seq)
        self.seq.sort()
        self.assertEqual(self.seq, range(10))
        # 验证执行函数时抛出了TypeError异常
        self.assertRaises(TypeError, random.shuffle, (1, 2, 3))


    def tearDown(self):
        pass

    # 如果变量a>5, 则忽略该测试方法
    @unittest.skipIf(a>5, "condition is not satisfied!")
    def test_choice(self):
        # 从序列seq中随机选取一个元素
        element = random.choice(self.seq)
        # 验证随机元素确实属于列表中
        self.assertTrue(element in self.seq)

    # 除非执行测试用例的平台是Windows平台，否则忽略该测试方法
    @unittest.skipUnless(sys.platform.startswith("linux"), "requires Windows")
    def test_sample(self):
        # 验证执行的语句是否抛出了异常
        with self.assertRaises(ValueError):
            random.sample(self.seq, 20)
        for element in random.sample(self.seq, 5):
            self.assertTrue(element in self.seq)


class TestDictValueFormatFunctions(unittest.TestCase):
    def setUp(self):
        self.seq = range(10)

    def tearDown(self):
        pass

    def test_shuffle(self):
        # 随机打乱原seq的顺序
        random.shuffle(self.seq)
        self.seq.sort()
        self.assertEqual(self.seq, range(10))
        # 验证执行函数时抛出了TypeError异常
        self.assertRaises(TypeError, random.shuffle, (1, 2, 3))


# 被测试类
class myclass(object):
    @classmethod
    def sum(cls, a, b):
        # 将两个传入参数进行相加操作
        return a + b

    @classmethod
    def sub(cls, a, b):
        # 将两个传入参数进行相减操作
        return a - b


class mytest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """初始化类固件"""
        print "---setUpClass"

    @classmethod
    def tearDownClass(cls):
        """重构类固件"""
        print "---tearDownClass"

    # 初始化工作
    def setUp(self):
        self.a = 3
        self.b = 1
        print "--setUp"

    # 退出清理工作
    def tearDown(self):
        print "--tearDown"

    # 具体的测试用例，一定要以teat开头
    def testsum(self):
        # 断言两数之和的结果是否是4
        self.assertEqual(myclass.sum(self.a, self.b), 4, 'test sum fail')

    def testsub(self):
        # 断言两数之差的结果是否是2
        self.assertEqual(myclass.sub(self.a, self.b), 2, 'test sub fail')


if __name__ == "__main__":
    # 根据给定的测试类，获取其中的所有以"test"开头的测试方法，并返回一个测试套件
    testCases = unittest.TestLoader().loadTestsFromTestCase(TestSequenceFunctions)
    suite = unittest.TestSuite(testCases)
    unittest.TextTestRunner(verbosity=2).run(suite)
    # testCase1 = unittest.TestLoader().loadTestsFromTestCase(TestSequenceFunctions)
    # testCase2 = unittest.TestLoader().loadTestsFromTestCase(TestDictValueFormatFunctions)
    # 将多个测试类加载到测试套件中
    # suite = unittest.TestSuite([testCase1, testCase2])
    # 设置verbosity = 2，可以打印出更详细的执行信息
    # unittest.TextTestRunner(verbosity=2).run(suite)
    # unittest.main()