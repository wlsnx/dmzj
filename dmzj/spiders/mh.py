# -*- coding: utf-8 -*-
import scrapy
from scrapy.contrib.linkextractors import LinkExtractor
from .filter_url import parse
from dmzj.items import DmzjItem
from itertools import chain


class MhSpider(scrapy.Spider):
    name = "mh"
    allowed_domains = ["manhua.dmzj.com"]


    def __init__(self, url=None, kw=None, *args, **kwargs):
        self.kw = kw
        self.start_urls = [url, ]
        super(MhSpider, self).__init__(*args, **kwargs)

    def parse(self, response):
        for url in chain(response.xpath("//div[@class='cartoon_online_border']/ul/li/a/@href").extract(), response.xpath("//div[@class='cartoon_online_border_other']/ul/li/a/@href").extract()):
            yield scrapy.Request("http://manhua.dmzj.com" + url,
                                 callback=self.parse_manga_page)

    def parse_manga_page(self, response):
        img_list = parse(response.body)
        img_list = ["http://images.dmzj.com/" + url for url in img_list]
        return DmzjItem(image_urls=img_list,
                        referer=response.url)


