'''
Created on 8 Nov 2017

@author: vinsharm
'''
import os
import logging 
import settings


class Logger(object):

    def __init__(self, name):
        name = name.replace('.log', '')
        logger = logging.getLogger('log_namespace.%s' % name)  # log_namespace can be replaced with your namespace 
        logger.setLevel(logging.INFO)
        formatter = logging.Formatter('%(asctime)s %(levelname)s:%(name)s %(message)s')
        consoleHandler = logging.StreamHandler()
        consoleHandler.setFormatter(formatter)
        logger.addHandler(consoleHandler)
        self._logger = logger

    def file_handler(self, name):
        name = name.replace('.log', '')
        logger = logging.getLogger('log_namespace.%s' % name)  # log_namespace can be replaced with your namespace 
        logger.setLevel(logging.INFO)
        formatter = logging.Formatter('%(asctime)s %(levelname)s:%(name)s %(message)s')
        file_name = os.path.join(settings.RESOURCES_DIR, '%s.log' % name)  # usually I keep the LOGGING_DIR defined in some global settings file
        handler = logging.FileHandler(file_name)
        handler.setFormatter(formatter)
        handler.setLevel(logging.INFO)
        logger.addHandler(handler)
        self._flogger = logger
    
    def get(self):
        return self._logger
    
    def getFileLogger(self):
        return self._flogger 
