# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.pipelines.images  import ImagesPipeline
from scrapy import Request
import re


pattern = re.compile(r"/\w/(.*)")

class DmzjPipeline(ImagesPipeline):

    def get_media_requests(self, item, info):
        for url in item["image_urls"]:
            yield Request(url,
                          headers={"Referer": item["referer"]})

    def file_path(self, request, response=None, info=None):
        from urllib import unquote
        url = unquote(request.url)
        matched = pattern.search(url)
        if matched:
            return "full/" + matched.group(1)
        else:
            return "full/" + url.split("/")[-1]
