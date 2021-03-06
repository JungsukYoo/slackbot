import logging
import logging.handlers
import os

from common import log_level


def get_logger(logger_name):

    Logger = logging.getLogger(logger_name)


    if log_level == 'debug':
        level = logging.DEBUG
    elif log_level == 'info':
        level = logging.INFO
    elif log_level == 'warn':
        level = logging.WARNING
    elif log_level == 'error':
        level = logging.ERROR
    elif log_level == 'critical':
        level = logging.CRITICAL
    else:
        level = logging.WARNING
    
    Logger.setLevel(level)
    LOG_FORMAT = ('%(levelname) -10s %(asctime)s %(name) -20s %(funcName) '
                  '-20s %(process)d %(lineno) -5d: %(message)s')
    LOG_FORMAT_DEP = '[%(levelname)s|%(filename)s:%(lineno)s-%(process)d] %(asctime)s > %(message)s'
    formatter = logging.Formatter(LOG_FORMAT)
    
    dir = "./logs/"
    if not os.path.exists(os.path.dirname(dir)):
        os.makedirs(dir)
    
    log_name = "./logs/" + logger_name + ".log"

    if not os.path.exists(log_name):
        f = open(log_name, 'w')
        f.close
    
    file_handler = logging.handlers.TimedRotatingFileHandler(filename=log_name,
                                                             encoding='utf8',
                                                             when='midnight',
                                                             backupCount=100
                                                            )
    file_handler.setFormatter(formatter)
    stream_hander = logging.StreamHandler()
    stream_hander.setFormatter(formatter)

    Logger.addHandler(file_handler)
    Logger.addHandler(stream_hander)

    Logger.debug('Logger generated')

    return Logger


def Logger(name='meal'):
    return get_logger(logger_name=name)


