
import os
import os.path as path
import sys
import pkg_resources 

def create_db_once():
    from bookmanager import db
    db.create_all()
    exit()

    
def find_paths():
    project_dir = os.path.dirname(os.path.abspath(__file__))
    print project_dir
    database_file = "sqlite:///{}".format(os.path.join(project_dir, "bookdatabase.db"))
    print database_file
    
def ch_dir():
    print os.getcwd
    
def get_resources():
    res_dir = os.path.dirname(os.path.abspath(__name__))
    #head, tail = os.path.split(res_dir)
    #head, tail = os.path.split(head)
    print res_dir + os.path.pardir
    #print res_dir
    
    
    
if __name__ == '__main__':
    get_resources()
    
