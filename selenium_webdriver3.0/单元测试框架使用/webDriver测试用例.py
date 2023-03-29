"""
@FileName：webDriver测试用例.py
@Author：stone
@Time：2023/3/14 15:03
@Description：
"""
import time
import unittest

from selenium import webdriver


class GloryRoad(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = webdriver.Firefox()

    def test_sogou(self):
        self.driver.get("http://sogou.com")
        self.driver.find_element_by_id("query").clear()
        self.driver.find_element_by_id("query").send_keys("webDriver实战演练")
        self.driver.find_element_by_id("stb").click()
        time.sleep(3)
        assert u"吴晓华" in self.driver.page_source, "页面元素不存在"

    def tearDown(self) -> None:
        self.driver.quit()
