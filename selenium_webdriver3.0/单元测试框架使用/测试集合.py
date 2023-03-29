"""
@FileName：测试集合.py
@Author：stone
@Time：2023/3/14 11:11
@Description：测试集合
"""
import random
import unittest


class TestSequenceFunctions(unittest.TestCase):
    def setUp(self):
        self.mq = list(range(10))

    def tearDown(self):
        pass

    def test_choice(self):
        element = random.choice(self.mq)
        self.assertTrue(element in self.mq)

    def test_sample(self):
        with self.assertRaises(ValueError):
            random.sample(self.mq, 20)
        for element in random.sample(self.mq, 5):
            self.assertTrue(element in self.mq)


class TestDictValueFunctions(unittest.TestCase):
    def setUp(self):
        self.seq = list(range(10))

    def tearDown(self):
        pass

    def test_shuffle(self):
        random.shuffle(self.seq)
        self.seq.sort()
        self.assertEqual(self.seq, list(range(10)))
        # 验证执行函数抛出TypeError异常
        self.assertRaises(TypeError, random.shuffle, (1, 2, 3))


if __name__ == '__main__':
    testCase1 = unittest.TestLoader().loadTestsFromTestCase(TestSequenceFunctions)
    testCase2 = unittest.TestLoader().loadTestsFromTestCase(TestDictValueFunctions)
    # 多个测试类加载到测试套件中
    suite = unittest.TestSuite(testCase1, testCase2)
    # verbosity = 2 打印出详细的执行信息
    unittest.TextTestRunner(verbosity=2).run(suite)
