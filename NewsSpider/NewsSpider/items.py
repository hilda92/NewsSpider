# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class NewsspiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class SinaNewsItem(scrapy.Item):
    title = scrapy.Field()

    indextext_title = scrapy.Field()
    indextext_link = scrapy.Field()
    indextext_ms = scrapy.Field()
    indextext_time =scrapy.Field()
    textbox = scrapy.Field()
