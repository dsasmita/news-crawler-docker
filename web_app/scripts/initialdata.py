import sys, os

sys.path.append(os.getcwd()) # sesuai dengan mark directory

from web_app.app import create_app
from web_app.module.scrap_news.models_scrap_news import Portal, db_scrap_news


app = create_app()

with app.app_context():
    # portal feed
    # kompas
    portal = Portal()
    portal.title = 'kompas.com'
    portal.home_page = 'https://www.kompas.com'
    portal.link_index = 'https://indeks.kompas.com/'

    db_scrap_news.session.add(portal)
    db_scrap_news.session.commit()

    # detik
    portal = Portal()
    portal.title = 'detik.com'
    portal.home_page = 'https://www.kompas.com'
    portal.link_index = 'https://indeks.kompas.com/'

    db_scrap_news.session.add(portal)
    db_scrap_news.session.commit()

