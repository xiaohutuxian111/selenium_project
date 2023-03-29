class Calc():

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

    @classmethod
    def mul(cls, x, y, *d):
        result = x * y
        for i in d:
            result *= i
        return result

    @staticmethod
    def div(x, y, *d):
        if y != 0:
            result = x / y
        else:
            return -1
        for i in d:
            if d != 0:
                result /= i
            else:
                return -1
        return result
