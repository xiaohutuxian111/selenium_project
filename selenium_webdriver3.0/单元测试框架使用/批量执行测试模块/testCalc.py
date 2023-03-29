"""
@FileName：testCalc.py
@Author：stone
@Time：2023/3/14 13:25
@Description：测试模块
"""
import unittest

from Calc import Calc


class MyTest(unittest.TestCase):
    c = None

    @classmethod
    def setUpClass(cls) -> None:
        print("单元测试，创建Calc类的实例")
        cls.c = Calc()

    def test_add(self):
        print("执行测试 add")
        self.assertEqual(MyTest.c.add(1, 2, 3), 15, "test add fail")
