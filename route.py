# coding=utf-8

from login import *
from index import *


urls = [
    (r"/test", TestHandler),
    (r"/", IndexHandler),
    (r"/login", LoginHandler),
    (r"/register", RegisterHandler),
    (r"/resetpwd", ResetPwdHandler),
]
