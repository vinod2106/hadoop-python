'''
Created on 8 Nov 2017

@author: vinsharm
'''
from utils.custom_log import Logger
from utils import utils


class Delete(object):
    '''
    classdocs
    '''

    def __init__(self):
        '''
        Constructor
        '''
        self.logger = Logger(self.__class__.__name__).get()
         
    def delete_task(self, conn, tid):
        """
        Delete a task by task id
        :param conn:  Connection to the SQLite database
        :param id: id of the task
        :return:
        """
        sql = 'DELETE FROM tasks WHERE id=?'
        cur = conn.cursor()
        cur.execute(sql, (tid,))
        
    def delete_all_tasks(self, conn):
        """
        Delete all rows in the tasks table
        :param conn: Connection to the SQLite database
        :return:
        """
        sql = 'DELETE FROM tasks'
        cur = conn.cursor()
        cur.execute(sql)
        
    def main(self):
        database = "C:\\sqlite\db\pythonsqlite.db"
        self.logger.info("database" + database)
        # create a database connection
        conn = utils.create_connection(database)
        with conn:
            # self.delete_task(conn, 2);
            self.logger.info("Deleting all records")
            self.delete_all_tasks(conn);

            
if __name__ == '__main__':
    deltask = Delete()
    deltask.main()
        
