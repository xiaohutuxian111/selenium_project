"""
@FileName：contact_data.py
@Author：stone
@Time：2023/3/30 18:18
@Description：联系人数据
"""
class ContactData(object):
    """添加联系人测试数据"""

    add_contact_success = [
        (
            "linux1",
            "281754041@qq.com",
            "1",
            "13691579841",
            "添加联系人1",
            "281754041@qq.com"
        )
    ]
    add_contact_fail = [
        (
            "linux2",
            "@qq.com",
            "0",
            "13691579842",
            "添加联系人2",
            "请正确填写邮件地址。"
        )
    ]


if __name__ == '__main__':
    pass