"""
@FileName：ContactPage.py
@Author：stone
@Time：2023/3/28 15:01
@Description：添加联系人的功能
"""
import time

from page.BasePage import BasePage
from page.HomePage import HomePage
from page.LoginPage import LoginPage


class ContactPage(BasePage):
    new_contact = BasePage.cf.getLocatorsOrAccount("ContactPageElements", "new_contact")
    name = BasePage.cf.getLocatorsOrAccount("ContactPageElements", 'name')
    mail = BasePage.cf.getLocatorsOrAccount("ContactPageElements", "mail")
    star = BasePage.cf.getLocatorsOrAccount("ContactPageElements", "star")
    phone = BasePage.cf.getLocatorsOrAccount("ContactPageElements", "phone")
    comment = BasePage.cf.getLocatorsOrAccount("ContactPageElements", "comment")
    commit = BasePage.cf.getLocatorsOrAccount("ContactPageElements", "commit")
    errortip = BasePage.cf.getLocatorsOrAccount("ContactPageElements", "tooltip")

    def newContact(self, Name, Mail, Star, Phone, Comment):
        """添加联系人"""
        self.click(*ContactPage.new_contact)
        self.sendKeys(*ContactPage.name, Name)
        self.sendKeys(*ContactPage.mail, Mail)
        if Star == '1':
            self.click(*ContactPage.star)
        self.sendKeys(*ContactPage.phone, Phone)
        self.sendKeys(*ContactPage.comment, Comment)
        self.click(*ContactPage.commit)

    def assertErrorTip(self, excpted):
        """断言联系人中添加失败是否有提示信息"""
        text = self.getElementText(*ContactPage.errortip)
        print('info:assert {} == {}'.format(text, excpted))
        assert text == excpted


if __name__ == '__main__':
    from selenium import webdriver

    driver = webdriver.Firefox()
    login = LoginPage(driver)
    home = HomePage(driver)
    con = ContactPage(driver, 30)


    name = "test"
    mail = '2398391057@qq.com'
    star = ""
    phone ='134878782342'
    comment = "测试账号"
    username = ""
    password = ""
    login.login(username,password)
    home.selectMenu()
    time.sleep(5)
    con.newContact(name,mail,star,phone,comment)

