from sqlalchemy import create_engine
from sqlite3 import Error

from utils.settings import RESOURCES_DIR

 
class Connect():
  
    def db_connect(self):
        try:
            database = 'sqlite:///C:\\sqlite\\db\\chinook.db'
            #database = 'sqlite:///chinook.db' 
            db_connect = create_engine(database, echo=True)
            return db_connect
        except Error as e:
            print(e)
        
        return None

if __name__ == '__main__':
    connect = Connect()
    connect.db_connect() 
    #my_data = pkg_resources.resource_string(__name__, "chinook.db")
     
    #print __loader__.get_data(os.path.join('package_name','README.txt'))         
