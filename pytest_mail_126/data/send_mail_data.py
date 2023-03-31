"""
@FileName：send_mail_data.py
@Author：stone
@Time：2023/3/30 18:20
@Description：发送邮件信息
"""
from typing import List, Tuple


class SendMailData(object):
    """发送邮件测试数据"""

    send_mail_success = [
        (
            "281754043@qq.com",
            "测试发送普通测试邮件",
            "测试发送普通测试邮件",
            "",
            "发送成功"
        ),
        (
            "281754043@qq.com",
            "测试发送带附件的邮件",
            "测试发送带附件的邮件",
            "D:\\code\\pythonCode\\selenium_project\\pytest_mail_126\\data\\attachment",
            "发送成功"
        ),
        (
            "281754043@qq.com",
            "",
            "测试发送带附件的邮件且主题为空",
            "D:\\code\\pythonCode\\selenium_project\\pytest_mail_126\\data\\attachment",
            "发送成功"
        )
    ]

    send_fail_address_is_none = [
        (
            "",
            "测试收件人地址为空",
            "测试收件人地址为空",
            "D:\\code\\pythonCode\\selenium_project\\pytest_mail_126\\data\\attachment",
            "请填写收件人地址后再发送"
        )
    ]

    send_fail_subject_is_none_data: List[Tuple[str, str, str, str, str]] = [
        (
            "281754043@qq.com",
            "",
            "测试邮件主题为空:不能添加附件",
            "",
            "确定真的不需要写主题吗？"
        )
    ]

    send_fail_address_is_invalid_data = [
        (
            "281754043",
            "测试收件人格式不正确",
            "测试收件人格式不正确",
            "D:\\code\\pythonCode\\selenium_project\\pytest_mail_126\\data\\attachment",
            "以下邮箱地址无效，将无法成功收到邮件"
        )
    ]


if __name__ == '__main__':
    pass

