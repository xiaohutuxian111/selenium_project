"""
@FileName：RunTestCase.py
@Author：stone
@Time：2023/3/28 17:48
@Description：主函数
"""

import sys

sys.path.append('.')
from config.conf import *
from util.sendMailWithReport import SendMailWithReport


def main():
    # 判断项目的根目录是否在sys.path中，没有就参加
    if projectDir not in sys.path:
        sys.path.append(projectDir)
    # 执行用例
    os.system(args)
    # 发送邮件
    SendMailWithReport.send_mail(
        smtpServer, fromUser, fromPassWord,
        toUser, subject, contents,
        htmlName
    )


if __name__ == '__main__':
    main()
