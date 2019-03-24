import logging
import os
# class logger(object):
#     def __init__(self, file_path):
#         print('Nowy logger!')
#         self.file_path = file_path
#         print('To jest sciezka pliku: ' + self.file_path)

#     def write(self, text):
#         print('Tu zapisuje do pliku text: ' + text)

class logger(object):
    def __init__(self,
                 logger_name=os.path.basename(__file__),
                 log_file_name=os.path.basename(__file__)):
        self.xlogger = logging.getLogger(logger_name)
        self.xlogger.setLevel(logging.DEBUG)
        self.logging_file = logging.FileHandler(
            'Python/logs/' + log_file_name
        )
        self.logging_file.setLevel(logging.DEBUG)
        # self.cmd_handler = logging.StreamHandler()
        # self.cmd_handler.setLevel(logging.ERROR)
        self.formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )
        # self.cmd_handler.setFormatter(self.formatter)
        self.logging_file.setFormatter(self.formatter)
        # self.xlogger.addHandler(self.cmd_handler)
        self.xlogger.addHandler(self.logging_file)

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
