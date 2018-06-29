# coding=utf-8

import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
import tornado.httpclient

from tornado.options import define, options

define('port', default=8000, help='run on the given port', type=int)

from routes.web_routes import WebRoutes
from config.settings import Settings


class Application(tornado.web.Application):
    def __init__(self):
        tornado.web.Application.__init__(self, WebRoutes, **Settings)


# 程序入口
def main():
    print(__file__)
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(Application())
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
