# coding=utf-8

import time
import redis
from setting import redis_options, redis_pool
from tornado.gen import coroutine
from tornado.web import RequestHandler


class TestHandler(RequestHandler):
    # @coroutine
    def get(self):
        user_list = "userinfo"
        try:
            r = redis.Redis(
                connection_pool=redis_pool,
                # password=redis_options["password"],
                decode_responses=True
            )
        except Exception as error:
            self.write({"error": error})
        user_count = r.llen(user_list)
        userinfo_data = r.lrange(user_list, 0, user_count)
        self.write(userinfo_data[0])


class LoginHandler(RequestHandler):
    @coroutine
    def get(self):
        self.render("login.html")


class RegisterHandler(RequestHandler):
    def get(self):
        self.render("register.html")


class ResetPwdHandler(RequestHandler):
    def get(self):
        self.render("reset-password.html")
