# coding=utf-8

import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
import tornado.httpclient

from tornado.options import define, options

define('port', default=8000, help='run on the given port', type=int)

# 路由配置
from routes.web_routes import WebRoutes

# 全局部分参数及变量配置
from config.settings import Settings

import databases


class Application(tornado.web.Application):
    def __init__(self):
        tornado.web.Application.__init__(self, WebRoutes, **Settings)
        # 将连接的数据库实例挂载在 app 上,外部可通过 self.application.db 访问
        self.db = databases.get_mysql_instance()


# 程序入口
def main():
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(Application())
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
