import pyodbc
import pandas as pd

class ConnectSQL:
    def __init__(self, server, database, username, password):
        self.server = server
        self.database = database
        self.username = username
        self.password = password
        self.connection = None

    def connect(self):
        try:
            self.connection = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};'
                                             f'SERVER={self.server};'
                                             f'DATABASE={self.database};'
                                             f'UID={self.username};'
                                             f'PWD={self.password}')
            print("Kết nối thành công")
        except Exception as e:
            print("Lỗi khi kết nối đến SQL Server:", e)
    
    def get_data(self, query):
        if self.connection is not None:
            return pd.read_sql(query, self.connection)
        else:
            print("Chưa kết nối tới cơ sở dữ liệu")
            return None

    def close(self):
        if self.connection is not None:
            self.connection.close()
  