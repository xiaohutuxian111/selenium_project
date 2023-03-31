"""
@FileName：conf.py
@Author：stone
@Time：2023/3/16 17:47
@Description：全局配置文件
"""

# 项目的根目录
import os
from datetime import datetime

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 报告目录
REPORT_DIR = os.path.join(ROOT_DIR, 'report')
# ui对象库所在的文件目录
CONF_PATH = os.path.join(ROOT_DIR, 'config', 'config.ini')
# 测试数据所在的库
DATA_PATH = os.path.join(ROOT_DIR, 'data', 'testdate.xlsx')
# 当前时间
CURRENT_TIME = datetime.now().strftime("%H_%M_%S")

# 邮件服务器
SMTP_SERVER = 'smtp.qq.com'
# 发送者
FROM_USER = '账号@qq.com'
# 发送者密码
FROM_PASSWORD = 'mhxvqpewblldbjhf'
# 接收者
TO_USER = ['账号@qq.com']  # 可以同时发送给多人，追加到列表中
# 邮件标题
SUBJECT = 'xx项目自动化测试报告'
# 邮件正文
CONTENTS = '测试报告正文'
# 报告名称
HTML_NAME = 'testReport{}.html'.format(CURRENT_TIME)
print(HTML_NAME)
