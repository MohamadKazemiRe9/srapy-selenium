# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader.processors import TakeFirst


class LivecoinItem(scrapy.Item):
    name = scrapy.Field(
        output_processor = TakeFirst()
    )
    valume = scrapy.Field(
        output_processor = TakeFirst()
    )
    last_price = scrapy.Field(
        output_processor = TakeFirst()
    )