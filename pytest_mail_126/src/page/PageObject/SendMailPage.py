"""
@FileName：SendMailPage.py
@Author：stone
@Time：2023/3/31 9:43
@Description：发送邮件
"""
from src.page.BasePage import BasePage
from util.parseConFile import ParseConFile


class SendMailPage(BasePage):
    # 配置文件的元素读取
    do_conf = ParseConFile()
    # 写信按钮
    write_mail_btn = do_conf.getLocatorsOrAccount("SendMailPageElements", "writeMail")
    # 收件人地址
    address = do_conf.getLocatorsOrAccount("SendMailPageElements", "addressee")
    # 主题
    subject = do_conf.getLocatorsOrAccount("SendMailPageElements", "subject")
    # 上传附件
    upload_attachment = do_conf.getLocatorsOrAccount("SendMailPageElements", "uploadAttachment")
    # 正文外的iframe
    iframe = do_conf.getLocatorsOrAccount("SendMailPageElements", "iframe")
    # 邮件正文
    text = do_conf.getLocatorsOrAccount("SendMailPageElements", "text")
    # 发送邮件确认按钮
    sendBtn = do_conf.getLocatorsOrAccount("SendMailPageElements", "sendBtn")
    # 发送成功的提示信息
    send_success = do_conf.getLocatorsOrAccount("SendMailPageElements", "send_success")
    # 收件人为空的提示信息
    error_info_address_is_none = do_conf.getLocatorsOrAccount('SendMailPageElements', 'error_info_address_is_none')
    # 收件人格式或者主题为空的提示信息
    error_info_popup_window = do_conf.getLocatorsOrAccount('SendMailPageElements', 'error_info_popup_window')

    def send_mail(self, address, subject, text, pfa):
        self.click_write_mail_btn()
        self.input_address(address)
        self.input_subject(subject)
        if pfa:
            self.upload_file(pfa)
        self.switch_frame()
        self.input_main_text(text)
        self.switch_default_frame()
        self.click_send_btn()

    def click_write_mail_btn(self):
        return self.click(*SendMailPage.write_mail_btn)

    def input_address(self, address):
        return self.send_keys(*SendMailPage.address, address)

    def input_subject(self, subject):
        return self.send_keys(*SendMailPage.subject, subject)

    def upload_file(self, pfa):
        return self.send_keys(*SendMailPage.upload_attachment,pfa)

    def switch_frame(self):
        return self.switch_to_frame(*SendMailPage.iframe)

    def input_main_text(self, text):
        return self.send_keys(*SendMailPage.text,text)

    def switch_default_frame(self):
        return self.switch_to_default_frame()

    def click_send_btn(self):
        return self.click(*SendMailPage.sendBtn)

    def wait_success_info_element_located(self):
        return self.wait_element_to_be_located(*SendMailPage.send_success)

    def get_error_address_is_none(self):
        element = self.driver.find_element(*SendMailPage.error_info_address_is_none)
        return element.text

    def get_error_popup_window(self):
        return self.get_element_text(*SendMailPage.error_info_popup_window)
