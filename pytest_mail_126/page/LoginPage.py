"""
@FileName：LoginPage.py
@Author：stone
@Time：2023/3/28 14:49
@Description：登录功能
"""
from page.BasePage import BasePage


class LoginPage(BasePage):
    # 读取配置元素
    frame = BasePage.cf.getLocatorsOrAccount('LoginPageElements','frame')
    useranme = BasePage.cf.getLocatorsOrAccount('LoginPageElements','username')
    password = BasePage.cf.getLocatorsOrAccount('LoginPageElements','password')
    loginBtn = BasePage.cf.getLocatorsOrAccount('LoginPageElements','loginBtn')
    ferrorHead = BasePage.cf.getLocatorsOrAccount('LoginPageElements','ferrorHead')

    def login(self, userName, passWord):
        """登录"""
        self.loadUrl("https:mail.126.com")
        self.switchToFrame(*LoginPage.frame)
        self.clear(*LoginPage.useranme)
        self.sendKeys(*LoginPage.useranme, userName)
        self.clear(*LoginPage.password)
        self.sendKeys(*LoginPage.password, passWord)
        self.click(*LoginPage.loginBtn)
        self.switchToDefaultFrame()

    def assertTextEqString(self, expected, name=None):
        """提示信息与期望是否一致"""
        self.switchToFrame(*LoginPage.frame)
        text = self.getElementText(*LoginPage.ferrorHead, name)
        self.switchToDefaultFrame()
        print('info:asset "{}" == "{}"'.format(text, expected))
        assert text == expected, "{}!={}".format(text, expected)

if __name__ == '__main__':
    pass



