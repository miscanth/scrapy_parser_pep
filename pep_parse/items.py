# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class PepParseItem(scrapy.Item):
    number = scrapy.Field()
    name = scrapy.Field()
    status = scrapy.Field()

    """def __init__(self):
        super().__init__()
        self.fields['Номер'] = scrapy.Field()
        self.fields['Название'] = scrapy.Field()
        self.fields['Статус'] = scrapy.Field()"""
