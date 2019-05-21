import sqlite3
from sqlite3 import Error

class Sqlite:
    def __init__(self, dbfile):
        """ create a database connection to a database that resides
            in the memory
        """
        if (dbfile is None):
            try:
                self.conn = sqlite3.connect(':memory:')
                print(sqlite3.version)
            except Error as e:
                print(e)
        else:
            try:
                self.conn = sqlite3.connect(dbfile)
            except Error as e:
                print(e)
        return None

    def close_connection(self):
        self.conn.close()


    def create_table_models(self):
        """ create a table from the create_table_sql statement
        :param conn: Connection object
        :param create_table_sql: a CREATE TABLE statement
        :return:
        """
        sql_create = """ CREATE TABLE IF NOT EXISTS models (
                                    id integer PRIMARY KEY,
                                    tweet text NOT NULL,
                                    latitude float,
                                    longitude float
                                ); """
        try:
            c = self.conn.cursor()
            c.execute(sql_create)
            self.conn.commit()
        except Error as e:
            print(e)

    def create_table_statistics(self):
        """ create a table from the create_table_sql statement
        :param conn: Connection object
        :param create_table_sql: a CREATE TABLE statement
        :return:
        """
        sql_create = """ CREATE TABLE IF NOT EXISTS stats (
                                    tweet text NOT NULL,
                                    isTI bool,
                                    isGob bool,
                                    isInd bool,
                                    isGeo bool
                                ); """
        try:
            c = self.conn.cursor()
            c.execute(sql_create)
            self.conn.commit()

        except Error as e:
            print(e)            

    def insert_model (self, model):
        sql = ''' INSERT INTO models(tweet,latitude,longitude)
                VALUES(?,?,?) '''
        cur = self.conn.cursor()
        cur.execute(sql, model)
        self.conn.commit()
        return cur.lastrowid
    
    def insert_stat (self, stat):
        sql = ''' INSERT INTO stats(tweet,isTI,isGob,isInd,isGeo)
                VALUES(?,?,?,?,?) '''
        cur = self.conn.cursor()
        cur.execute(sql, stat)
        self.conn.commit()
        return cur.lastrowid

    def selectGeoloc (self):
        cur = self.conn.cursor()
        cur.execute("SELECT * FROM models WHERE latitude IS NOT NULL AND longitude IS NOT NULL")

        rows = cur.fetchall()
        return rows
    
    def selectStats (self):
        cur = self.conn.cursor()
        cur.execute("SELECT * FROM stats")
        rows = cur.fetchall()
        return rows


