# coding=utf-8

import tornado.web
import tornado.gen


class ArticleCtrl():
    def __init__(self):
        print('nothing')


# 文章列表
# @RouterGet('/article/list')
class ArticleListCtrl(tornado.web.RequestHandler):
    @tornado.web.asynchronous
    @tornado.gen.coroutine
    def get(self):
        articles = yield self.application.db.execute(
            "select id,title,description from articles limit 10"
        )
        # for atc in articles:
        #     print(atc)
        self.render(
            'app/index.html',
            articles=articles
        )


# 文章详情
# @RouterGet('/article/read/1')
class ArticleDetailCtrl(tornado.web.RequestHandler):
    def get(self):
        self.write('文章详情页')


# 添加文章
# @RouterPost('/article/add')
class ArticleAddCtrl(tornado.web.RequestHandler):
    def post(self):
        self.write('添加文章')


# 删除文章
# @RouterPost('/article/del/:article_id')
class ArticleDelCtrl(tornado.web.RequestHandler):
    def post(self):
        self.write('删除文章')


# 更新文章
# @RouterPost('/article/update/:article_id')
class ArticleUpdateCtrl(tornado.web.RequestHandler):
    def post(self):
        self.write('更新文章')
