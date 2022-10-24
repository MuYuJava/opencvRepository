import logging

'''
1.logging中，日志等级分为debug、info、warning、error、critical
其中日志输出按照大于默认日志器的等级进行输出
debug表示调试信息、info表示普通输出信息、warning表示警告信息、error表示错误信息、critical表示紧急错误信息
2.logging中，包括四个组件为logger(计量器，用于日志采集)、handler(处理器，将日志发送到合适路径)、formatter(格式化器，设定日志格式)、filter(过滤器)
'''


# 初始化logger，并将日志格式、日志保存路径、日志等级进行设置
def init_logger(output_path):
    logger = logging.getLogger()
    # 设置日志信息内容格式
    log_format = "%(asctime)s -- %(levelname)s -- %(message)s"
    # 设置日志保存路径
    log_file = output_path
    # 设置默认级别为debug
    logging.basicConfig(filename=log_file, level=logging.DEBUG, format=log_format)
    return logger


log = init_logger('log/log.txt')
# 由于控制器的日志等级目前为warning，故不会输出debug信息
logging.debug('这是debug1信息')
# 设置控制器日志等级为debug
console = logging.StreamHandler()
console.setLevel(logging.DEBUG)
log.addHandler(console)
# 输出并保存日志内容
logging.debug('这是debug2信息')
logging.info('这是info信息')
logging.warning('这是warning信息')
