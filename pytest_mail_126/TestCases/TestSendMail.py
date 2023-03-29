"""
@FileName：TestSendMail.py
@Author：stone
@Time：2023/3/28 16:54
@Description：
"""
import pytest

from page.SendMailPage import SendMailPage


class TestSendMail(object):
    sendMailSheet = SendMailPage.getSheet("mail")
    data = SendMailPage.excel.getAllValuesOfSheet(sendMailSheet)

    @pytest.mark.sendmail
    @pytest.mark.parametrize("Address,Subject,Text,PFA", data)
    def test_sendMail(self, driver, login, Address, Subject, Text, PFA):
        # 测试发送数据
        send_mail = SendMailPage(driver)
        send_mail.sendMail(Address, Subject, Text, PFA)
        send_mail.sleep(5)
        assert send_mail.isAlertAndSwitchToIt(*SendMailPage.expect)


if __name__ == '__main__':
    pass
