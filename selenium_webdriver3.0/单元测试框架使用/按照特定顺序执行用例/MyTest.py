"""
@FileName：MyTest.py
@Author：stone
@Time：2023/3/14 11:41
@Description：特定顺序执行用例
"""
import unittest
from Calc import Calc


class MyTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.c = Calc()

    def test_add(self):
        print("run add")
        self.assertEqual(MyTest.c.add(1, 2, 12), 15, "test add fail")

    def test_sub(self):
        print("run sub")
        self.assertEqual(MyTest.c.sub(2, 1, 3), -2, "test sub fail")

    def test_mul(self):
        print("run mul")
        self.assertEqual(MyTest.c.mul(2, 3, 5), 30, "test mul fail")

    def test_div(self):
        print("run div")
        self.assertEqual(Calc.div(8, 2, 4), 1, "test div fail")


if __name__ == '__main__':
    # unittest.main()
    suite = unittest.TestSuite()
    suite.addTest(MyTest("test_mul"))
    suite.addTest(MyTest("test_div"))
    suite.addTest(MyTest("test_sub"))
    suite.addTest(MyTest("test_add"))
    runner = unittest.TextTestRunner()
    runner.run(suite)
