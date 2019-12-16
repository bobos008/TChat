# coding=utf-8

import setting
import tornado.options
from urls import urls
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
    IOLoop.current().start()
