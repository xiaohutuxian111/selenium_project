"""
@FileName：TestAddContact.py
@Author：stone
@Time：2023/3/28 16:31
@Description：添加联系人功能
"""
import re

from page.ContactPage import ContactPage
from page.HomePage import HomePage


class TestAddContact(object):

    # 测试数据
    contactsheet = ContactPage.getSheet('contact')
    data =  ContactPage.excel.getAllValuesOfSheet(contactsheet)

    @pytest.mark.newcontact
    @pytest.mark.parametrize("Name,Mail,Star,Phone,Comment,expect",data)
    def test_NewContact(self,driver,login,Name,Mail,Star,Phone,Comment,expect):
        """测试添加联系人"""
        home_page = HomePage(driver)
        contact_page = ContactPage(driver)
        home_page.selectMenu()
        contact_page.new_contact(Name,Mail,Star,Phone,Comment)
        home_page.sleep(5)

        # 检验错误的信息是否提示信息正确
        if re.match(r'^.{1,}@[0-9a-zA-Z]{1,13}\..*$', Mail):
            contact_page.assertValueInSource(expect)
        else:
            contact_page.assertValueInSource(expect)

if __name__ == '__main__':
    pass




