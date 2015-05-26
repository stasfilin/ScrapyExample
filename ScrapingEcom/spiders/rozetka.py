# -*- coding: utf-8 -*-
import scrapy
from ScrapingEcom.items import RozetkaItem

class RozetkaSpider(scrapy.Spider):

    name = "rozetka"
    allowed_domains = ["rozetka.com.ua"]

    def __init__(self, url=None, start=1, end=50, *args, **kwargs):
        super(RozetkaSpider, self).__init__(*args, **kwargs)
        self.start_urls = [url+'page=%s/' % page for page in xrange(int(start), int(end)+1)]

    def parse(self, response):
        items = []
        for item in response.xpath('//div[@class="g-i-tile-i-150-image"]/a'):
            href = item.xpath('@href').extract()
            title = item.xpath('img/@alt').extract()
            if href[0] != '#':
                base = RozetkaItem()
                base['title'] = title[0]
                base['link'] = href[0]
                items.append(base)
        return items