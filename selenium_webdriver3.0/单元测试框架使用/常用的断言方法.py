"""
@FileName：常用的断言方法.py
@Author：stone
@Time：2023/3/14 13:40
@Description：常用的断言方法
"""
import random
import unittest


class MyClass():
    @classmethod
    def sum(cls, a, b):
        return a + b

    @classmethod
    def div(cls, a, b):
        return a / b

    @classmethod
    def retrun_None(cls):
        return None


class MyTest(unittest.TestCase):
    def test_assertEqual(self):
        # 断言两数之和
        try:
            a, b = 1, 2
            sum = 3
            self.assertEqual(a + b, sum, "断言失败，{} + {}!={}".format(a, b, sum))
        except AssertionError as e:
            pass

    def test_assertNotEqual(self):
        try:
            a, b = 5, 2
            res = 3
            self.assertnotEqual(a - b, res, "断言失败，{}+{}！={}".format(a, b, res))
        except AssertionError as e:
            print(e)

    def test_assertTrue(self):
        try:
            self.assertTrue(1 == 1, "表达式为假")
        except AssertionError as e:
            print(e)

    def test_assertFalse(self):
        try:
            self.assertFalse(3 == 2, "表达式为真")
        except AssertionError as e:
            print(e)

    def test_assertIs(self):
        try:
            b = 12
            a = b
            self.assertIs(a, b, "{}与{}不是同一个对象".format(a, b))
        except AssertionError as e:
            print(e)

    def test_assertIsNot(self):
        try:
            a = 12
            b = "test"
            self.assertIsNot(a, b, "{}与{}属于同一个对象".format(a, b))
        except AssertionError as e:
            print(e)

    def test_assertIsNotNone(self):
        try:
            result = MyClass.sum(2, 5)
            self.assertIsNotNone(result, "not is None")
        except AssertionError as e:
            print(e)

    def test_assertNotIn(self):
        try:
            strA = "this is a test"
            strB = "Selenium"
            self.assertNotIn(strB, strA, "{}包含在{}中".format(strB, strA))
        except AssertionError as e:
            print(e)

    def test_assertIsInstance(self):
        try:
            x = MyClass
            y = object
            self.assertIsInstance(x, y, "{}的类型不是{}".format(x, y))
        except AssertionError as e:
            print(e)

    def test_assertNotIsInstance(self):
        try:
            a = 123
            b = "str"
            self.assertNotIsInstance(a, b, "{}的类型是{}".format(a, b))
        except AssertionError as e:
            print(e)

    def test_assertRaises(self):
        # 测试指定的异常类型
        with self.assertRaises(ValueError) as cn:
            random.sample([1, 2, 3, 4, 5], "j")
        print("===", cn.exception)

        try:
            self.assertRaises(ZeroDivisionError, MyClass.div, 3, 0)
        except ZeroDivisionError as e:
            print(e)

    def test_assertRaisesRegexp(self):
        with self.assertRaisesRegexp(ValueError, "literal") as ar:
            int("xyz")
        print(ar.exception)

        try:
            self.assertRaisesRegexp(ValueError, "invalid literal for ")
        except AssertionError as e:
            print(e)


if __name__ == '__main__':
    unittest.main()
