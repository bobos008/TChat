# coding=utf-8

import pymysql
from setting import mysql_options


class DB(object):
    def __init__(self):
        self.host = mysql_options['host']
        self.database = mysql_options['database']
        self.user = mysql_options['user']
        self.password = mysql_options['password']
        self.charset = mysql_options['charset']

    def connect_db(self):
        db = pymysql.connect(
            self.host,
            self.user,
            self.password,
            self.database,
            charset = self.charset
        )
        return db

    def fetch_one(self):
        """"""
        pass

    def fetch_all(self):
        pass

    def insert_data(self, sql):
        pass

    def delete_data(self):
        pass
