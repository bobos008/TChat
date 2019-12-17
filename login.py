# coding=utf-8

import time
from pymysql.cursors import DictCursor
from db_class import DB
from tornado.web import RequestHandler


class TestHandler(RequestHandler):
    def get(self):
        db_obj = DB()
        db = db_obj.connect_db()
        time.sleep(150)
        print("------:", db.ping())
        sql = "select * from userinfo;"
        cursor = db.cursor(DictCursor)
        cursor.execute(sql)
        result = cursor.fetchone()
        self.write(result)
        db.close()


class LoginHandler(RequestHandler):
    def get(self):
        self.render("login.html")


class RegisterHandler(RequestHandler):
    def get(self):
        self.render("register.html")


class ResetPwdHandler(RequestHandler):
    def get(self):
        self.render("reset-password.html")
