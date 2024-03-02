import pandas as pd
import sqlalchemy
class ConnectSQLAlChemy:
    def __init__(self, server, database, username, password):
        self.server = server
        self.database = database
        self.username = username
        self.password = password        
        self.engine = None

    def connect(self):
        try:
            driver = 'ODBC Driver 17 for SQL Server'
            self.engine = sqlalchemy.create_engine(f'mssql+pyodbc://{self.username}:{self.password}@{self.server}/{self.database}?driver={driver}')
            print("Kết nối thành công")
        except Exception as e:
            print("Lỗi khi kết nối đến SQL Server:", e)

    def get_data(self, query):
        return pd.read_sql(query, self.engine)

    def close(self):
        self.engine.dispose()

