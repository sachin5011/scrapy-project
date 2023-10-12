# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import sqlite3

class TutorialPipeline:
    def __init__(self):
        self.create_connection()
        self.create_table()

    def create_connection(self):
        self.conn = sqlite3.connect("scrapper.db")
        self.cursor = self.conn.cursor()

    def create_table(self):
        self.cursor.execute(""" Drop table if exists quote_tb """)
        self.cursor.execute("""
            create table quote_tb(
                quote text,
                author text,
                tags text
            )
        """)

    def store_to_db(self, items):
        self.cursor.execute(""" insert into quote_tb values( ?, ?, ?) """,
                            (items["quote"][0], items["author"][0], items["tags"][0]))
        self.conn.commit()

    def process_item(self, item, spider):
        self.store_to_db(item)
        return item



