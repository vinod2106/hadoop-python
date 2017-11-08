'''
Created on 8 Nov 2017

@author: vinsharm
'''

import utils
import logging
logging.basicConfig(level=logging.INFO)


class Select(object):

    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.logger.info('creating an instance of Class')

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
 
    def main(self):
        database = "C:\\sqlite\db\pythonsqlite.db"
     
        # create a database connection
        conn = utils.create_connection(database)
        with conn:
            self.logger.info("1. Query task by priority:")
            print("1. Query task by priority:")
            self.select_task_by_priority(conn, 1)
     
            self.logger.info("2. Query all tasks")
            print("2. Query all tasks")
            self.select_all_tasks(conn)
     

if __name__ == '__main__':
    select = Select()
    #select.main()
    utils.read_json('D:\\dev\\git\\hadoop-python\\src\\main\\resources\\logging.json')
