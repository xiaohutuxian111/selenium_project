"""
@FileName：RunTestCase.py
@Author：stone
@Time：2023/3/28 17:48
@Description：主函数
"""

import sys
import pytest


from util.sendMailWithReport import SendMailWithReport

sys.path.append('.')
from config.conf import ROOT_DIR, HTML_NAME


def main():
    # 判断项目的根目录是否在sys.path中，没有就参加
    if ROOT_DIR not in sys.path:
        sys.path.append(ROOT_DIR)
    # 执行用例
    # ["-v", "-m", "demo", "--reruns", "2", "--reruns-delay", "5", "--alluredir=../OutPuts/allure-results"]
    args = ['--reruns', '2', '--html=' + './report/' + HTML_NAME]
    pytest.main(args)
    # 发送邮件
    # SendMailWithReport.send_mail(
    #     smtpServer, fromUser, fromPassWord,
    #     toUser, subject, contents,
    #     htmlName
    # )


if __name__ == '__main__':
    main()
