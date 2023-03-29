"""
@FileName：SendMailPage.py
@Author：stone
@Time：2023/3/28 15:13
@Description：发送邮件的功能
"""
from page.BasePage import BasePage


class  SendMailPage(BasePage):
    # 配置文件的元素读取
    writeMail = BasePage.cf.getLocatorsOrAccount()
    addressee = BasePage.cf.getLocatorsOrAccount()
    subject = BasePage.cf.getLocatorsOrAccount()
    iframe = BasePage.cf.getLocatorsOrAccount()
    text = BasePage.cf.getLocatorsOrAccount()
    sendBtn = BasePage.cf.getLocatorsOrAccount()
    expect = BasePage.cf.getLocatorsOrAccount()
    uploadAttachment = BasePage.cf.getLocatorsOrAccount()
    delete = BasePage.cf.getLocatorsOrAccount()


    def  sendMail(self,Address,Subject,Text,PFA=''):
        """发送邮件功能"""
        self.click(*SendMailPage.writeMail)
        self.sendKeys(*SendMailPage.addressee,Address)
        self.sendKeys(*SendMailPage.subject,Subject)
        self.switchToFrame(*SendMailPage.iframe)
        self.sendKeys(*SendMailPage.text,Text)
        self.switchToDefaultFrame()
        if PFA:
            self.click(*SendMailPage.uploadAttachment)
            self.ctrlV(PFA)
            self.enterKey()
            self.waitElementtobelocated(*SendMailPage.delete)
        self.click(*SendMailPage.sendBtn)



if __name__ == '__main__':
    pass
