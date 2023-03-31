"""
@FileName：TestAddContact.py
@Author：stone
@Time：2023/3/28 16:31
@Description：添加联系人功能
"""
import pytest
from data.contact_data import ContactData


@pytest.mark.contactTest
class TestAddContact(object):
    """添加联系人"""
    contact_data = ContactData

    success_data = contact_data.add_contact_success
    fail_data = contact_data.add_contact_fail

    @pytest.mark.parametrize("name,mail,star,phone,comment,expect", success_data)
    def test_add_contact_success(self, login, refresh_page, name, mail, star, phone, comment, expect):
        """测试添加联系人"""
        home_page = login[1]
        contact_page = login[2]
        home_page.select_menu(menu='mailList')
        contact_page.add_contact(name, mail, star, phone, comment)
        actual = contact_page.get_source()
        assert expect in actual, "添加联系人成功,断言失败"

    @pytest.mark.parametrize('name,mail,star,hone,comment,expect', fail_data)
    def test_add_contact_fail(self, login, refresh_page, name, mail, star, hone, comment, expect):
        home_page = login[1]
        contact_page = login[2]
        home_page.select_menu(menu='mailList')
        contact_page.add_contact(name, mail, star, hone, comment)
        actual = contact_page.get_error_text()
        assert actual == expect, "添加联系人失败,断言失败"


if __name__ == '__main__':
    pytest.main(['-v', "TestAddContact.py"])
