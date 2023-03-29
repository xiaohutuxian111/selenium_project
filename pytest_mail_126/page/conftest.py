"""
@FileName：conftest.py
@Author：stone
@Time：2023/3/28 15:22
@Description：用户登录前提操作
"""
import pytest

from page.LoginPage import LoginPage

username = LoginPage.cf.getLocatorsOrAccount()
password =  LoginPage.cf.getLocatorsOrAccount()




@pytest.fixture(scope='function')
def   login(driver):
    """除了登录用例是每一个用例的前置用例"""
    print("--------------------start login------------")
    loginFunc = LoginPage(driver,30)
    loginFunc.login(username,password)
    yield
    print("-------------------end login-------------------")
    driver.delete_all_cookies()
