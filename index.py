# coding=utf-8

import json
import redis
from tornado.web import RequestHandler
from tornado.gen import coroutine
from setting import redis_pool


class IndexHandler(RequestHandler):
    @coroutine
    def get(self):
        user_id = 1
        try:
            redis_conn = redis.Redis(
                connection_pool=redis_pool,
                decode_responses=True
            )
        except Exception as error:
            self.write("<h2>Server error, Please ask again later!</h2>")
            return self.set_status(500, "db connection error!")
        friends_list = "user_of_friends"
        friends_count = redis_conn.llen(friends_list)
        friends_data = redis_conn.lrange(friends_list, 0, friends_count)
        for tkey, tfriend in enumerate(friends_data):
            tfriend_data = json.loads(tfriend)
            if tfriend_data["uid"] == user_id:
                friends = json.loads(tfriend_data["friends"])
                break
            if tkey + 1 == friends_count:
                self.write("<h2>Server error, Please ask again later!</h2>")
                return self.set_status(500, "db connection error!")

        user_list = "userinfo"
        user_count = redis_conn.llen(user_list)
        all_user_data = redis_conn.lrange(user_list, 0, user_count)
        curr_user_friend = list()
        for tuser in all_user_data:
            user_data = json.loads(tuser)
            if user_data["id"] in friends:
                curr_user_friend.append(user_data)
        redis_conn.close()
        return self.render("index.html", user_friend=curr_user_friend)
