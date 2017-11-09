'''
Created on 9 Nov 2017

@author: vinsharm
'''
from flask import jsonify, Flask
from flask_restful import Resource, Api
from utils.custom_log import Logger
from connect import Connect


class Tracks(Resource):

    def __init__(self):
        # self.logger = logging.getLogger(__name__)
        self.logger = Logger(self.__class__.__name__).get() 
        self.connect = Connect()

        # self.logger('creating an instance of Class')
    def get(self):
        conn = self.connect.db_connect()
        query = conn.execute("select trackid, name, composer, unitprice from tracks;")
        result = {'data': [dict(zip(tuple (query.keys()) , i)) for i in query.cursor]}
        return jsonify(result)

    
    def main(self):
        app = Flask(__name__)
        api = Api(app)
        api.add_resource(Tracks, '/tracks')  # Route_2
        port_num = '5003'
        app.run(port=port_num)
        self.logger.info('Application %s running %d' , app, port_num)


if __name__ == '__main__':
    tracks = Tracks()
    tracks.main()
