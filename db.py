from MySQLdb import connect, Connection
from MySQLdb.cursors import Cursor, DictCursor
from typing import Dict

DB_CREDENTIALS: Dict = {
    'user': 'root',
    'password': 'root',
    'database': 'son_python_db_api_pratica',
    'host': '127.0.0.1',
    'port': 3306
}


class DB:
    __connection: Connection = None

    # design pattern - singleton
    @staticmethod
    def connect() -> Connection:
        if not DB.__connection:
            DB.__connection = connect(
                user=DB_CREDENTIALS['user'],
                password=DB_CREDENTIALS['password'],
                db=DB_CREDENTIALS['database'],
                host=DB_CREDENTIALS['host'],
                port=DB_CREDENTIALS['port'],
                autocommit=True,
                cursorclass=DictCursor
            )
        return DB.__connection

    @staticmethod
    def cursor() -> Cursor:
        return DB.connect().cursor()
