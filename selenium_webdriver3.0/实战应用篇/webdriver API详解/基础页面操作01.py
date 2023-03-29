"""
@FileName：基础页面操作01.py
@Author：stone
@Time：2023/3/14 15:30
@Description：
"""
import time
import unittest

from selenium import webdriver


class MyTest(unittest.TestCase):

    def setUp(self) -> None:
        self.webdriver = webdriver.Firefox()

    # 访问某个网址
    @unittest.skip("")
    def test_VisitURL(self):
        visitURl = "http://www.sogou.com"
        self.webdriver.get(visitURl)
        time.sleep(3)
        assert self.webdriver.title.find(u"搜狗搜索引擎") >= 0, "assert error"

        # 网页的前进和后退

    @unittest.skip("")
    def test_visitRecentURL(self):
        firstVisitURL = "http://www.sogou.com"
        lastVisitURL = "http://www.baidu.com"

        self.webdriver.get(firstVisitURL)
        time.sleep(3)
        self.webdriver.get(lastVisitURL)
        # 返回上一次访问的网页
        self.webdriver.back()
        # 再次回到搜狗首页
        self.webdriver.forward()

    # 刷新当前网页
    @unittest.skip("")
    def test_refreshCurrentPage(self):
        url = "http://www.sogou.com"
        self.webdriver.get(url)
        time.sleep(3)
        self.webdriver.refresh()

    # 浏览器最大化
    @unittest.skip("")
    def test_maxinizeWindow(self):
        url = "http://www.sogou.com"
        self.webdriver.get(url)
        self.webdriver.maximize_window()

    # 获取并设置当前窗口的位置
    @unittest.skip("")
    def test_window_position(self):
        url = "http://www.sogou.com"
        self.webdriver.get(url)
        position = self.webdriver.get_window_position()
        print("当前浏览器所在位置的横坐标", position['x'])
        print("当前浏览器所在位置的横坐标", position['y'])
        self.webdriver.set_window_position(y=200, x=400)
        print(self.webdriver.get_window_position())

    # 获取并设置当前窗口的大小
    def test_window_size(self):
        url = "http://www.sogou.com"
        self.webdriver.get(url)
        sizeDict = self.webdriver.get_window_size()
        print("当前浏览器窗口的大小：", sizeDict["width"])
        print("当前浏览器窗口的大小：", sizeDict["height"])
        self.webdriver.set_window_size(120, 400,windowHandle='current')
        time.sleep(3)

        # 设置窗口大小后再次查看窗口大小
        print(self.webdriver.get_window_size(windowHandle="current"))

    def tearDown(self) -> None:
        self.webdriver.quit()



if __name__ == '__main__':
    unittest.main()
