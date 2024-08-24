from abc import ABC, abstractmethod

class Singleton(type):
    _instances = {} 

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances: 
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class DBConnection(metaclass=Singleton):
    @abstractmethod
    def create(self): 
        pass

class MySQLConnection(DBConnection):
    def __init__(self, port, db_name, table_name):
        self.port = port 
        self.db_name = db_name
        self.table_name = table_name
    def create(): 
        print("Creating mysql db")

class PostgreSQLConnection(DBConnection):
    def __init__(self, port, db_name, table_name):
        self.port = port 
        self.db_name = db_name, 
        self.table_name = table_name
    def create(): 
        print("Creating Pg db")

class MongoDBConnection(DBConnection):
    def __init__(self, port, db_name, collection_name):
        self.port = port 
        self.db_name = db_name
        self.collection_name = collection_name
    def create(): 
        print("Creating mongo db")

class DBFactory(ABC):
    @abstractmethod
    def create(**kwargs): 
        pass

class MySQLConnectionFactory(DBFactory):
    @staticmethod
    def create(**kwargs): 
        print(kwargs)
        return MySQLConnection(kwargs["port"], kwargs["db_name"], kwargs["table_name"])

class PostgreSQLConnectionFactory(DBFactory):
    @staticmethod
    def create(**kwargs): 
        return PostgreSQLConnection(kwargs["port"], kwargs["db_name"], kwargs["table_name"])

class MongoDBConnectionFactory(DBFactory):
    @staticmethod
    def create(**kwargs): 
        print("Called mongodb factory")
        return MongoDBConnection(kwargs["port"], kwargs["db_name"], kwargs["collection_name"])


input_data = {
    "port": 3306,
    "db_name": "test_db",
    "table_name": "test_table"
}

# Creating MySQL connection
db_connection1 = MySQLConnectionFactory.create(**input_data)
db_connection2 = MySQLConnectionFactory.create(**input_data)
db_connection3 = PostgreSQLConnectionFactory.create(**input_data)

print(db_connection1 is db_connection2)    
print(db_connection1 is db_connection3)   