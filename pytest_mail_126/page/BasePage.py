"""
@FileName：BasePage.py
@Author：stone
@Time：2023/3/19 15:21
@Description：对基础操作封装
"""
import time

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait as wb
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException, NoAlertPresentException

from util.parseExcel import ParseExcel
from util.perseConFile import ParseConFile
from util.keyBoard import KeyBoard
from util.clipboard import ClipBoard


class BasePage(object):
    cf = ParseConFile()
    excel = ParseExcel()

    def __init__(self, driver, outTime=20):
        self.byDic = {
            'id': "By.ID",
            'name': "By.NAME",
            'class_name': "css selector",
            'xpath': "xpath",
            'link_text': "link text"
        }
        self.driver = driver
        self.outTime = outTime

    def findElement(self, by, locator):
        try:
            print("info:find element  {}:{} ".format(by,locator))
            element = wb(self.driver, self.outTime).until(lambda x: x.find_element(by, locator))
        except TimeoutException as t:
            print("error:{} outtime".format(t))
        except NoSuchElementException as e:
            print("error: no element {}".format(e))
        except Exception as e:
            raise e
        else:
            return element

    def findElements(self, by, locator):
        try:
            elements = wb(self.driver, self.outTime).until(lambda x: x.find_elements(by, locator))
        except TimeoutException as t:
            print(t)
        except NoSuchElementException as e:
            print(e)
        except  Exception as e:
            raise e
        else:
            return elements

    def isElementExsit(self, by, locator):
        if by.lower() in self.byDic:
            try:
                wb(self.driver, self.outTime).until(EC.visibility_of_element_located((self.byDic[by], locator)))
            except TimeoutException as t:
                print(t)
                return False
            except NoSuchElementException as e:
                print(e)
                return False
            return True
        else:
            print("the '[} error".format(by))

    def isClick(self, by, locator):
        if by.lower() in self.byDic:
            try:
                element = wb(self.driver, self.outTime).until(EC.element_to_be_clickable((self.byDic[by], locator)))
            except Exception as e:
                return False
            return element
        else:
            print('the {} error'.format(by))

    def isAlertAndSwitchToIt(self, by, locator):
        try:
            re = wb(self.driver, self.outTime).until(EC.alert_is_present())
        except NoAlertPresentException:
            return False
        except Exception as e:
            return False
        return re

    # 判断是否存在frame，存在跳到frame
    def switchToFrame(self, by, locator):
        if by.lower() in self.byDic:
            try:
                wb(self.driver, self.outTime).until(
                    EC.frame_to_be_available_and_switch_to_it((self.byDic[by], locator)))
            except TimeoutException as t:
                print("error: found {} timeout".format(t))
            except NoSuchElementException as e:
                print("error:no such {} ".format(e))
            except Exception as e:
                raise e
        else:
            print('the {} error'.format(by))

    # 返回默认的frame
    def switchToDefaultFrame(self):
        try:
            self.driver.switch_to.default_content()
        except Exception as e:
            print(e)

    def getALertText(self):
        """
        获取alert的提示信息
        :return:
        """

        if self.isAlertAndSwitchToIt():
            alter = self.isAlertAndSwitchToIt()
            return alter.text
        else:
            return None

    def getElementText(self, by, locator, name=None):
        """
        获取某一个元素的text信息
        :param by:
        :param locator:
        :param name:
        :return:
        """

        try:
            element = self.findElement(by, locator)
            if name:
                return element.get_attribute(name)
            else:
                return element.text

        except Exception as e:
            print('get {} text failed return None'.format(e))
            return None

    def loadUrl(self, url):
        """加载url"""
        print("info:string upload url {}".format(url))
        self.driver.get(url)

    def getSourece(self):
        """获取页面源码"""
        return self.driver.page_source

    def sendKeys(self, by, locator, value=''):
        """写数据"""
        print("info:input {}".format(value))
        try:
            element = self.findElement(by, locator)
            element.send_keys(value)
        except AssertionError as e:
            print(e)

    def clear(self, by, locator):
        """清理数据"""
        print('info:clearing value')
        try:
            element = self.findElement(by, locator)
            element.clear()
        except AssertionError as e:
            print(e)

    def click(self, by, locator):
        """点击某个元素"""
        print("info: click {}".format(locator))
        element = self.isClick(by, locator)
        if element:
            element.click()
        else:
            print("error:{}".format("unclickable"))

    def sleep(self, num):
        """强制等待"""
        print("info:sleep {} minutes".format(num))
        time.sleep(num)

    def ctrlV(self, value):
        """ctrl + V """
        print("info:pasting {}".format(value))
        ClipBoard.setText(value)
        self.sleep(3)
        KeyBoard.twoKeys('ctrl', 'v')

    def enterKey(self):
        """回车键"""
        print("info:keydown enter")
        KeyBoard.oneKey('enter')

    def waitElementtobelocated(self, by, locator):
        """显示等待某个元素出现，且可见"""
        print("info:waiting {} to be located".format(locator))
        try:
            wb(self.driver, self.outTime).until(EC.visibility_of_element_located(self.byDic[by]), locator)
        except  TimeoutException as t:
            print('error:found {} timeout'.format(locator))
        except NoSuchElementException as e:
            print("error:no such  {} ".format(locator), e)
        except Exception as e:
            raise e

    def assertValueInSource(self, value):
        """断言某个关键子是否存在页面源码中"""
        print("info:assert {}  in page  source".format(value))
        source = self.getSourece()
        assert value in source, "关键字 {} 不在源码中".format(value)

    def assertStringContainsValue(self, String, value):
        """断言某个字符串是否包含在另外一个字符串中"""
        print("info:assert {} contains".format(String, value))
        assert value in String, "{} 不包含 {}".format(String, value)

    @staticmethod
    def getSheet(sheetName):
        """获取某个sheet页的对象"""
        sheet = BasePage.excel.getSheetByName(sheetName)
        return sheet


if __name__ == '__main__':
    driver = webdriver.Firefox()
    frame = ('xpath', '//*[@id="loginDiv"]//iframe[0]')
    wait = BasePage(driver)
    driver.get('https://mail.126.com/')
    wait.switchToFrame(*frame)
    username = wait.findElement('xpath', '//*[@id="login-form"]/div[1]/div[1]/div[2]/input')
    username.send_keys('23982310@126.com')
    if wait.isElementExsit('xpath', '//*[@id="login-form"]//div[1]//div[3]//div[2]'):
        wait.findElement("xpath", '//*[@id="login-form"]//div[1]//div[3]//div[2]')
    wait.click('xpath', '//*[@id="dologin"]').send_keys("12112asdsacdzcxz@")


