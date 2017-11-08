'''
Created on 8 Nov 2017

@author: vinsharm
'''
from database.custom_log import Logger


class CustomClass(object):

    def __init__(self):
        self.logger = Logger(self.__class__.__name__).get()  # accessing the "private" variables for each class

    def do_something(self):
        
        self.logger.info('Hello')
        print('hello')

    def raise_error(self):
        self.logger.error('some error message')


if __name__ == '__main__':
    cc = CustomClass()
    cc.do_something()
