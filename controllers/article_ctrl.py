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
        sql_key = [
            'id',
            'title',
            'description',
            'created_at',
            'category_id',
            'author_id',
            'views_num'
        ]
        sql_key_str = ','.join(sql_key)
        sql_key_str = "select " + sql_key_str + " from articles limit 10"
        articles = yield self.application.db.execute(sql_key_str)
        self.render(
            'app/index.html',
            articles=articles
        )


# 文章详情
# @RouterGet('/article/read/1')
class ArticleDetailCtrl(tornado.web.RequestHandler):
    @tornado.web.asynchronous
    @tornado.gen.coroutine
    def get(self, input):
        article_id = input[::-1]
        query_article_sql = "select * from articles where id=" + article_id
        queryed_article = yield self.application.db.execute(query_article_sql)
        article_info = ()
        for val in queryed_article:
            article_info = val
        self.render(
            'app/article_detail.html',
            article_info=article_info
        )


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
