# coding=utf-8

import tornado.web

# 顶部导航条模板
class AppHeaderModule(tornado.web.UIModule):
    def render(self):
        cate = dict(
            catename="Hello"
        )
        return self.render_string('modules/templates/navbar.component.html', cate=cate)


# 侧边栏模板
class AppSideModule(tornado.web.UIModule):
    def render(self):
        return self.render_string('modules/templates/sidebar.component.html')


# 导出所有模块
App_ui_modules = dict({
    'App_header': AppHeaderModule,
    'App_side': AppSideModule
})
