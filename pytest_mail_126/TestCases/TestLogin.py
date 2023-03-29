"""
@FileName：TestLogin.py
@Author：stone
@Time：2023/3/28 15:29
@Description：测试登录功能
"""

import pytest

from page.LoginPage import LoginPage


@pytest.mark.loginTest
class TestLogin(object):
    # 测试数据
    loginSheet = LoginPage.getSheet('login')
    data = LoginPage.excel.getAllValuesOfSheet(loginSheet)

    #  正确的账号和密码
    userName = LoginPage.cf.getLocatorsOrAccount()
    passWord = LoginPage.cf.getLocatorsOrAccount()

    @pytest.fixture()
    def teardown_func(self, driver):
        """
        执行每个用例之后要清除一下 cookie
        否则你第一个账号登录之后，重新加载网址还是登录系统，无法测试后面的账号
        """
        yield
        driver.delete_all_cookies()

    @pytest.mark.parametrize("username,password,expect", data)
    def test_login(self, teardown_func, driver, username, password, expect):
        """测试登录"""
        login = LoginPage(driver, 30)
        login.login(username, password)
        login.sleep(5)
        # 登录失败，对提示信息进行验证
        if username == TestLogin.userName and password == TestLogin.passWord:
            login.assertValueInSource(expect)
        elif username == "":
            login.assertTextEqString(expect)
        elif username != "":
            login.assertTextEqString(expect)
        elif username == "" and password == "":
            login.assertTextEqString(expect)
        else:
            login.assertTextEqString(expect)


if __name__ == '__main__':
    pass
