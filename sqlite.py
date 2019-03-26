import sqlite3
from sqlite3 import Error
 
def create_connection():
    """ create a database connection to a database that resides
        in the memory
    """
    try:
        conn = sqlite3.connect(':memory:')
        print(sqlite3.version)
        return conn
    except Error as e:
        print(e)
    return None

def close_connection(conn):
    conn.close()


def create_table_models(conn):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    sql_create = """ CREATE TABLE IF NOT EXISTS models (
                                id integer PRIMARY KEY,
                                tweet text NOT NULL,
                                latitude decimal,
                                longitude decimal
                            ); """
    try:
        c = conn.cursor()
        c.execute(sql_create)
        print ("DB opened")
    except Error as e:
        print(e)

def insert_row (conn, model):
    sql = ''' INSERT INTO models(tweet,latitude,longitude)
            VALUES(?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, model)
    return cur.lastrowid

def selectAll (conn):
    cur = conn.cursor()
    cur.execute("SELECT * FROM models")

    rows = cur.fetchall()

    for row in rows:
        print(row)


