"""
@FileName：unittest_demo2.py\n
@Author：stone\n
@Time：2023/3/14 10:56\n
@Description：\n
"""
import unittest


class MyClass():

    @classmethod
    def sum(self, a, b):
        return a + b

    @classmethod
    def sub(self, a, b):
        return a - b


class mytest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # 初始化使用固件
        print("setUpClass")

    @classmethod
    def tearDownClass(cls):
        print("tearDownClass")

    # 初始化工作
    def setUp(self):
        self.a = 3
        self.b = 2
        print("setup")

    def tearDown(self):
        print("tearDown")

    def testadd(self):
        self.assertEqual(MyClass.sum(self.a, self.b), 5, "test sum fail")

    def testsub(self):
        self.assertEqual(MyClass.sub(self.a, self.b), 1, "test sub fail")


if __name__ == '__main__':
    unittest.main()
