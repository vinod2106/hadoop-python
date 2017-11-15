'''
Created on 8 Nov 2017

@author: vinsharm
'''
from utils import utils
from random import randint
from utils.custom_log import Logger
import datetime
import random


class DataInsert(object):

    def __init__(self):
        
        self.logger = Logger(self.__class__.__name__).get() 
        self.logger.info('creating an instance of Class')

    def create_project(self, conn, project):
        """
        Create a new project into the projects table
        :param conn:
        :param project:
        :return: project id
        """
        sql = ''' INSERT INTO projects(name,begin_date,end_date)
                  VALUES(?,?,?) '''
        cur = conn.cursor()
        cur.execute(sql, project)
        return cur.lastrowid
    
    def create_task(self, conn, task):
        """
        Create a new task
        :param conn:
        :param task:
        :return:
        """
      
        sql = ''' INSERT INTO tasks(name,priority,status_id,project_id,begin_date,end_date)
                  VALUES(?,?,?,?,?,?) '''
        cur = conn.cursor()
        cur.execute(sql, task)
        return cur.lastrowid
    
    def insert_data(self, conn, nrows):
        project = ('AppSQLitePython', '2015-01-01', '2015-01-30');
        project_id = self.create_project(conn, project)
        
        # create tasks
        self.logger.info("Inserting records into task table")
        for x in range(nrows):
            # tasks
            d1 = datetime.date(2007, 01, 01)
            d2 = datetime.date(2007, 01, 31)
            sdate = utils.random_date(d1, d2)
            edate = sdate + datetime.timedelta(days=random.randint(1, 11))
            task_1 = ('AnalyzeApp', randint(0, 2), randint(0, 5), project_id, sdate, edate)
            task_2 = ('ConfirmUser', randint(0, 2), randint(0, 5), project_id, sdate, edate)
            self.create_task(conn, task_1)
            self.create_task(conn, task_2)           
    
    def main(self):
        
        database = "C:\\sqlite\db\pythonsqlite.db"
        self.logger.info("database name %s" , database)
     
        # create a database connection
        conn = utils.create_connection(database)
        
        with conn:
            self.insert_data(conn, 100)


if __name__ == '__main__':
    data_in = DataInsert()
    data_in.main()
        
