"""
@FileName：忽略某个测试方法.py
@Author：stone
@Time：2023/3/14 13:09
@Description：忽略某个测试方法
"""
import random
import sys
import unittest


class TestSequenceFunctions(unittest.TestCase):
    a = 1

    def setUp(self) -> None:
        self.seq = list(range(10))

    @unittest.skip("无条件跳过此方法")
    def test_shuffle(self):
        print("test_shuffle")
        random.shuffle(self.seq)
        self.seq.sort()
        self.assertEqual(self.seq, list(range(10)))
        self.assertRaises(TypeError, random.shuffle, (1, 2, 3))

    @unittest.skipIf(a > 5, "conditions is not satisfied")
    def test_choice(self):
        print("test_choice")
        element = random.choice(self.seq)
        self.assertTrue(element in self.seq)

    @unittest.skipUnless(sys.platform.startswith("linux"), "requires window")
    def test_sample(self):
        print("test_sample")
        with  self.assertRaises(ValueError):
            random.sample(self.seq, 20)
        for element in random.sample(self.seq, 5):
            self.assertTrue(element in self.seq)


if __name__ == '__main__':
    testCase = unittest.TestLoader().loadTestsFromTestCase(TestSequenceFunctions)
    suite = unittest.TestSuite(testCase)
    unittest.TextTestRunner(verbosity=2).run(suite)
