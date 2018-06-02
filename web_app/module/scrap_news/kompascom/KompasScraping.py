import datetime
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

    def generate_content_all_news(self):
        news_list_link = self.generate_link()
        news = []
        for link in news_list_link:
            print(link)
            news.append(self.scarp_detail_news(link))

        return news

    def scarp_detail_news(self, news_link):
        content = requests.get(news_link)
        response = bs4.BeautifulSoup(content.text, "html.parser")

        news = {}
        # title
        news["title"] = response.find('h1','read__title').get_text()

        # content
        contens = response.find('div', 'read__content')
        tmp_paragraf_news = []
        for paragraf in contens.select('p'):
            check = True
            if paragraf.get_text().find('Baca juga') != -1:
                check = False

            if check and paragraf.get_text().strip() != "":
                tmp_paragraf_news.append('<p>%s</p>' %(paragraf.get_text().strip()))

        news["content"] = ' '.join(tmp_paragraf_news)

        # tags
        tags = response.find('ul', 'tag__article__wrap')
        tmp_tags_array = []
        for tag in tags.select('li'):
            tmp_tags_array.append(tag.get_text().strip())

        news['tags'] = ', '.join(tmp_tags_array)

        # category
        categories = response.find('ul', 'breadcrumb__wrap')
        tmp_category_array = []
        for category in categories.select("li"):
            if category.get_text().strip() != 'Home':
                tmp_category_array.append(category.get_text().strip())

        try:
            news['category'] = tmp_category_array[0]
        except:
            news['category'] = 'empty'

        try:
            news['category_sub'] = tmp_category_array[1]
        except:
            news['category_sub'] = 'empty'

        # date_publish
        date_time = response.find('div', 'read__time').get_text()
        date_before_format = date_time.replace('Kompas.com - ', '')
        date_time_array = date_before_format.split(',')
        date_array = date_time_array[0].split('/')
        time_array = date_time_array[1].split(' ')
        news['date_publish'] =  '%s-%s-%s %s' % (date_array[2], date_array[1], date_array[0], time_array[1])

        # image_link
        photos = response.find('div','photo')
        news['image_link'] = photos.img['src']
        news['image_link_alt'] = photos.img['alt']

        # author
        author = response.find('div', {'id' : 'penulis'})
        try:
            news['author'] = author.a.get_text()
        except:
            news['author'] = 'empty'

        # editor
        editor = response.find('div', {'id': 'editor'})
        news['editor'] = editor.a.get_text()

        # meta data
        metas = response.find_all('meta')
        for meta in metas:
            if 'name' in meta.attrs:
                if meta.attrs['name'] == 'description':
                    news['meta_description'] = meta.attrs['content']
                elif meta.attrs['name'] == 'content_category':
                    news['meta_content_category'] = meta.attrs['content']
                elif meta.attrs['name'] == 'content_category_sub':
                    news['meta_content_category_sub'] = meta.attrs['content']
                elif meta.attrs['name'] == 'content_location':
                    news['meta_content_location'] = meta.attrs['content']
                elif meta.attrs['name'] == 'content_author':
                    news['meta_content_author'] = meta.attrs['content']
                elif meta.attrs['name'] == 'content_editor':
                    news['meta_content_editor'] = meta.attrs['content']
                elif meta.attrs['name'] == 'content_lipsus':
                    news['meta_content_lipsus'] = meta.attrs['content']
                elif meta.attrs['name'] == 'content_type':
                    news['meta_content_type'] = meta.attrs['content']
                elif meta.attrs['name'] == 'content_publish_date':
                    news['meta_content_publish_date'] = meta.attrs['content']
                elif meta.attrs['name'] == 'content_source':
                    news['meta_content_source'] = meta.attrs['content']
                elif meta.attrs['name'] == 'content_tag':
                    news['meta_content_tag'] = meta.attrs['content']
                elif meta.attrs['name'] == 'content_total_words':
                    news['meta_content_total_words'] = meta.attrs['content']
                elif meta.attrs['name'] == 'content_PublishedDate':
                    news['meta_content_publish_date'] = meta.attrs['content']

        news['created_at'] = datetime.datetime.now().strftime('%Y-%m-%d %H:%M')
        news['updated_at'] = datetime.datetime.now().strftime('%Y-%m-%d %H:%M')

        return news
