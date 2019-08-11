import logging
import os
from sys import argv

file_name = os.path.basename(argv[0])
# logging_format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
logging_format = '%(asctime)s - %(levelname)s - %(message)s'


class CreateLogger(object):
    def __init__(self,
                 logger_name=file_name,
                 log_file_name="'" + file_name + "'.log"
                 ):
        if not os.path.exists('logs'):
            os.mkdir('logs')

        self.xlogger = logging.getLogger(logger_name)
        self.logging_file = logging.FileHandler(
            "logs/" + log_file_name
        )

        self.xlogger.setLevel(logging.DEBUG)
        self.logging_file.setLevel(logging.DEBUG)

        self.formatter = logging.Formatter(logging_format)
        self.logging_file.setFormatter(self.formatter)
        self.xlogger.addHandler(self.logging_file)

        # self.cmd_handler = logging.StreamHandler()
        # self.cmd_handler.setLevel(logging.ERROR)
        # self.cmd_handler.setFormatter(self.formatter)
        # self.xlogger.addHandler(self.cmd_handler)

    def debug(self, debug_message):
        self.xlogger.debug(debug_message)

    def info(self, info_message):
        self.xlogger.info(info_message)

    def warning(self, warning_message):
        self.xlogger.warning(warning_message)

    def error(self, error_message):
        self.xlogger.error(error_message)

    def critical(self, critical_message):
        self.xlogger.critical(critical_message)

    def exception(self, exception_message):
        self.xlogger.exception(exception_message)
