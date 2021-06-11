# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class CrawlerItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    
    is_sarcastic = scrapy.Field()
    headline = scrapy.Feld()
    article_link = scrapy.Field()
    time = scrapy.Field()

    pass
