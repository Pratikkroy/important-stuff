import logging 
from .singleton import Singleton
from settings.base import LOGS

class Logger(Singleton):
    def __init__(self):
        logs_file_name = LOGS+"newfile.log"
        format = '%(asctime)s - %(levelname)s - %(message)s'
        # logging.basicConfig(filename=logs_file_name, 
        #                 format = format,
        #                 filemode='w')
        self.logger = logging.getLogger('BlogsLogger')
        console_handler = self.configure_console_handler(format)
        file_handler = self.configure_file_handler(format, logs_file_name)
        self.logger.addHandler(console_handler)
        self.logger.addHandler(file_handler)
    
    def debug(self, message):
        self.logger.debug(message)
        
    def info(self, message):
        self.logger.info(message)
        
    def warn(self, message):
        self.logger.warn(message)
        
    def error(self, message):
        self.logger.error(message)
        
    def exception(self, message):
        self.logger.exception("Exception:: {}".format(message))
        
    
    def configure_console_handler(self, format):
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.INFO)
        console_handler.setFormatter(logging.Formatter(format))
        return console_handler
    
    
    def configure_file_handler(self, format, logs_file_name):
        file_handler = logging.FileHandler(logs_file_name)
        file_handler.setLevel(logging.INFO)
        file_handler.setFormatter(logging.Formatter(format))
        return file_handler
    