from typing import Dict

from MySQLdb import Connection, connect
from MySQLdb.cursors import DictCursor, Cursor

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


class Hydrator:

    @staticmethod
    def hydrate(obj: object, row: object, key_relation_alias: object = None) -> object:
        for k, v in obj.__class__.get_fields().items():
            key_relation = "%s.%s" % (key_relation_alias, k)
            if k in row or key_relation in row:
                key_in = k if k in row else key_relation
                setattr(obj, k, row[key_in])
                row.pop(key_in)


class GetFieldsAnnotation:
    @classmethod
    def get_fields(cls) -> Dict:
        return cls.__dict__['__annotations__']