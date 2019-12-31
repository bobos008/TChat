# coding=utf-8

# import time
import json
import redis
from setting import redis_pool
from tornado.gen import coroutine
from tornado.web import RequestHandler


class LoginHandler(RequestHandler):
    @coroutine
    def get(self):
        self.render("login.html")

    @coroutine
    def post(self):
        back_status = True
        back_res = {"res": back_status}
        username = self.get_body_argument("username", default="")
        password = self.get_body_argument("password", default="")

        redis_userinfo_list = "userinfo"
        try:
            redis_conn = redis.Redis(
                connection_pool=redis_pool,
                decode_responses=True
            )
        except Exception as error:
            print(error)
            back_res["res"] = False
            return self.write(back_res)
        user_count = redis_conn.llen(redis_userinfo_list)
        all_user_data = redis_conn.lrange(redis_userinfo_list, 0, user_count)
        for tkey, tuser_data in enumerate(all_user_data):
            user_data = json.loads(tuser_data)
            if "@" in username:
                if user_data["email"] == username and user_data["password"] == password:
                    return self.write(back_res)
            else:
                if user_data["username"] == username and user_data["password"] == password:
                    return self.write(back_res)
            if tkey + 1 == user_count:
                back_res['res'] = False
                return self.write(back_res)


class RegisterHandler(RequestHandler):
    def get(self):
        self.render("register.html")

    def post(self):
        back_status = True
        username = self.get_body_argument("username", default="")
        nickname = self.get_body_argument("nickname", default="")
        email = self.get_body_argument("email", default="")
        password = self.get_body_argument("password", default="")

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
            "username": username,
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
