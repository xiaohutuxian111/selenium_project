"""
unittest 框架的使用
    test fixture（测试组件）
    test case（测试用例）
    test suite （测试套件）
    test runner （测试运行器）
"""

import unittest
import random


class TestSequenceFunctions(unittest.TestCase):

    def setUp(self):
        self.meq = list(range(10))

    def runTest(self):
        element = random.choice(self.meq)
        self.assertTrue(element in self.meq)


class TestDictValueFormatFunctions(unittest.TestCase):
    def setUp(self):
        self.meq = list(range(10))

    def test_shuffle(self):
        random.shuffle(self.meq)
        self.meq.sort()
        self.assertEqual(self.meq, list(range(10)))
        self.assertRaises(TypeError, random.shuffle, (1, 2, 3))


if __name__ == '__main__':
    unittest.main()
