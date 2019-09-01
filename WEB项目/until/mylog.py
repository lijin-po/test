#！/usr/bin/python
#-*-coding:utf-8-*-
import logging
import datetime
# 日志目录/文件夹
LOG_DIR = 'D:\\新建文件夹\\WEB项目\\log\\'
# 日期.out/txt
# 创建一个日志文件的名字
a=LOG_DIR+str(datetime.datetime.now().date())+".txt"
# logging  ----> python定义日志的库
#定义日志输出的格式                时间           秒        等级（最大4）                      行数          信息
formatter=logging.Formatter(fmt='%(asctime)s,%(msecs)d %(levelname)-4s [%(filename)s:%(lineno)d] %(message)s',
                    datefmt='%d-%m-%Y:%H:%M:%S')
# print(formatter)
# logging的两种输出方式
# 第一种：将日志输出到pycharm的控制台
c = logging.StreamHandler()
# 添加日志的样式
c.setFormatter(formatter)
# 第二种：将日志输出到文本中
w=logging.FileHandler(a,encoding="utf-8")
# 添加日志的样式
w.setFormatter(formatter)

#
def get_logger(filename):
    # 获取执行日志的脚本名字
    l=logging.getLogger(filename)
    # 添加输出内容到控制台
    l.addHandler(c)
    # 添加输出内容到文本
    l.addHandler(w)
    # 定义日志的等级     INFO --->最低等级        CRITICAL  --->致命
    l.setLevel(logging.INFO)
    return l


