from mysql import connector

class ConnectDB:
    def __init__(self):  
        self.host = "localhost"
        self.user = "root"
        self.password = "adelard"
        self.database = "federatedsystem"
    
    
    def connect_database(self):
        try:
            mydb = connector.connect(
                host = self.host,
                user = self.user,
                password = self.password,
                database = self.database
            )
            print('Database connection Established!')
            return mydb
        except Exception as e:
            print(e)
  
  
if __name__=="__main__":
  mydb = ConnectDB()
  connection = mydb.connect_database()
  