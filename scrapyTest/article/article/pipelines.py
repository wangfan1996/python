# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
from pymysql import cursors
from twisted.enterprise import adbapi
import time
from scrapy.pipelines.images import ImagesPipeline
from article.utils.common import get_md5
from scrapy.utils.project import get_project_settings
import scrapy


class BookPipeline(object):
    def __init__(self, db_pool):
        self.db_pool = db_pool

    @classmethod
    def from_settings(cls, settings):
        """类方法，只加载一次，数据库初始化"""
        db_params = dict(
            host=settings['MYSQL_HOST'],
            user=settings['MYSQL_USER'],
            password=settings['MYSQL_PASSWORD'],
            port=settings['MYSQL_PORT'],
            database=settings['MYSQL_DBNAME'],
            charset=settings['MYSQL_CHARSET'],
            use_unicode=True,
            # 设置游标类型
            cursorclass=cursors.DictCursor
        )
        # 创建连接池
        db_pool = adbapi.ConnectionPool('pymysql', **db_params)
        # 返回一个pipeline对象
        return cls(db_pool)

    def process_item(self, item, spider):
        myItem = {}
        myItem["title"] = item["title"]
        myItem["url"] = item["url"]
        myItem["author"] = item["author"]
        myItem["description"] = item["description"]
        myItem["img_src"] = item["img_src"]
        myItem['create_date'] = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        myItem['url_object_id'] = get_md5(item["url"])
        myItem['image_path'] = item['image_path']
        # 把要执行的sql放入连接池
        query = self.db_pool.runInteraction(self.insert_into, myItem)
        # 如果sql执行发送错误,自动回调addErrBack()函数
        query.addErrback(self.handle_error, myItem, spider)
        return myItem

    # 处理sql函数
    def insert_into(self, cursor, item):
        # 创建sql语句
        sql = """
        INSERT INTO books(title, url, author, description, img_src, image_path, url_object_id, create_date, is_have)
        VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        # 执行sql语句
        cursor.execute(sql, (item['title'], item['url'], item['author'], item['description'], item['img_src'], item['image_path'], item['url_object_id'], item['create_date'], 1))

    # 错误函数
    def handle_error(self, failure, item, spider):
        print("failure", failure)


class BookImagePipeline(ImagesPipeline):
    # 获取settings文件里设置的变量值 IMAGES_STORE 也就是下载的图片保存的地址
    IMAGES_STORE = get_project_settings().get('IMAGES_STORE')

    def get_media_requests(self, item, info):
        img_src = item['img_src']
        yield scrapy.Request(img_src)

    def item_completed(self, results, item, info):
        image_path = [x['path'] for ok, x in results if ok]
        item["image_path"] = image_path[0]
        return item

