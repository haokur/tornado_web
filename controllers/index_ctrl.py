# coding=utf-8

import tornado.web

# @routerGet('/')
class IndexCtrl(tornado.web.RequestHandler):
    def get(self):
        self.render('app/index.html')
