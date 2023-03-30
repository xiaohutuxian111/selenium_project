"""
@FileName：SendMailPage.py
@Author：stone
@Time：2023/3/28 15:13
@Description：发送邮件的功能
"""
import time

from page.BasePage import BasePage
from page.HomePage import HomePage
from page.LoginPage import LoginPage


class SendMailPage(BasePage):
    # 配置文件的元素读取
    writeMail = BasePage.cf.getLocatorsOrAccount("SendMailPageElements", "writeMail")
    addressee = BasePage.cf.getLocatorsOrAccount("SendMailPageElements", "addressee")
    subject = BasePage.cf.getLocatorsOrAccount("SendMailPageElements", "subject")
    iframe = BasePage.cf.getLocatorsOrAccount("SendMailPageElements", "iframe")
    text = BasePage.cf.getLocatorsOrAccount("SendMailPageElements", "text")
    sendBtn = BasePage.cf.getLocatorsOrAccount("SendMailPageElements", "sendBtn")
    expect = BasePage.cf.getLocatorsOrAccount("SendMailPageElements", "expect")
    uploadAttachment = BasePage.cf.getLocatorsOrAccount("SendMailPageElements", "uploadAttachment")
    delete = BasePage.cf.getLocatorsOrAccount("SendMailPageElements", "delete")

    def sendMail(self, Address, Subject, Text, PFA=''):
        """发送邮件功能"""
        self.click(*SendMailPage.writeMail)
        self.sendKeys(*SendMailPage.addressee, Address)
        self.sendKeys(*SendMailPage.subject, Subject)
        self.switchToFrame(*SendMailPage.iframe)
        self.sendKeys(*SendMailPage.text, Text)
        self.switchToDefaultFrame()
        if PFA:
            self.click(*SendMailPage.uploadAttachment)
            self.ctrlV(PFA)
            self.enterKey()
            self.waitElementtobelocated(*SendMailPage.delete)
        self.click(*SendMailPage.sendBtn)


if __name__ == '__main__':
    from selenium import webdriver
    driver = webdriver.Firefox()
    login = LoginPage(driver)
    username = ""
    password = ""
    login.login(username,password)
    home = HomePage(driver)
    home.selectMenu("inBox")
    time.sleep(3)
    Address=""
    Subject = "test"
    Text = "qqqqqqqqqqqqqqqqqqqqqqqqqqqqq"
    send = SendMailPage(driver)
    send.sendMail(Address,Subject,Text)



