'''
Created on 8 Nov 2017

@author: vinsharm
'''
from database.custom_log import Logger
from select import  Select
from database.delete import Delete
from insert import DataInsert
import utils


class CustomClass(object):

    def __init__(self):
        self.logger = Logger(self.__class__.__name__).get()  # accessing the "private" variables for each class
        database = "C:\\sqlite\db\pythonsqlite.db"
        self.logger.info("Database name:%s", database)
        self.conn = utils.create_connection(database)
        self.select = Select()
        self.insert = DataInsert()
        self.delete = Delete()
        
    def insertData(self, conn):
        self.logger.info("Insert query")
        self.insert.insert_data(conn, 200)

    def deleteData(self, conn):
        self.logger.info("Delete query")
        self.delete.delete_all_tasks(conn)
    
    def selectData(self, conn):
        self.logger.info("Select query")
        self.select.select_all_tasks(conn)
    
            
    def main(self):
        #self.deleteData(self.conn)
        self.insertData(self.conn)
        self.selectData(self.conn)
        
if __name__ == '__main__':
    cc = CustomClass()
    cc.main()
    
