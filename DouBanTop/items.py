# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class DoubantopItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    MovieName = scrapy.Field()  # 电影名称
    MovieInfo = scrapy.Field()  # 电影信息
    Star = scrapy.Field()  # 电影评分
    Quote = scrapy.Field()  # 名言引用
    pass
