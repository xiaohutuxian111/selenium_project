"""
@FileName：login_data.py
@Author：stone
@Time：2023/3/30 18:19
@Description：登录测试数据
"""

class LoginData(object):
    """用户登录测试数据"""

    login_success_data = [
        (
            "defoliationfly@126.com",
            "",
            "defoliationfly@126.com"
        )
    ]

    login_fail_data = [
        (
            "linuxxiaochao",
            "",
            "请输入密码"
        ),
        (
            "",
            "xiaochao11520",
            "请输入帐号"
        ),
        (
            "linux",
            "xiaochao",
            "帐号或密码错误"
        )
    ]


if __name__ == '__main__':
    pass
