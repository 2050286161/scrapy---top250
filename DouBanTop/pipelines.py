# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import sqlite3

from itemadapter import ItemAdapter


class DoubantopPipeline:

    def __init__(self):
        self.conn = sqlite3.connect('.\Data\DouBan.db')
        self.cursor = self.conn.cursor()

    def process_item(self, item, spider):
        print(item)
        MovieName = item['MovieName']
        MovieInfo = item['MovieName']
        Star = item['Star']
        Quote = item['Quote']
        sql = "insert into DouBanInfo(MovieName,MovieInfo,Star,Quote) values ('" + MovieName + "','" + MovieInfo + "','" + Star + "','" + Quote + "')"
        self.cursor.execute(sql)
        self.conn.commit()
        return item

    def __del__(self):
        self.cursor.close()
        self.conn.close()
