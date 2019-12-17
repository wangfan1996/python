# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class BookItem(scrapy.Item):
    title = scrapy.Field()
    url = scrapy.Field()
    author = scrapy.Field()
    description = scrapy.Field()
    img_src = scrapy.Field()
    image_path = scrapy.Field()
    create_date = scrapy.Field()
    url_object_id = scrapy.Field()
