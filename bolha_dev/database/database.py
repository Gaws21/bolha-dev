#!/usr/bin/python
import logging
import sqlite3

class Sqlite():
    def __init__(self, db='/home/linkedin-python-scrapy-scraper/myjobs.db'):
        self.db = db
        self.conn = sqlite3.connect(self.db, isolation_level=None)
        self.cur = self.conn.cursor()

    def execute_query(self, query):
        try:
            query_execute = self.cur.execute(query)
            query_fetch = query_execute.fetchall()
            if query_fetch:
                return query_fetch
            logging.info("Query run ok ")
        except Exception as err:
            logging.error("Query not run. Error %s", err)
    
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
    
    def insert_values(self, query):
        try:
            self.cur.execute(query)
            self.conn.commit()
            logging.info("Insert Query ok")
        except Exception as err:
            logging.error("Insert Query not run. Error %s", err)

    def insert_many_values(self, data, table_name='LinkedinJobs'):
        try:
            with self.conn:
                self.conn.executemany(f"INSERT INTO {table_name} VALUES(?, ?, ?, ?, ?, ?, ?, ?)", (data))
        except sqlite3.IntegrityError:
            logging.error("couldn't add Python twice")
    
    