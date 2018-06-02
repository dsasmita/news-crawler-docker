from flask import Flask

from web_app.module.home.view import module_home
from web_app.module.scrap_news.models_scrap_news import db_scrapt_news
from web_app.module.scrap_news.views import module_scrap_news


def create_app():
    app = Flask(__name__)
    # setup config
    app.config.from_pyfile('settings.py')

    # register module
    app.register_blueprint(module_home, url_prefix="/")
    app.register_blueprint(module_scrap_news, url_prefix="/scrap")

    # register model
    db_scrapt_news.init_app(app)


    return app