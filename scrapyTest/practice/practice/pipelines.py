# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
from pymysql import cursors
from twisted.enterprise import adbapi


class PracticeTenCentPipeline(object):
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
        # 把要执行的sql放入连接池
        query = self.db_pool.runInteraction(self.insert_into, item)
        # 如果sql执行发送错误,自动回调addErrBack()函数
        query.addErrback(self.handle_error, item, spider)
        return item

    # 处理sql函数
    def insert_into(self, cursor, item):
        # 创建sql语句
        sql = """
        INSERT INTO tencent(RecruitPostName, PostId, RecruitPostId, CountryName, LocationName, BGName,
        ProductName, CategoryName, Responsibility, LastUpdateTime, PostURL, SourceID, IsCollect, IsValid)
        VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        # 执行sql语句
        cursor.execute(sql, (item['RecruitPostName'], item['PostId'], item['RecruitPostId'], item['CountryName'],
                             item['LocationName'], item['BGName'], item['ProductName'], item['CategoryName'],
                             item['Responsibility'], item['LastUpdateTime'], item['PostURL'], item['SourceID'],
                             item['IsCollect'], item['IsValid']))

    # 错误函数
    def handle_error(self, failure, item, spider):
        print("failure", failure)

