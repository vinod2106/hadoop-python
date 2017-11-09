'''
Created on 9 Nov 2017

@author: vinsharm
'''
from flask import jsonify
from flask_restful import Resource
from connect import Connect

class Employee_Name(Resource):
    
    def __init__(self):
        self.connect = Connect()
        
    def get(self, employee_id):
        conn = self.connect.db_connect()
        query = conn.execute("select * from employees where EmployeeId =%d " % int(employee_id))
        result = {'data': [dict(zip(tuple (query.keys()) , i)) for i in query.cursor]}
        return jsonify(result)
