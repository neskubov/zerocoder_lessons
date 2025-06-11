# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import sqlite3

class DivanparswritetossqllitePipeline:

    def __init__(self):
        self.connection = sqlite3.connect('scrapy_data.db')
        self.cursor = self.connection.cursor()

        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS items (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT,
                price TEXT,
                url TEXT
            )
        """)
        self.connection.commit()

    def process_item(self, item, spider):
        self.cursor.execute("""
            INSERT INTO items (title, price, url) VALUES (?, ?, ?)
        """, (item['title'], item['price'], item['url']))
        self.connection.commit()
        return item

    def close_spider(self, spider):
        # Закрытие соединения с базой данных
        self.connection.close()
