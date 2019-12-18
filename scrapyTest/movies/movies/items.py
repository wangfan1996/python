# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class MoviesItem(scrapy.Item):
    title = scrapy.Field()
    score = scrapy.Field()
    content = scrapy.Field()
    info = scrapy.Field()
    evaluate = scrapy.Field()
    url = scrapy.Field()

