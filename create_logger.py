__all__ = ['CreateLogger']

import logging
import os
from logging.handlers import TimedRotatingFileHandler
from sys import argv

# getting filename
filename = os.path.basename(argv[0])
# if file has dots in name
tmp_list = filename.split('.')
if len(tmp_list) > 1:
    tmp_list.pop(-1)
    filename = '.'.join(tmp_list)


def _create_logs_dir(inside_folder_name=None):
    if not os.path.exists('logs'):
        os.mkdir('logs')
    if inside_folder_name and not os.path.exists(f'logs/{inside_folder_name}'):
        os.mkdir(f'logs/{inside_folder_name}')


class CreateLogger(object):
    def __init__(self, logger_name=filename,
                 stream_handler=False,
                 file_handler=True,
                 time_rotated_file=True,
                 days_to_keep=7,
                 log_inside_folder=False):
        # create logger
        self._log = logging.getLogger(logger_name)
        self.file_handler = None
        self.cmd_handler = None
        self.loglevel = logging.DEBUG
        # create logs directories
        if log_inside_folder:
            _create_logs_dir(logger_name)
            self._logfile_name = f'{filename}/{filename}.log'
        else:
            _create_logs_dir()
            self._logfile_name = f'{filename}.log'
        # create log format
        self._log_format = None
        self.change_format()
        # adding file handler
        if file_handler or stream_handler is False:
            self.add_file_handler(time_rotated_file, days_to_keep)
        # adding stream handler
        if stream_handler or file_handler is False:
            self.add_stream_handler()
        # setting level

        self._log.setLevel(self.loglevel)

    def debug(self, debug_message):
        self._log.debug(debug_message)

    def info(self, info_message):
        self._log.info(info_message)

    def warning(self, warning_message):
        self._log.warning(warning_message)

    def error(self, error_message):
        self._log.error(error_message)

    def critical(self, critical_message):
        self._log.critical(critical_message)

    def exception(self, exception_message='', one_line=True, delimiter='|'):
        if one_line:
            import traceback
            exception = delimiter.join(traceback.format_exc().split('\n'))
            self._log.error(f'{exception_message} {delimiter}{exception}')
        else:
            self._log.exception(exception_message)

    def add_stream_handler(self):
        self.cmd_handler = logging.StreamHandler()
        self.cmd_handler.setLevel(self.loglevel)
        self.cmd_handler.setFormatter(self._log_format)
        self._log.addHandler(self.cmd_handler)

    def add_file_handler(self, time_rotated_file=True, days_to_keep=7):
        if time_rotated_file:
            self.file_handler = TimedRotatingFileHandler(f'logs/{self._logfile_name}',
                                                         'midnight', 1, days_to_keep, 'UTF-8')
        else:
            self.file_handler = logging.FileHandler(f'logs/{self._logfile_name}', encoding='UTF-8')
        self.file_handler.setLevel(self.loglevel)
        self.file_handler.setFormatter(self._log_format)
        self._log.addHandler(self.file_handler)

    def change_level(self, level):
        if level == 'info' or level == 20:
            self.loglevel = logging.INFO
        elif level == 'warning' or level == 30:
            self.loglevel = logging.WARNING
        elif level == 'error' or level == 40:
            self.loglevel = logging.ERROR
        elif level == 'critical' or level == 50:
            self.loglevel = logging.CRITICAL
        else:
            self.loglevel = logging.DEBUG

        if self.file_handler:
            self.file_handler.setLevel(self.loglevel)
        if self.cmd_handler:
            self.cmd_handler.setLevel(self.loglevel)

    def change_format(self, log_format='%(asctime)s - %(filename)s - %(levelname)s - %(message)s'):
        self._log_format = logging.Formatter(log_format)
        if self.file_handler:
            self.file_handler.setFormatter(self._log_format)
        if self.cmd_handler:
            self.cmd_handler.setFormatter(self._log_format)

    def handlers(self):
        return self._log.handlers
