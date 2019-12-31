# coding=utf-8

import time
import json
import redis
from setting import redis_pool
from tornado.gen import coroutine
from tornado.web import RequestHandler


class TestHandler(RequestHandler):
    @coroutine
    def get(self):
        user_list = "userinfo"
        try:
            r = redis.Redis(
                connection_pool=redis_pool,
                decode_responses=True
            )
        except Exception as error:
            print("error:", error)
            return self.write({"error": "this is error"})
        user_count = r.llen(user_list)
        userinfo_data = r.lrange(user_list, 0, user_count)
        self.write(userinfo_data[0])


class LoginHandler(RequestHandler):
    @coroutine
    def get(self):
        self.render("login.html")
    @coroutine
    def post(self):
        back_status = True
        username = self.get_body_argument("username", default=None)
        password = self.get_body_argument("password", default=None)

        redis_userinfo_list = "userinfo"
        try:
            redis_conn = redis.Redis(
                connection_pool=redis_pool,
                decode_responses=True
            )
        except Exception as error:
            print(error)
        user_count = redis_conn.llen(redis_userinfo_list)



class RegisterHandler(RequestHandler):
    def get(self):
        self.render("register.html")
    def post(self):
        back_status = True
        username = self.get_body_argument("username", default=None)
        nickname = self.get_body_argument("nickname", default=None)
        email = self.get_body_argument("email", default=None)
        password = self.get_body_argument("password", default=None)

        redis_userinfo_list = "userinfo"
        try:
            redis_conn = redis.Redis(
                connection_pool=redis_pool,
                decode_responses=True
            )
        except Exception as error:
            print(error)
            return self.write({"res": False})
        user_count = redis_conn.llen(redis_userinfo_list)
        new_user = {
            "id": user_count + 1,
            "user": username,
            "nickname": nickname,
            "email": email,
            "password": password
        }
        end_res = redis_conn.rpush(redis_userinfo_list, json.dumps(new_user))
        if end_res <= user_count:
            back_status = False
        redis_conn.close()
        result = {"res": back_status}
        return self.write(result)


class ResetPwdHandler(RequestHandler):
    def get(self):
        self.render("reset-password.html")
