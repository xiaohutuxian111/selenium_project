"""
@FileName：ContactPage.py
@Author：stone
@Time：2023/3/28 15:01
@Description：添加联系人的功能
"""
from page.BasePage import BasePage


class ContactPage(BasePage):
    new_contact = BasePage.cf.getLocatorsOrAccount()
    name = BasePage.cf.getLocatorsOrAccount()
    mail = BasePage.cf.getLocatorsOrAccount()
    star = BasePage.cf.getLocatorsOrAccount()
    phone = BasePage.cf.getLocatorsOrAccount()
    comment = BasePage.cf.getLocatorsOrAccount()
    commit = BasePage.cf.getLocatorsOrAccount()
    errortip = BasePage.cf.getLocatorsOrAccount()

    def newContact(self, Name, Mail, Star, Phone, Comment):
        """添加联系人"""
        self.click(*ContactPage.new_contact)
        self.sendKeys(*ContactPage.name, Name)
        self.sendKeys(*ContactPage.mail, Mail)
        if Star == '1':
            self.click(*ContactPage.star)
        self.sendKeys(*ContactPage.phone, Phone)
        self.sendKeys(*ContactPage.comment, Comment)
        self.click(*ContactPage.comment)

    def assertErrorTip(self, excpted):
        """断言联系人中添加失败是否有提示信息"""
        text = self.getElementText(*ContactPage.errortip)
        print('info:assert {} == {}'.format(text, excpted))
        assert text == excpted


if __name__ == '__main__':
    pass
