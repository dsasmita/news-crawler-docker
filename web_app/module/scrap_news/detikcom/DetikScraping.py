# -*- coding: utf-8 -*-
import bs4
import requests


class DetikScraping:
    def __init__(self):
        self.id_news = 0 # id news
        self.link_index = '' # indeks link
        self.link_list = '' # indeks want to scarp

    def generate_index(self, link_list):
        if link_list == '':
            return 'link_list not specified'
        return 'url_pagination';

    def generate_link(self, link_list):
        return link_list

    def generate_content_all_news(self):
        return 'list'

    @property
    def get_kanal(self):
        link_index = self.link_index
        categories = []
        if link_index == '':
            return categories

        content = requests.get(link_index, timeout=10)
        response = bs4.BeautifulSoup(content.text, "html.parser")

        categories_container = response.find('div', 'menu_idx')
        for cat_option in categories_container.select('a'):
            title = cat_option.get_text()
            title = title.replace("» ", "")
            slug = cat_option['href']
            slug = slug.replace("https://",'')
            slug = slug.replace("//", "")

            tmp = {}
            tmp['title'] = title
            tmp['slug'] = slug
            categories.append(tmp)

        return categories

    def scarp_detail_news(self, news_link):
        return 'detail'
