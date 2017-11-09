'''
Created on 9 Nov 2017

@author: vinsharm
'''
from flask import Flask
from flask_restful import Api
from tracks import Tracks
from employees import Employees
from employee_name import Employee_Name


database = 'sqlite:///C:\\sqlite\\db\\chinook.db'
app = Flask(__name__)
api = Api(app)
api.add_resource(Employees, '/employees')  # Route_1
api.add_resource(Tracks, '/tracks')  # Route_2
api.add_resource(Employee_Name, '/employees/<employee_id>')  # Route_3

if __name__ == '__main__':
    app.run(port='5002')
    
