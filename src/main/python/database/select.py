'''
Created on 8 Nov 2017

@author: vinsharm
'''

import utils
# import logging
# logging.basicConfig(level=logging.INFO)
from database.custom_log import Logger


class Select(object):

    def __init__(self):
        # self.logger = logging.getLogger(__name__)
        self.logger = Logger(self.__class__.__name__).get() 
        # self.logger('creating an instance of Class')

    def select_all_tasks(self, conn):
        """
        Query all rows in the tasks table
        :param conn: the Connection object
        :return:
        """
        cur = conn.cursor()
        cur.execute("SELECT * FROM tasks")
     
        rows = cur.fetchall()
     
        for row in rows:
            print(row)
        
        self.table_count(conn)
 
    def select_task_by_priority(self, conn, priority):
        """
        Query tasks by priority
        :param conn: the Connection object
        :param priority:
        :return:
        """
        cur = conn.cursor()
        cur.execute("SELECT * FROM tasks WHERE priority=?", (priority,))
     
        rows = cur.fetchall()
     
        for row in rows:
            print(row)
 
    def table_count(self, conn):
        cur = conn.cursor()
        cur.execute("SELECT Count() FROM tasks")
        numberOfRows = cur.fetchone()[0]
        self.logger.info("Table Count : %s", numberOfRows)
        print(numberOfRows)
    
    def main(self):
        database = "C:\\sqlite\db\pythonsqlite.db"
        self.logger.info("Database name:%s", database)
        # create a database connection
        conn = utils.create_connection(database)
        with conn:
            self.logger.info("1. Query task by priority:")
            print("1. Query task by priority:")
            self.select_task_by_priority(conn, 1)
     
            self.logger.info("2. Query all tasks")
            print("2. Query all tasks")
            self.select_all_tasks(conn)
        
        #self.table_count(conn)    


if __name__ == '__main__':
    select = Select()
    select.main()
    # utils.read_json('D:\\dev\\git\\hadoop-python\\src\\main\\resources\\logging.json')
