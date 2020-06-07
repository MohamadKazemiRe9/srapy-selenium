import scrapy
import time
from scrapy.selector import Selector
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from shutil import which
from scrapy.loader import ItemLoader
import datetime
from ..items import LivecoinItem


class CoinSpider(scrapy.Spider):
    name = 'coin'
    allowed_domains = ['https://www.livecoin.net']
    start_urls = ['https://www.livecoin.net/en/']

    def parse(self, response):
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_path = which('chromedriver')
        driver = webdriver.Chrome(executable_path=chrome_path,options=chrome_options)
        driver.get("https://www.livecoin.net/en/")

        html = driver.page_source

        res = Selector(text=html)

        for item in res.xpath("//div[contains(@class, 'ReactVirtualized__Table__row tableRow___3EtiS')]"):
            loader = ItemLoader(item=LivecoinItem(),selector=item,response=response)
            loader.add_xpath("name",".//div[1]/div/text()")
            loader.add_xpath("valume",".//div[2]/span/text()")
            loader.add_xpath("last_price",".//div[3]/span/text()")

            yield loader.load_item()