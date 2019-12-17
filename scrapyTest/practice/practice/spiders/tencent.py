# -*- coding: utf-8 -*-
import scrapy
from practice.items import PracticeTenCentItem
import json
import math
from scrapy.http import Request
from urllib import parse
# import time


class TencentSpider(scrapy.Spider):
    name = 'tencent'
    start_urls = [
        'https://careers.tencent.com/tencentcareer/api/post/Query?timestamp=1576564204565&pageIndex=1&pageSize=4132'
    ]
    default_index = 1

    def parse(self, response):
        job = json.loads(response.body)
        if job['Code'] == 200:
            # 总页码
            allPage = math.ceil(job['Data']['Count']/10)
            if job['Data']['Posts']:
                data = job['Data']['Posts']
                for x in data:
                    item = PracticeTenCentItem()
                    Id = x['Id']
                    PostId = x['PostId']
                    RecruitPostId = x['RecruitPostId']
                    RecruitPostName = x['RecruitPostName']
                    CountryName = x['CountryName']
                    LocationName = x['LocationName']
                    BGName = x['BGName']
                    ProductName = x['ProductName']
                    CategoryName = x['CategoryName']
                    Responsibility = x['Responsibility']
                    LastUpdateTime = x['LastUpdateTime']
                    PostURL = x['PostURL']
                    SourceID = x['SourceID']
                    IsCollect = x['IsCollect']
                    IsValid = x['IsValid']
                    item['Id'] = Id
                    item['PostId'] = PostId
                    item['RecruitPostId'] = RecruitPostId
                    item['RecruitPostName'] = RecruitPostName
                    item['CountryName'] = CountryName
                    item['LocationName'] = LocationName
                    item['BGName'] = BGName
                    item['ProductName'] = ProductName
                    item['CategoryName'] = CategoryName
                    item['Responsibility'] = Responsibility
                    item['LastUpdateTime'] = LastUpdateTime
                    item['PostURL'] = PostURL
                    item['SourceID'] = SourceID
                    item['IsCollect'] = IsCollect
                    item['IsValid'] = IsValid
                    yield item
                # 判断写一页是否能抓取
                next_index = self.default_index+1
                if next_index <= allPage:
                    next_url = "https://careers.tencent.com/tencentcareer/api/post/Query?" \
                               "timestamp=1576564204565&pageIndex=" \
                               "%s&pageSize=10" % next_index
                    # time.sleep(10)
                    yield Request(url=parse.urljoin(response.url, next_url), callback=self.parse)
                else:
                    print('页码已达到最大')
            else:
                print('此页无数据')
        else:
            print('请求错误')
