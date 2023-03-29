"""
@FileName：conf.py
@Author：stone
@Time：2023/3/16 17:47
@Description：全局配置文件
"""


 # 项目的根目录
import os
from datetime import datetime

base_path =  os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 报告目录
reportDir = os.path.join(base_path,'report')
# ui对象库所在的文件目录
configDir  = os.path.join(base_path,'config','config.ini')
# 测试数据所在的库
excel_path =  os.path.join(base_path,'data','testdate.xlsx')
# 当前时间
currentTime = datetime.now().strftime("%H_%M_%S")



# 邮件配置信息
# 邮件服务器
smtpServer = 'smtp.qq.com'
# 发送者
fromUser = '账号@qq.com'
# 发送者密码
fromPassWord = 'mhxvqpewblldbjhf'
# 接收者
toUser = ['账号@qq.com']# 可以同时发送给多人，追加到列表中
# 邮件标题
subject = 'xx项目自动化测试报告'
# 邮件正文
contents = '测试报告正文'
# 报告名称
htmlName = r'{}\testReport{}.html'.format(reportDir, currentTime)

# 脚本执行命令
args = r'pytest --html=' + htmlName+ ' ' + '--self-contained-html'
# modify by linuxchao at 2019/4/25
args_login = r'pytest --html='+ htmlName+ ' ' + '-m' + ' ' + 'loginTest'+ ' --self-contained-html'
args_contact = r'pytest --html='+ htmlName+ ' ' + '-m' + ' ' + 'contactTest'+ ' --self-contained-html'
args_sendmail = r'pytest --html='+ htmlName+ ' ' + '-m' + ' ' + 'sendMailTest'+ ' --self-contained-html'




















