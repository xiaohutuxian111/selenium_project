"""
@FileName：testFact.py
@Author：stone
@Time：2023/3/14 13:30
@Description：测试模块
"""
import unittest
from functools import reduce


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.num = 5

    def testFactorial(self):
        seq = range(1, self.num + 1)
        res = reduce(lambda x, y: x + y, seq)
        # 断言阶乘结果
        self.assertEqual(res, 120, "阶乘断言结果错误")
