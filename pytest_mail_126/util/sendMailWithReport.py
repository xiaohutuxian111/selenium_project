"""
@FileName：sendMailWithReport.py
@Author：stone
@Time：2023/3/28 18:11
@Description：
"""

import yagmail


class SendMailWithReport():

    @staticmethod
    def send_mail(smtp_server, from_user, from_pass_word,
                  to_user, subject, contents,
                  file_name):
        #  初始化服务器信息
        yag = yagmail.SMTP(from_user, from_pass_word, smtp_server)
        # 发送邮件
        yag.send(to_user, subject, contents, file_name)


if __name__ == '__main__':
    SendMailWithReport.send_mail('smtp.qq.com',
                                 '账号@qq.com',
                                 'mhxvqpewblldbjhf',
                                 '账号@qq.com',
                                 'python自动化测试',
                                 '邮件正文',
                                 '17_12_07.html')
