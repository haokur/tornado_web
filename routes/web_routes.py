from controllers.index_ctrl import IndexMainCtrl
from controllers.article_ctrl import ArticleListCtrl

WebRoutes = [
    (r'/', ArticleListCtrl),
    (r'/article/list', ArticleListCtrl)
]
