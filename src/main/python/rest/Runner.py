'''
Created on 9 Nov 2017

@author: vinsharm
'''
from flask import  Flask
from flask_restful import Api
from utils.custom_log import Logger
from rest import tracks as tracks
class Runner(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        
    
    def run_app(self):
        app = Flask(__name__)
        api = Api(app)
        port_num = '5003'
        api.add_resource(tracks, '/tracks')  # Route_2
        app.run(port=port_num)
        


if __name__ == '__main__':
    run = Runner()
    run.run_app()
    