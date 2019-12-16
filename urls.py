# coding=utf-8

from login import *
from index import *


urls = [
    (r"/", IndexHandler),
    (r"/login", LoginHandeler),
    (r"/register", RegisterHandler),
    (r"/resetpwd", ResetPwdHandler),
]
