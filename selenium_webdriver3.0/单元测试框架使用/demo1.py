from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

binary = FirefoxBinary()


# 修改浏览器驱动过的
driver = webdriver.Firefox(firefox_binary=binary, executable_path=r'D:\soft\tools\浏览器驱动\geckodriver.exe')

driver.get("http:www.baidu.com")

