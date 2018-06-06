from flask import Blueprint, jsonify
import datetime
from web_app.module.scrap_news.kompascom import KompasScraping
from web_app.module.scrap_news.kompascom.KompasScraping import KompasScraping
from web_app.module.scrap_news.models_scrap_news import Portal, Kanal, db_scrap_news

module_scrap_news = Blueprint(
    'module_scrap_news',  # name of module
    __name__,
    template_folder='templates'  # templates folder
)


@module_scrap_news.route('/')
def index():
    return 'This is landing for scrap'

# kompas
@module_scrap_news.route('/kompas/scrap/list')
def kompas_scrap_list():
    check_kompas = Portal.query.filter_by(title='kompas.com').count()
    if check_kompas == 0:
        return 'news portal kompas not added yet'

    portal = Portal.query.filter_by(title = 'kompas.com').first()
    kanals = Kanal.query.filter_by(id_portal = portal.id).all()

    kanal_list = []
    for kn in kanals:
        tmp = {}
        tmp['link'] = 'https://indeks.kompas.com/' + kn.title +'/2018-06-06'
        tmp['kanal'] = kn.title
        kanal_list.append(tmp)

    kompas = KompasScraping()
    link_news = kompas.generate_link(kanal_list)

    return len(link_news) + 'news list post scrap from kompas.com'

@module_scrap_news.route('/kompas/category-insert')
def kompas_category_insert():
    check_kompas = Portal.query.filter_by(title = 'kompas.com').count()
    if check_kompas == 0:
        return 'news portal kompas not added yet'

    portal = Portal.query.filter_by(title = 'kompas.com').first()

    kompas = KompasScraping()
    kompas.id_news = portal.id
    kompas.link_index = portal.link_index
    kanals = kompas.get_kanal();

    for kn in kanals:
        check_category = Kanal.query.filter_by(slug = kn).count()
        if check_category == 0:
            kanal = Kanal()
            kanal.id_portal = portal.id
            kanal.title = kn
            kanal.slug = kn
            kanal.description = kn

            db_scrap_news.session.add(kanal)
            db_scrap_news.session.commit()

    return 'category inserted'
