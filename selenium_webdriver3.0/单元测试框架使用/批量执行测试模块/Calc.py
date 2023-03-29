"""
@FileName：Calc.py
@Author：stone
@Time：2023/3/14 13:23
@Description：
"""


class Calc():

    def add(self, x, y, *d):
        result = x + y
        for i in d:
            result += i
        return result

    def mul(self, x, y):
        return x * y
