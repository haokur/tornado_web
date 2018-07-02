# coding =utf-8

from utils.common import resolve

from views.modules.app_ui_modules import App_ui_modules

Settings = dict(
    template_path=resolve('views'),
    static_path=resolve('static'),
    ui_modules=App_ui_modules,
    debug=True,
)
