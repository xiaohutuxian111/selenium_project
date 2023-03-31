"""
@FileName：LoginPage.py
@Author：stone
@Time：2023/3/30 20:07
@Description：登录页面
"""
from page.BasePage import BasePage
from util.perseConFile import ParseConFile


class LoginPage(BasePage):
    # 读取配置元素
    do_conf = ParseConFile()
    # 选择密码登录的按钮
    password_login_btn = do_conf.getLocatorsOrAccount('LoginPageElements', 'password_login_btn')
    # 登录的frame页面
    frame = do_conf.getLocatorsOrAccount('LoginPageElements', 'frame')
    # 用户名
    useranme = do_conf.getLocatorsOrAccount('LoginPageElements', 'username')
    # 密码
    password = do_conf.getLocatorsOrAccount('LoginPageElements', 'password')
    # 登录确认按钮
    loginBtn = do_conf.getLocatorsOrAccount('LoginPageElements', 'loginBtn')
    # 报错信息
    error_head = do_conf.getLocatorsOrAccount('LoginPageElements', 'ferrorHead')
    #  登录成功后的用户显示元素
    account = do_conf.getLocatorsOrAccount("HomePageElements", "account")

    def login(self, username, password):
        """登录流程"""
        self.open_url()
        self.click_password_login_btn()
        self.switch_login_frame()
        self.input_useranme(username)
        self.input_password(password)
        self.click_login_btn()

    def open_url(self):
        return self.load_url("https://mail.126.com")

    def switch_login_frame(self):
        return self.click(*LoginPage.password_login_btn)

    def clear_username(self):
        return self.clear(*LoginPage.useranme)

    def input_useranme(self, username):
        self.clear_username()
        return self.send_keys(*LoginPage.useranme,username)

    def clear_password(self):
        return  self.clar(*LoginPage.password)

    def input_password(self, password):
        self.clear_password()
        return self.send_keys(*LoginPage.password,password)

    def click_login_btn(self):
        return self.click(*LoginPage.loginBtn)

    def switch_default_frame(self):
        return  self.switch_to_default_frame()


    def get_error_text(self):
        return self.get_element_text(*LoginPage.error_head)


    def get_login_success_account(self):
        return  self.get_element_text(*LoginPage.account)

