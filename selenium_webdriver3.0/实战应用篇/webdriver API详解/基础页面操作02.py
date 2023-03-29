"""
@FileName：基础页面操作02.py
@Author：stone
@Time：2023/3/14 16:13
@Description：页面操作
"""
import time
import unittest

from selenium import webdriver


class MyTest(unittest.TestCase):
    url1 = "http://www.sogou.com"
    url2 = "http://www.baidu.com"

    def setUp(self) -> None:
        self.driver = webdriver.Firefox()

    # 获取页面标题
    @unittest.skip("")
    def test_getTitle(self):
        url = "http://www.baidu.com"
        self.driver.get(url)
        title = self.driver.title
        print("当前页面的title是：{}".format(title))
        self.assertEqual(title, u"百度一下，你就知道", "测试标题title属性值错误")

    # 获取页面html的源码
    @unittest.skip("")
    def test_getPageSource(self):
        url = "http://www.sogou.com"
        self.driver.get(url)
        time.sleep(3)
        pageSource = self.driver.page_source
        print(pageSource)
        self.assertEqual(u"新闻" in pageSource, "页面中未找到新闻关键字")

    # 获取当前页面的url
    @unittest.skip(" ")
    def test_getCurrentPageUrl(self):
        url = "http://www.sogou.com"
        self.driver.get(url)
        current_url = self.driver.current_url
        print(current_url)
        self.assertEqual(current_url, "https://www.sogou.com/", "当前网页非预测")

    # 获取与切换浏览器窗口的句柄
    @unittest.skip("")
    def test_operateWindowhadle(self):
        url = "http://www.baidu.com"
        self.driver.get(url)
        # 获取当前的窗口句柄
        now_handle = self.driver.current_window_handle
        print(now_handle)
        self.driver.find_element_by_id('kw').send_keys("w3cschool")
        self.driver.find_element_by_id("su").click()
        time.sleep(3)
        self.driver.find_element_by_xpath("/html/body/div[2]/div[3]/div[1]/div[3]/div[1]/div/div[1]/h3/a")
        time.sleep(5)
        all_handles = self.driver.window_handles
        print("----{}".format(all_handles[-1]))
        # 循环遍历所有的要打开的新窗口
        for handle in all_handles:
            if handle != now_handle:
                print(handle)

    # 获取页面元素的基本信息
    @unittest.skip("")
    def test_getBasicInfo(self):
        url = "http://www.baidu.com"
        self.driver.get(url)
        newelement = self.driver.find_element_by_xpath("//a[text()='新闻']")
        print(newelement.tag_name)
        print(newelement.size)

    # 获取页面元素的文本内容
    @unittest.skip("")
    def test_getWebElementTest(self):
        url = "http://www.baidu.com"
        self.driver.get(url)
        time.sleep(3)
        aElement = self.driver.find_element_by_xpath("//*[@class='mnav c-font-normal c-color-t'][1]")
        a_text = aElement.text
        self.assertEqual(a_text, u"新闻")

    # 判断页面元素是否可见
    def test_getWebElementIsDisplayed(self):
        self.driver.is_displayed()




    def tearDown(self) -> None:
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
