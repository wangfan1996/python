# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class PracticeTenCentItem(scrapy.Item):
    Id = scrapy.Field()
    PostId = scrapy.Field()
    RecruitPostId = scrapy.Field()
    RecruitPostName = scrapy.Field()
    CountryName = scrapy.Field()
    LocationName = scrapy.Field()
    BGName = scrapy.Field()
    ProductName = scrapy.Field()
    CategoryName = scrapy.Field()
    Responsibility = scrapy.Field()
    LastUpdateTime = scrapy.Field()
    PostURL = scrapy.Field()
    SourceID = scrapy.Field()
    IsCollect = scrapy.Field()
    IsValid = scrapy.Field()
