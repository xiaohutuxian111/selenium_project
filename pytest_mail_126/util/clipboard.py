"""
@FileName：clipboard.py
@Author：stone
@Time：2023/3/16 16:51
@Description：剪切板工具类
"""

import win32con
import win32clipboard as WC


class ClipBoard(object):

    @staticmethod
    def getText():
        """
        获取剪切版内容
        :return:
        """
        WC.OpenClipboard()
        value = WC.GetClipboardData(win32con.CF_TEXT)
        WC.CloseClipboard()
        return value

    @staticmethod
    def setText(value):
        # 设置剪切板的内容
        WC.OpenClipboard()
        WC.EmptyClipboard()
        WC.SetClipboardData(win32con.CF_UNICODETEXT, value)
        WC.CloseClipboard()


if __name__ == '__main__':
    from selenium import webdriver
    value = 'python'
    driver = webdriver.Firefox()
    driver.get("https://www.baidu.com")
    query = driver.find_element_by_id("kw")
    ClipBoard.setText(value)
    cVlaue = ClipBoard.getText()
    query.send_keys(cVlaue.decode("utf-8"))
