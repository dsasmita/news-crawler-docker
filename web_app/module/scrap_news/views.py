from flask import Blueprint, jsonify
import datetime
from web_app.module.scrap_news.kompascom import KompasScraping
from web_app.module.scrap_news.kompascom.KompasScraping import KompasScraping

module_scrap_news = Blueprint(
    'module_scrap_news',  # name of module
    __name__,
    template_folder='templates'  # templates folder
)


@module_scrap_news.route('/')
def index():
    return 'This is landing for scrap'


@module_scrap_news.route('/kompas')
def kompas():
    print(datetime.datetime.now())
    kompas = KompasScraping()
    kompas.link_list = "https://indeks.kompas.com/news/2018-06-02"
    result = kompas.generate_content_all_news();
    print(datetime.datetime.now())
    return jsonify(result)
