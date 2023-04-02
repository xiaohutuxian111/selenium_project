"""
@FileName：log.py
@Author：stone
@Time：2023/4/1 20:28
@Description：基于loguru日志工具
"""

# class Log(object):
#     """编写日志类，供其他模块调用"""
#
#     def __init__(self, logger):
#         # 拼接日志文件夹，如果不存在则自动创建
#         # cur_path = os.path.dirname(os.path.realpath(__file__))
#         log_path = LOG_PATH
#         if not os.path.exists(log_path): os.mkdir(log_path)
#
#         # 设置日志文件名称格式及日志等级
#         self.log_name = os.path.join(log_path, '%s.log' % time.strftime('%Y-%m-%d'))
#         self.logger = logging.getLogger(logger)
#         self.logger.setLevel(logging.DEBUG)
#
#         # 创建一个handler，将日志写入日志文件
#         fh = logging.FileHandler(self.log_name, 'a', encoding='utf-8')
#         fh.setLevel(logging.INFO)
#
#         # 再创建一个handler，将日志输出到控制台
#         ch = logging.StreamHandler()
#         ch.setLevel(logging.INFO)
#
#         # 定义日志输出格式
#         self.formatter = logging.Formatter('%(asctime)s %(filename)s [line:%(lineno)d] %(levelname)s %(message)s')
#         ch.setFormatter(self.formatter)
#         fh.setFormatter(self.formatter)
#
#         # 给logger添加handler
#         self.logger.addHandler(fh)
#         self.logger.addHandler(ch)
#
#     def get_log(self):
#         return self.logger
import os

"""操作日志记录
"""
import time
from loguru import logger
from config.conf import LOG_PATH



t = time.strftime("%Y_%m_%d")



class Loggings:
    __instance = None
    logger.add(f"{LOG_PATH}/selenium_{t}.log", rotation="500MB", encoding="utf-8", enqueue=True,
               retention="10 days")

    # 单例模式防止重复创建日志文件
    def __new__(cls, *args, **kwargs):
        if not cls.__instance:
            cls.__instance = super(Loggings, cls).__new__(cls, *args, **kwargs)

        return cls.__instance

    def info(self, msg):
        return logger.info(msg)

    def debug(self, msg):
        return logger.debug(msg)

    def warning(self, msg):
        return logger.warning(msg)

    def error(self, msg):
        return logger.error(msg)


loggings = Loggings()
if __name__ == '__main__':
    loggings.info("中文test")
    loggings.debug("中文test")
    loggings.warning("中文test")
    loggings.error("中文test")

    logger.info('If you are using Python {}, prefer {feature} of course!', 3.6, feature='f-strings')
    n1 = "cool"
    n2 = [1, 2, 3]
    logger.info(f'If you are using Python {n1}, prefer {n2} of course!')
