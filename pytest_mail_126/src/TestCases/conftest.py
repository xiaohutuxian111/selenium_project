"""
@FileName：conftest.py
@Author：stone
@Time：2023/3/28 15:22
@Description：用户登录前提操作
"""
import pytest

from src.page.PageObject import ContactPage
from src.page.PageObject.HomePage import HomePage
from src.page.PageObject.LoginPage import LoginPage
from src.page.PageObject import SendMailPage
from util.parseConFile import ParseConFile
from util.log import loggings

do_conf = ParseConFile()
username = do_conf.getLocatorsOrAccount("126LoginAccount", 'username')
password = do_conf.getLocatorsOrAccount("126LoginAccount", 'password')


@pytest.fixture(scope='function')
def ini_pages(driver):
    login_page = LoginPage(driver)
    home_page = HomePage(driver)
    contact_page = ContactPage(driver)
    send_mail_page = SendMailPage(driver)
    yield driver, login_page, home_page, contact_page, send_mail_page


@pytest.fixture(scope='function')
def open_url(ini_page):
    driver = ini_page[0]
    login_page = ini_pages[1]
    yield login_page
    driver.delete_all_cookies()


@pytest.fixture(scope='class')
def login(ini_pages):
    """除了登录用例是每一个用例的前置用例"""
    driver, login_page, home_page, contact_page, send_mail_page = ini_pages
    loggings.info("--------------------start login------------")
    login_page.login(username, password)
    login_page.switch_to_default_frame()
    yield login_page, home_page, contact_page, send_mail_page
    loggings.info("-------------------end login-------------------")
    driver.delete_all_cookies()


@pytest.fixture(scope='function')
def refresh_page(ini_pages):
    driver = ini_pages[0]
    yield
    driver.refresh()
