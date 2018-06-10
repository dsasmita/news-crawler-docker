# -*- coding: utf-8 -*-
from imp import reload

import bs4
import requests

import sys

reload(sys)
sys.setdefaultencoding('utf-8')


class DetikScraping:
    def __init__(self):
        self.id_news = 0  # id news
        self.link_index = ''  # indeks link
        self.link_list = ''  # indeks want to scarp

    def generate_index(self, link_list):
        if link_list['link'] == '':
            return 'link_list not specified'

        url_pagination = []

        if (link_list['type'] == 'GET'):
            content = requests.get(link_list['link'], timeout=10)
            bs = bs4.BeautifulSoup(content.text, "html.parser")

            pagination = bs.find('div', 'paging')
            last_page = 1
            if (pagination != None):
                for page in pagination.select('a'):
                    number = page.get_text().replace('Â»', '')
                    number = number.strip()
                    if (self.is_number(number)):
                        last_page = self.cast_to_int(number)

                for i in range(1, last_page):
                    tmp = {}
                    tmp['link'] = "%s/all/%s?date=%s" % (link_list['link_ori'], i, link_list['date'])
                    tmp['date'] = link_list['date']
                    tmp['type'] = link_list['type']
                    url_pagination.append(tmp)
            else:
                tmp = {}
                tmp['link'] = link_list['link']
                tmp['date'] = link_list['date']
                tmp['type'] = link_list['type']
                url_pagination.append(tmp)
        else:
            tmp = {}
            tmp['link'] = link_list['link_ori']
            tmp['date'] = link_list['date']
            tmp['type'] = link_list['type']
            url_pagination.append(tmp)

        return url_pagination;

    def generate_link(self, link_list):
        news_link = []
        for lk in link_list:
            url_pagination = self.generate_index(lk)

            for url in url_pagination:
                if url['type'] == 'GET':
                    print(url['link'])
                    content = requests.get(url['link'], timeout=10)
                    response = bs4.BeautifulSoup(content.text, "html.parser")
                    list_array = response.find("ul", {"id": "indeks-container"})

                    if list_array != None:
                        if len(list_array) > 0:
                            for link in list_array.select('article'):
                                print(link.get_text())
                                tmp = {}
                                tmp['href'] = link['href']
                                tmp['title'] = link.get_text()
                                tmp['kanal'] = lk['kanal']
                                news_link.append(tmp)
                    else:
                        list_array = response.find_all("ul", "list")
                        print(list_array)


                else:
                    print('POST')
        return news_link

    def generate_content_all_news(self):
        return 'list'

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
            slug = slug.replace("https://", '')
            slug = slug.replace("//", "")

            tmp = {}
            tmp['title'] = title
            tmp['slug'] = slug
            categories.append(tmp)

        return categories

    def scarp_detail_news(self, news_link):
        return 'detail'

    def is_number(self, s):
        try:
            return float(s)
        except ValueError:
            return False

    def cast_to_int(self, s):
        try:
            return int(s)
        except ValueError:
            return False
