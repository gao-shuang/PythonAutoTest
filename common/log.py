import logging


def get_logger(name,filename,mode='a',encoding='utf-8',fmt=None,debug=False):
    '''
    :param name: 日志器的名字
    :param filename:日志文件名
    :param mode:文件模式
    :param encoding:字符编码
    :param fmt:日志格式
    :param debug:调试模式
    :return:
    '''

#创建一个日志器并设置日志等级
    logger=logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    #确定文件和控制台输出的日志级别，文件处理器的等级一般情况比控制台要高
    if debug:
        file_level=logging.DEBUG
        console_level=logging.DEBUG
    else:
        file_level=logging.WARNING
        console_level=logging.INFO
​
    #定义日志的输出格式
    if fmt is None:
        fmt='%(asctime)s %(levelname)s [%(name)s] [%(filename)s (%(funcName)s:%(lineno)d] - %(message)s'
​
    #创建日志处理器
    #写入文件的日志处理器
    file_handler=logging.FileHandler(filename=filename,mode=mode,encoding=encoding)
    file_handler.setLevel(file_level)
    #写入控制台的日志处理器
    console_handler=logging.StreamHandler()
    console_handler.setLevel(console_level)
​
    #创建格式化器并添加到日志处理器
    formatter=logging.Formatter(fmt=fmt)
    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)
​
    # 将日志处理器添加到日志器上
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)
​
    #返回日志
    return logger