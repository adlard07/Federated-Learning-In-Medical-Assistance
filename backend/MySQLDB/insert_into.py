from dataclasses import dataclass 
from MySQLDB.connect_db import ConnectDB
from datetime import date

@dataclass
class PushData:
    def __init__(self):
        self.mydb = ConnectDB()
        self.connection = self.mydb.connect_database()
        self.cursor = self.connection.cursor()
        self.query = "USE federatedsystem;"
        if self.connection.is_connected():
            self.db_Info = self.connection.get_server_info()
            self.cursor.execute(self.query)         
            self.connection.commit()


    def fetch_table(self, role):
        try:
            role = role.lower()
            query = f"SELECT * FROM {role};"
            self.cursor.execute(query)
            table = self.cursor.fetchall()
            # self.connection.close()
            return table
        except Exception as e:
            print(e)


    def create_table(self):
        try:
            query = f'''CREATE TABLE users(user_id int primary key auto_increment, name varchar(40), email varchar(40), password varchar(20));'''
            self.cursor.execute(query)            
            self.connection.commit()
            # self.connection.close()
            print("Table created!")
        except Exception as e:
            print(e)


    def insert_values(self, role, values):
        try:
            role = role.lower()

            self.cursor.execute(f"SELECT * FROM {role}")
            table = self.cursor.fetchall()
            self.connection.commit()

            if list(values)[0] not in [list(ids)[1] for ids in table]:
                query = f"INSERT INTO {role}(name, email, password) VALUES {values};"
                self.cursor.execute(query)           
                self.connection.commit()
                # self.connection.close()
                return "User added!"
            else:
                return "User already exists!"

        except Exception as e:
            print(e)
            return "User was not added!"
        
        
class GraphData:
    def __init__(self):
        self.mydb = ConnectDB()
        self.connection = self.mydb.connect_database()
        self.cursor = self.connection.cursor()
        self.query = "USE federatedsystem;"
        if self.connection.is_connected():
            self.db_Info = self.connection.get_server_info()
            self.cursor.execute(self.query)         
            self.connection.commit()
        self.date = date
        self.days_of_week = {
            0:'Monday',
            1:'Tuesday',
            2:'Wednesday',
            3:'Thursday',
            4:'Friday',
            5:'Saturday',
            6:'Sunday'
            }
            
    
    def fetch_graph_data(self):
        try:
            data_query = f"SELECT * FROM predictions;"
            self.cursor.execute(data_query)
            values = self.cursor.fetchall()
            self.connection.commit()

            column_query = f'SHOW COLUMNS FROM  predictions;'
            self.cursor.execute(column_query)
            columns = [day[0] for day in self.cursor.fetchall()]
            self.connection.commit()

            return (values,columns) 

        except Exception as e:
            print(e)
            
    def insert_graph_data(self, day):
        try:
            today = self.days_of_week.get(day)
            query = f'update predictions set {today} = {today}+1;'
            self.cursor.execute(query)           
            self.connection.commit()
            return "Data inserted successfully."
            
        except Exception as e:
            print(e)
    

if __name__=="__main__":
    db = PushData()
    table = db.create_table()
    message = db.insert_values(values=('example@gmail.com', 'Example@123'))
    print(message)
    table = db.fetch_table()
    print(table)