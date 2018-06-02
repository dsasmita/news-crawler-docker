from flask import Blueprint, jsonify

from web_app.module.scrap_news.kompascom import KompasScraping
from web_app.module.scrap_news.kompascom.KompasScraping import KompasScraping

module_scrap_news = Blueprint(
    'module_scrap_news', #name of module
    __name__,
    template_folder='templates' # templates folder
)
@module_scrap_news.route('/')
def index():
    return 'This is landing for scrap'

@module_scrap_news.route('/kompas')
def kompas():
    kompas = KompasScraping()
    kompas.link_list = "https://indeks.kompas.com/news/2018-06-01"
    result = kompas.scarp_detail_news('http://internasional.kompas.com/read/2018/06/01/23590011/survei--rakyat-korsel-mulai-mengidolakan-trump-dan-kim-jong-un')
    # return jsonify(result)
    return 'kompas scrap'