"""
@FileName：使用HTMLTestRunner生成HTML测试报告.py
@Author：stone
@Time：2023/3/14 14:30
@Description：生成HTML测试报告
"""
import math
import unittest


class Calc(object):

    def add(self, x, y, *d):
        result = x + y
        for i in d:
            result += i
        return result


    def sub(self, x, y, *d):
        result = x - y
        for i in d:
            result -= i
        return result




class SuiteTestCalc(unittest.TestSuite):
    def  setUp(self):
        self.c = Calc()

    def test_Sub(self):
        print("sub")
        self.assertEqual(self.c.sub(100,34,6),60,"求差结果错误")

    def test_add(self):
        print("add")
        self.assertEqual(self.c.add(1,32,56),89,"求和结果错误")


class SuiteTestPow(unittest.TestCase):
    def setUp(self) -> None:
        self.seq = list(range(10))

    def test_Pow(self):
        print("pow")
        self.assertEqual(pow(6,3),216,"求幂的结果错误")

    def test_hasattr(self):
        print(hasattr)
        self.assertTrue(hasattr(math,'pow'),"检测属性不存在")



if __name__ == '__main__':
    suite1 = unittest.TestLoader().loadTestsFromTestCase(SuiteTestPow)
    suite2 = unittest.TestLoader().loadTestsFromTestCase(SuiteTestCalc)
    suite = unittest.TestSuite(suite1,suite2)
    filename = "./test.html"
    fp = open(filename,"wb")
    # runner = HTMLTestRunner.HTMlTestRunner(stream = fp,title="Report tille",description = "Report_description")
    # runner.run(suite)




