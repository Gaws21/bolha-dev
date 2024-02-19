#!/usr/bin/python
import logging
import sqlite3
from app.config import Config

class Sqlite():
    def __init__(self, db=Config.SQLALCHEMY_DATABASE_URI):
        self.db = db
        self.conn = sqlite3.connect(self.db, isolation_level=None)
        self.cur = self.conn.cursor()
    
    def execute_query_by_path(self, path):
        try:
            query_execute = None
            query_fetch = None
            with open(path, 'r') as sql_file:
                query_execute = self.cur.execute(sql_file.read())
                query_fetch = query_execute.fetchall()
            
            if query_fetch:
                return query_fetch
            logging.info("Query run ok ")
        except Exception as err:
            logging.error("Query not run. Error %s", err)
    
    
    