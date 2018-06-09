from flask import Blueprint, jsonify, request
import datetime

from web_app.module.scrap_news.detikcom.DetikScraping import DetikScraping
from web_app.module.scrap_news.kompascom import KompasScraping
from web_app.module.scrap_news.kompascom.KompasScraping import KompasScraping
from web_app.module.scrap_news.models_scrap_news import Portal, Kanal, db_scrap_news, NewsPost


module_scrap_news = Blueprint(
        'module_scrap_news',
        __name__,
        template_folder='templates'
)


@module_scrap_news.route('/')
def index():
    return 'This is landing for scrap'


# kompas
@module_scrap_news.route('/kompas/scrap/list')
def kompas_scrap_list():
    date_scrap = request.args.get('date', datetime.datetime.now().strftime('%Y-%m-%d'))

    print('start ....')
    print(datetime.datetime.now())
    print('......')
    print('......')
    print('......')

    check_kompas = Portal.query.filter_by(title='kompas.com').count()
    if check_kompas == 0:
        return 'news portal kompas not added yet'

    portal = Portal.query.filter_by(title='kompas.com').first()
    kanals = Kanal.query.filter_by(id_portal=portal.id).all()

    kanal_list = []
    for kn in kanals:
        tmp = {}
        tmp['link'] = 'https://indeks.kompas.com/' + kn.title + '/' + date_scrap
        tmp['kanal'] = kn.title
        kanal_list.append(tmp)

    kompas = KompasScraping()
    link_news = kompas.generate_link(kanal_list)

    for link in link_news:
        check = NewsPost.query.filter_by(link_news=link['href']).count()
        if check == 0:
            news = NewsPost()
            news.link_news = link['href']
            news.id_portal = portal.id
            news.title = link['title']
            news.kanal_index = link['kanal']

            db_scrap_news.session.add(news)
            db_scrap_news.session.commit()
        else:
            news = NewsPost.query.filter_by(link_news=link['href']).first()
            if link['kanal'] not in news.kanal_index:
                news.kanal_index = news.kanal_index + ', ' + link['kanal']
                db_scrap_news.session.add(news)
                db_scrap_news.session.commit()

    print('Done')
    print(datetime.datetime.now())
    return str(len(link_news)) + ' news list post scrap from kompas.com'


@module_scrap_news.route('/kompas/category-insert')
def kompas_category_insert():
    check_kompas = Portal.query.filter_by(title='kompas.com').count()
    if check_kompas == 0:
        return 'news portal kompas not added yet'

    portal = Portal.query.filter_by(title='kompas.com').first()

    kompas = KompasScraping()
    kompas.id_news = portal.id
    kompas.link_index = portal.link_index
    kanals = kompas.get_kanal;

    for kn in kanals:
        check_category = Kanal.query.filter_by(slug=kn).count()
        if check_category == 0:
            kanal = Kanal()
            kanal.id_portal = portal.id
            kanal.title = kn
            kanal.slug = kn
            kanal.description = kn

            db_scrap_news.session.add(kanal)
            db_scrap_news.session.commit()

    return 'category inserted'


@module_scrap_news.route('kompas/scrap/detail')
def kompas_scrap_detail():
    limit = request.args.get('limit', 20)

    print('start ....')
    print(datetime.datetime.now())
    print('......')
    print('......')
    print('......')

    news_posts = NewsPost.query.filter_by(scrap_status=False).order_by(NewsPost.id.asc()).limit(limit).all()

    kompas = KompasScraping()

    i = 0
    for news in news_posts:
        print(str(i + 1) + ': ' + str(datetime.datetime.now()))
        print(news.link_news)
        content = kompas.scarp_detail_news(news.link_news)
        news.scrap_status = True

        if content['title'] != '':
            news.title = content['title']

        news.content = content['content']
        news.tags = content['tags']
        news.category = content['category']
        news.category_sub = content['category_sub']

        if content['date_publish'] != '':
            news.date_publish = content['date_publish']

        news.image_link = content['image_link']
        news.image_link_alt = content['image_link_alt']
        news.author = content['author']
        news.editor = content['editor']
        news.source = content['meta_content_source']
        news.meta_description = content['meta_description']
        news.meta_keyword = content['meta_keyword']
        news.meta_content_category = content['meta_content_category']
        news.meta_content_category_sub = content['meta_content_category_sub']
        news.meta_content_location = content['meta_content_location']
        news.meta_content_author = content['meta_content_author']
        news.meta_content_editor = content['meta_content_editor']
        news.meta_content_lipsus = content['meta_content_lipsus']
        news.meta_content_type = content['meta_content_type']

        if content['meta_content_publish_date'] != '':
            news.meta_content_publish_date = content['meta_content_publish_date']

        news.meta_content_source = content['meta_content_source']
        news.meta_content_total_words = content['meta_content_total_words']
        news.meta_content_total_words = content['meta_content_total_words']

        db_scrap_news.session.add(news)
        db_scrap_news.session.commit()

        i = i + 1

    print(str(i) + ' news scarp')
    print('done ....')
    print(datetime.datetime.now())
    return str(i) + ' news scarp'

# Detik
@module_scrap_news.route('/detik/category-insert')
def detik_category_insert():
    check_kompas = Portal.query.filter_by(title='detik.com').count()
    if check_kompas == 0:
        return 'news portal detik not added yet'

    portal = Portal.query.filter_by(title='detik.com').first()

    detik = DetikScraping()
    detik.id_news = portal.id
    detik.link_index = portal.link_index
    kanals = detik.get_kanal

    for kn in kanals:
        # check_category = Kanal.query.filter_by(slug=kn).count()
        print(kn['title'])
        print(kn['slug'])
        # if check_category == 0:
        #     kanal = Kanal()
        #     kanal.id_portal = portal.id
        #     kanal.title = kn
        #     kanal.slug = kn
        #     kanal.description = kn
        #
        #     db_scrap_news.session.add(kanal)
        #     db_scrap_news.session.commit()

    return 'category inserted'