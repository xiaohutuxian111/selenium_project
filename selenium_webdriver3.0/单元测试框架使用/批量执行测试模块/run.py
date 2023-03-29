"""
@FileName：run.py
@Author：stone
@Time：2023/3/14 13:37
@Description：
"""
import unittest

if __name__ == '__main__':
    testcase = unittest.TestLoader().discover('.')
    unittest.TextTestRunner(verbosity=2).run(testcase)
