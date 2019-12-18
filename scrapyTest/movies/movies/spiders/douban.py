# -*- coding: utf-8 -*-
import scrapy
from movies.items import MoviesItem
import re


class DoubanSpider(scrapy.Spider):
    name = 'douban'
    allowed_domains = ['movie.douban.com']
    start = 0
    url = 'https://movie.douban.com/top250?start='
    end = '&filter='
    start_urls = [url + str(start) + end]

    def parse(self, response):
        movies = response.css('li div.item')
        for node in movies:
            item = MoviesItem()
            item['title']= node.css('div.info div.hd a span::text').get()
            item['score'] = node.css('div.info div.bd div.star span.rating_num::text').get()
            item['content'] = node.css('div.info div.bd p::text').get()
            item['info'] = node.css('div.info div.bd p.quote span::text').get()
            evaluate = node.css('div.info div.bd div.star span::text').getall()[1]
            match_re = re.match(".*?(\d+).*", evaluate)
            item['evaluate'] = int(match_re.group(1))
            item['url'] = node.css('div.pic a::attr(href)').get()
            yield item



