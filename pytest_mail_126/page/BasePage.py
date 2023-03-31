"""
@FileName：BasePage.py
@Author：stone
@Time：2023/3/30 18:32
@Description:封装一些基本方法
"""
import time

from selenium.webdriver.support.wait import WebDriverWait as WD
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.common.exceptions import (TimeoutException, NoAlertPresentException)

from util.clipboard import ClipBoard
from util.keyBoard import KeyBoard
from util.parseExcel import ParseExcel
from util.perseConFile import ParseConFile


class BasePage(object):
    """结合显示等待封装一些selenium的方法"""
    cf = ParseConFile()
    excel = ParseExcel()

    def __init__(self, driver, timeout=30):
        self.byDic = {
            'id': By.ID,
            'name': By.NAME,
            'class_name': By.CLASS_NAME,
            'xpath': By.XPATH,
            'like_text': By.LINK_TEXT
        }
        self.driver = driver
        self.outTime = 30

    def find_element(self, by, locator):
        """识别元素"""
        try:
            print('[Info:Starting find the element {} by {}]'.format(locator, by))
            element = WD(self.driver, self.outTime).until(lambda x: x.find_element(by, locator))
        except TimeoutException as t:
            print('error:found {} timeout'.format(locator), t)
        else:
            return element

    def find_elements(self, by, locator):
        """发现多个元素"""
        try:
            print("info:start  find  the elements {} by {}".format(locator, by))
            elements = WD(self.driver, self.outTime).until(lambda x: x.find_elements(by, locator))
        except TimeoutException as t:
            print("error: found {} timeout!".format(locator), t)
        else:
            return elements

    def is_element_exist(self, by, locator):
        """判断一个元素是否存在"""
        if by.lower() in self.byDic:
            try:
                WD(self.driver, self.outTime).until(ec.visibility_of_element_located(self.byDic[by], locator))
            except TimeoutException as t:
                print("error:elemnt {} not exist".format(locator))
                return False
            return True
        else:
            print("the {} error".format(by))

    def is_click(self, by, locator):
        if by.lower() in self.byDic:
            try:
                element = WD(self.driver, self.outTime).until(ec.element_to_be_clickable(self.byDic[by], locator))
            except TimeoutException as t:
                print("元素不可点击")
            else:
                return element
        else:
            print("the {} error".format(by))

    def is_alert(self):
        """判断是否是弹窗"""
        try:
            re = WD(self.driver, self.outTime).until(ec.alert_is_present())
        except(TimeoutException, NoAlertPresentException):
            print("error:no found  alert")
        else:
            return re

    def switch_to_frame(self, by, locator):
        """判断是否存在frame,存在就跳到frame"""
        print("info:switching to  iframe {}".format(locator))
        if by.lower() in self.byDic:
            try:
                WD(self.driver, self.outTime).until(ec.frame_to_be_available_and_switch_to_it(self.byDic[by], locator))
            except TimeoutException as t:
                print("error: found {} timeout,切换frame失败".format(locator))
        else:
            print("the {} error".format(by))

    def switch_to_default_frame(self):
        """返回默认的frame"""
        print("info:switch back to default frame")
        try:
            self.driver.switch_to.default_content()
        except Exception as e:
            print(e)

    def get_alert_text(self):
        """获取alter的提示信息"""
        alter = self.is_alert()
        if alter:
            return alter.text
        else:
            return None

    def get_element_text(self, by, locator, name=None):
        """获取某个元素的text内容"""
        try:
            element = self.find_element(by, locator)
            if name:
                return element.get_attribute(name)
            else:
                return element.text
        except AssertionError:
            print('get {} text faild return None'.format(locator))

    def load_url(self, url):
        """加载url"""
        print("info:加载{}".format(url))
        self.driver.get(url)

    def get_source(self):
        """获取页面源码"""
        return self.driver.page_source

    def send_keys(self, by, locator, value=''):
        """写数据"""
        print("info:input {}".format(value))
        try:
            element = self.find_element(by, locator)
            element.send_keys(value)
        except AttributeError as e:
            print(e)

    def clear(self, by, locator):
        """清理数据"""
        print("info:claering value")
        try:
            element = self.find_element(by, locator)
            element.clear()
        except AttributeError as e:
            print(e)

    def click(self, by, locator):
        """点击某个元素"""
        print("info:click {} ".format(locator))
        element = self.is_click(by, locator)
        if element:
            element.clic()
        else:
            print("the {}  unclickable")

    @staticmethod
    def sleep(num=0):
        """强制等待"""
        print("info:sleep {} minutes".format(num))
        time.sleep(num)

    def ctrl_v(self, value):
        """ctrl +v 粘贴"""
        print("info:passing {} ".format(value))
        ClipBoard.setText(value)
        self.sleep(3)
        KeyBoard.twoKeys('ctrl', 'v')

    @staticmethod
    def enter_key(self):
        """enter 回车键"""
        print("info :keydown enter")
        KeyBoard.oneKey('enter')

    def wait_element_to_be_located(self, by, locator):
        """显示等待某个元素出现，且可见"""
        print("info:waiting {} to be located".format(locator))
        try:
            return WD(self.driver, self.outTime).until(ec.presence_of_element_located)
        except TimeoutException as t:
            print("error:foound {} timeout ".format(locator), t)

    def get_page_source(self):
        return self.get_source()


if __name__ == '__main__':
    pass
