"""
@FileName：test_loginCase.py
@Author：stone
@Time：2023/3/28 15:29
@Description：测试登录功能
"""

import pytest
from data.login_data import LoginData


@pytest.mark.loginTest
class TestLogin(object):
    """登录测试"""
    login_data = LoginData

    @pytest.mark.parametrize('username,password,expect', login_data.login_success_data)
    def test_login(self, open_url, username, password, expect):
        login_page = open_url
        login_page.login(username, password)
        login_page.switch_default_frame()
        actual = login_page.get_login_success_acount()
        assert expect in actual, "登录成功,断言失败"

    @pytest.mark.parametrize('username,password,expect', login_data.login_fail_data)
    def test_fail(self, open_url, username, password, expect):
        login_page = open_url
        login_page.login(username, password)
        actual = login_page.get_error_text()
        assert actual == expect, "登录失败,断言失败"


if __name__ == '__main__':
    pytest.main(['-v', 'test_loginCase.py'])