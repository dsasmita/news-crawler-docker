from _sitebuiltins import _Printer

import bs4
import requests

class KompasScraping:
    def __init__(self):
        self.link_list = ''
        self.link_detail = ''

    def generate_index(self):
        content = requests.get(self.link_list)
        bs = bs4.BeautifulSoup(content.text, "html.parser")

        index = [item['data-ci-pagination-page']
                 for item in bs.find_all('a', attrs={'data-ci-pagination-page': True})]
        lastPage = int(index[len(index) - 1]) + 1

        url_pagination = []
        for i in range(1, lastPage):
            url_pagination.append("%s/%s" % (self.link_list, i))

        return url_pagination;

    def generate_link(self):
        url_pagination = self.generate_index()

        news_link = []
        for url in url_pagination:
            content = requests.get(url)
            response = bs4.BeautifulSoup(content.text, "html.parser")
            list_link = response.find_all('a', 'article__link')

            for link in list_link:
                news_link.append(link["href"])

        return news_link

    def scarp_detail_news(self, news_link):
        content = requests.get(news_link)
        response = bs4.BeautifulSoup(content.text, "html.parser")

        news = {}
        # title
        news["title"] = response.find('h1','read__title').get_text()

        # content
        content_news = response.find('div', 'read__content')
        paragraf_news = []
        for paragraf in content_news.select('p'):
            check = True
            if paragraf.get_text().find('Baca juga') != -1:
                check = False

            if check and paragraf.get_text().strip() != "":
                paragraf_news.append(paragraf.get_text().strip())

        _Printer(pa)


        return 'news detail'
