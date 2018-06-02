import datetime
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, DateTime, BigInteger, Text

db_scrapt_news = SQLAlchemy()


class Page(db_scrapt_news.Model):
    __tablename__ = 'master_news_post'
    id = Column(BigInteger, primary_key=True)
    title = Column(Text)
    content = Column(Text)
    tags = Column(Text)
    category = Column(Text)
    category_sub = Column(Text)
    breadcrumb = Column(Text)
    date_publish = Column(DateTime, default=datetime.datetime.utcnow)
    image_link = Column(Text)
    author = Column(Text)
    meta_description = Column(Text)
    meta_keyword = Column(Text)
    meta_content_category = Column(Text)
    meta_content_category_sub = Column(Text)
    meta_content_location = Column(Text)
    meta_content_author = Column(Text)
    meta_content_editor = Column(Text)
    meta_content_lipsus = Column(Text)
    meta_content_type = Column(Text)
    meta_content_publish_date = Column(DateTime, default=datetime.datetime.utcnow)
    meta_content_source = Column(Text)
    meta_content_tag = Column(Text)
    meta_content_total_words = Column(Text)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.datetime.utcnow)

