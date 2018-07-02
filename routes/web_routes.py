# coding=utf-8

from controllers.article_ctrl import ArticleListCtrl, ArticleDetailCtrl

WebRoutes = [
    (r'/', ArticleListCtrl),
    (r'/article/list', ArticleListCtrl),
    (r'/article/read/(\w+)', ArticleDetailCtrl)
]
