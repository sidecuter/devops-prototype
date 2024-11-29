import mysql.connector
from mysql.connector import errorcode
from flask import g

class MySQL:
    def __init__(self,app):
        self.app = app
        self.app.teardown_appcontext(self.close_connection) 
    
    def connection(self):
        if 'db' not in g:
            g.db = mysql.connector.connect(**self.config())
            init(g.db)
        return g.db
    
    def config(self):
        return {
            'user': self.app.config['MYSQL_USER'],
            'password': self.app.config['MYSQL_PASSWORD'],
            'host': self.app.config['MYSQL_HOST'],
            'database': self.app.config['MYSQL_DATABASE'],
        }
    
    def close_connection(self, e=None):
        db = g.pop('db', None)
        if db is not None:
            db.close()


TABLES = {
    'data_table': (
        "CREATE TABLE IF NOT EXISTS `data_table` ("
        "  `id` int(11) NOT NULL AUTO_INCREMENT,"
        "  `data` varchar(14) NOT NULL,"
        "  PRIMARY KEY (`id`)"
        ") ENGINE=InnoDB"
    )
}

def init(db):
    cursor = db.cursor()
    for table_name in TABLES:
        table_description = TABLES[table_name]
        try:
            print("Creating table {}: ".format(table_name), end='')
            cursor.execute(table_description)
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
                print("already exists.")
            else:
                print(err.msg)
        else:
            print("OK")

    cursor.close()
