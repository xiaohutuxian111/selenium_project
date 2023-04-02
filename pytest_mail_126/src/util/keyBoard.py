"""
@FileName：keyBoard.py
@Author：stone
@Time：2023/3/16 17:12
@Description：模拟键盘操作
"""
import time

import win32api


class KeyBoard():
    # 模拟键盘
    vk_code = {
        'enter': 0x0D,
        'tab': 0x09,
        'ctrl': 0x11,
        'v': 0x56,
        'a': 0x41,
        'x': 0x58
    }

    # 按下键
    def keyDown(key_name):
        key_name = key_name.lower()
        try:
            win32api.keybd_event(KeyBoard.vk_code[key_name], 0, 0, 0)
        except Exception as e:
            print("未按下enter键")
            print(e)

    @staticmethod
    def keyUp(key_name):
        key_name = key_name.lower()
        win32api.keybd_event(KeyBoard.vk_code[key_name], 0, 0, 0)

    # 模拟单个按键
    @staticmethod
    def oneKey(key):
        key = key.lower()
        KeyBoard.keyDown(key)
        time.sleep(2)
        KeyBoard.keyUp(key)

    # 模拟组合按键
    @staticmethod
    def twoKeys(key1, key2):
        key1 = key1.lower()
        key2 = key2.lower()

        KeyBoard.keyDown(key1)
        KeyBoard.keyDown(key2)

        KeyBoard.keyUp(key1)
        KeyBoard.keyUp(key2)


if __name__ == '__main__':
    from selenium import webdriver

    driver = webdriver.Firefox()
    driver.get("https://www.baidu.com")
    driver.find_element_by_id("kw").send_keys("python")
    KeyBoard.twoKeys("ctrl", "a")
    KeyBoard.twoKeys("ctrl", "x")
