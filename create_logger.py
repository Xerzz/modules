__all__ = ['create_logger']

import os
from sys import argv

filename = os.path.basename(argv[0])
xlist = filename.split('.')
if len(xlist) > 1:
    xlist.pop(-1)
    filename = '.'.join(xlist)


def _create_logs_dir(inside_folder_name=None):
    if not os.path.exists('logs'):
        os.mkdir('logs')
    if inside_folder_name and not os.path.exists(f'logs/{inside_folder_name}'):
        os.mkdir(f'logs/{inside_folder_name}')


def create_logger(logger_name=filename,
                  stream_handler=False,
                  time_rotated_file=True,
                  inside_folder=False,
                  days_to_keep=7,
                  alternative_logging_format=False):
    import logging
    global filename
    log = logging.getLogger(logger_name)

    if inside_folder:
        _create_logs_dir(filename)
        logfile_path = 'logs/{0}/{0}.log'.format(filename)
    else:
        _create_logs_dir()
        logfile_path = f'logs/{filename}.log'

    if alternative_logging_format:
        logging_format = '%(asctime)s %(filename)s [%(levelname)s] %(message)s'
    else:
        logging_format = '%(asctime)s - %(filename)s - %(levelname)s - %(message)s'
    formatter = logging.Formatter(logging_format)

    level = logging.DEBUG
    log.setLevel(level)

    if time_rotated_file:
        from logging.handlers import TimedRotatingFileHandler
        file_handler = TimedRotatingFileHandler(logfile_path, 'midnight', 1, days_to_keep, 'UTF-8')
    else:
        file_handler = logging.FileHandler(logfile_path, encoding='UTF-8')
    file_handler.setFormatter(formatter)
    log.addHandler(file_handler)

    if stream_handler:
        xstream_handler = logging.StreamHandler()
        xstream_handler.setFormatter(formatter)
        log.addHandler(xstream_handler)
    return log
