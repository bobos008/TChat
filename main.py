# coding=utf-8

import time
import setting
import tornado.options
from route import urls
from tornado.web import Application
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
from tornado.options import options, define


define("port", default=9000, type=int, help="服务器的端口！")


if __name__ == "__main__":
    tornado.options.parse_command_line()
    app = Application(urls, **setting.settings)
    http_server = HTTPServer(app)
    http_server.listen(options.port)
    # http_server.bind(options.port)
    # http_server.start(0)
    IOLoop.current().start()
