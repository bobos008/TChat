# coding=utf-8

from tornado.web import RequestHandler


class LoginHandeler(RequestHandler):
    def get(self):
        self.render("login.html")


class RegisterHandler(RequestHandler):
    def get(self):
        self.render("register.html")


class ResetPwdHandler(RequestHandler):
    def get(self):
        self.render("reset-password.html")
