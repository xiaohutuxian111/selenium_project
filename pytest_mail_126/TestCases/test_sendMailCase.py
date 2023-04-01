"""
@FileName：test_sendMailCase.py
@Author：stone
@Time：2023/3/28 16:54
@Description:发送邮件测试案例
"""
import pytest

from data.send_mail_data import SendMailData



@pytest.mark.sendMailTest
class TestSendMail(object):
    """发送邮件"""
    # sendMailSheet = SendMailPage.getSheet("mail")
    # data = SendMailPage.excel.getAllValuesOfSheet(sendMailSheet)
    mail_data = SendMailData
    send_success_data = mail_data.send_mail_success
    send_fail_address_is_none_data = mail_data.send_fail_address_is_none
    send_fail_address_is_invalid_data = mail_data.send_fail_address_is_invalid_data
    send_fail_subject_is_none_data = mail_data.send_fail_subject_is_none_data

    @pytest.mark.sendmail
    @pytest.mark.parametrize("address,subject,text,pfa,expect", send_success_data)
    def test_send_mail_success(self, login, address, subject, text, pfa, expect):
        home_page = login[1]
        send_mail_page = login[3]
        home_page.select_menu(menu="homePage")
        send_mail_page.send_mail(address, subject, text, pfa)
        send_mail_page.wait_success_info_element_located()
        actual = send_mail_page.get_source()
        assert expect in actual, "发送邮件成功,断言失败"

    @pytest.mark.parametrize("address,subject,text,pfa,expect", send_fail_address_is_none_data)
    def test_fail_address_is_none_data(self, login, address, subject, text, pfa, expect):
        home_page = login[1]
        send_mail_page = login[3]
        home_page.select_menu(menu="homePage")
        send_mail_page.send_mail(address, subject, text, pfa)
        actual = send_mail_page.get_error_address_is_none()
        assert expect == actual, "发送邮件成功,断言失败"

    @pytest.mark.parametrize("address,subject,text,pfa,expect", send_fail_address_is_invalid_data)
    def test_fail_address_is_invalid_data(self, login, address, subject, text, pfa, expect):
        home_page = login[1]
        send_mail_page = login[3]
        home_page.select_menu(menu="homePage")
        send_mail_page.send_mail(address, subject, text, pfa)
        actual = send_mail_page.get_error_popup_window()
        assert expect == actual, "发送邮件成功,断言失败"

    @pytest.mark.parametrize("address,subject,text,pfa,expect", send_fail_subject_is_none_data)
    def test_fail_subject_is_none_data(self, login, address, subject, text, pfa, expect):
        home_page = login[1]
        send_mail_page = login[3]
        home_page.select_menu(menu="homePage")
        send_mail_page.send_mail(address, subject, text, pfa)
        actual = send_mail_page.get_error_popup_window()
        assert expect == actual, "发送邮件成功,断言失败"


if __name__ == '__main__':
    pytest.main(['v', 'test_sendMailCase.py'])
