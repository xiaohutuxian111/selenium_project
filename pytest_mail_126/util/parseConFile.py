"""
@FileName：parseConFile.py
@Author：stone
@Time：2023/3/16 18:30
@Description：解析.ini文件
"""

import configparser
from config.conf import CONF_PATH


class ParseConFile(object):
    def __init__(self):
        self.file = CONF_PATH
        self.conf = configparser.ConfigParser()
        self.conf.read(self.file, encoding='utf-8')

    # 获取所有的section，返回一个列表
    def getAllSections(self):
        return self.conf.sections()

    # 获取指定的section下所有的option
    def getAllOptions(self, section):
        return self.conf.options(section)

    # 获取指定的section下指定的option
    def getLocatorsOrAccount(self, section, option):
        try:
            locator = self.conf.get(section, option)
            if ('->' in locator):
                locator = tuple(locator.split('->'))
            return locator
        except configparser.NoOptionError as e:
            print("error: ", e)
        return "error: no option '{}' in section： {}".format(option, section)

    # 获取指定的section下所有的option对应的数据，返货i字典
    def getOptionValues(self, section):
        value = dict(self.conf.items(section))
        return value



if __name__ == '__main__':
    p = ParseConFile()
    print(p.file)
    print(p.getAllSections())
    print(p.getOptionValues('126LoginAccount'))
    print(p.getLocatorsOrAccount('HomePageElements','homePage'))