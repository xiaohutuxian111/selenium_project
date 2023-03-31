"""
@FileName：ContactPage.py
@Author：stone
@Time：2023/3/30 19:35
@Description：新建联系人
"""
from page.BasePage import BasePage
from util.perseConFile import ParseConFile


class ContactPage(BasePage):
    # 读取配置文件元素
    do_conf = ParseConFile()
    # 新建联系人按钮
    new_contact = do_conf.getLocatorsOrAccount("ContactPageElements", "new_contact")
    # 姓名输入框
    name = do_conf.getLocatorsOrAccount("ContactPageElements", 'name')
    # 电子邮件输入框
    mail = do_conf.getLocatorsOrAccount("ContactPageElements", "mail")
    # 标记为星级
    star = do_conf.getLocatorsOrAccount("ContactPageElements", "star")
    # 电话号码输入框
    phone = do_conf.getLocatorsOrAccount("ContactPageElements", "phone")
    # 备注输入框
    comment = do_conf.getLocatorsOrAccount("ContactPageElements", "comment")
    # 确定按钮
    commit = do_conf.getLocatorsOrAccount("ContactPageElements", "commit")
    # 添加失败提示信息
    error_tip = do_conf.getLocatorsOrAccount("ContactPageElements", "tooltip")

    def add_contact(self, name, mail, star, phone, comment):
        """添加联系人"""
        self.click_new_contact_btn()
        self.input_name(name)
        self.input_mail(mail)
        if star == '1':
            self.select_str()
        self.input_phone(phone)
        self.input_comment(comment)
        self.click_commit_btn()

    def click_new_contact_btn(self):
        return self.click(*ContactPage.new_contact)

    def input_name(self, name):
        return self.send_keys(*ContactPage.name, name)

    def input_mail(self, mail):
        return self.send_keys(*ContactPage.mail, mail)

    def select_str(self):
        return self.click(*ContactPage.star)

    def input_phone(self, phone):
        return self.send_keys(*ContactPage.phone, phone)

    def input_comment(self, comment):
        return self.send_keys(*ContactPage.comment, comment)

    def click_commit_btn(self):
        return self.click(*ContactPage.commit)

    def get_error_text(self):
        return self.get_element_text(*ContactPage.error_tip)
