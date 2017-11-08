'''
Created on 8 Nov 2017

@author: vinsharm
'''
import utils
import logging
logging.basicConfig(level=logging.INFO)

class DataInsert(object):

    def __init__(self):
        
        self.logger = logging.getLogger(__name__)
        self.logger.info('creating an instance of Class')

    def create_project(self, conn, project):
        """
        Create a new project into the projects table
        :param conn:
        :param project:
        :return: project id
        """
        self.logger.info("Inside create_project ")
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
        self.logger.info("Inside create_task ")
        
        sql = ''' INSERT INTO tasks(name,priority,status_id,project_id,begin_date,end_date)
                  VALUES(?,?,?,?,?,?) '''
        cur = conn.cursor()
        cur.execute(sql, task)
        return cur.lastrowid
    
    def main(self):
        
        database = "C:\\sqlite\db\pythonsqlite.db"
        self.logger.info("database name %s" , database)
     
        # create a database connection
        conn = utils.create_connection(database)
        
        with conn:
            # create a new project
            project = ('Cool App with SQLite & Python', '2015-01-01', '2015-01-30');
            project_id = self.create_project(conn, project)
     
            # tasks
            task_1 = ('Analyze the requirements of the app', 1, 1, project_id, '2015-01-01', '2015-01-02')
            task_2 = ('Confirm with user about the top requirements', 1, 1, project_id, '2015-01-03', '2015-01-05')
     
            # create tasks
            self.logger.info("Creating task")
            self.create_task(conn, task_1)
            self.create_task(conn, task_2)


if __name__ == '__main__':
    data_in = DataInsert()
    data_in.main()
        
