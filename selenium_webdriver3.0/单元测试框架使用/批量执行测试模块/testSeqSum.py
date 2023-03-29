"""
@FileName：testSeqSum.py
@Author：stone
@Time：2023/3/14 13:34
@Description：测试模块
"""
import unittest


class MyTestCase(unittest.TestCase):
    def testEqual(self):
        seq = list(range(11))
        self.assertEqual(sum(seq),55,"断言列表元素和结果")



