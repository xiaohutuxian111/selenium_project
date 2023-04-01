"""
@FileName：RunTestCase.py
@Author：stone
@Time：2023/3/28 17:48
@Description：主函数
"""

import sys
import pytest



from util.sendMailWithReport import SendMailWithReport
from config.conf import ROOT_DIR, HTML_NAME


def main():
    # 判断项目的根目录是否在sys.path中，没有就参加
    if ROOT_DIR not in sys.path:
        sys.path.append(ROOT_DIR)
    # 执行用例
    args = ['--reruns', '1', '--html=' + './report/' + HTML_NAME]
    pytest.main(args)

    # 发送邮件
    # SendMailWithReport.send_mail(
    #     smtp_server, from_user, from_pass_word,
    #     to_user, subject, contents,
    #     file_name
    # )


if __name__ == '__main__':
    main()
