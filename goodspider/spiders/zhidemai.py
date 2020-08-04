import scrapy
import json

class ZhidemaiSpider(scrapy.Spider):
    name = "zhidemai"
    allowed_domains = ["smzdm.com", "http://smzdm.com", "www.smzdm.com"]
    start_urls = [
            "https://www.smzdm.com/homepage/headline",
            "https://www.smzdm.com/fenlei/yundonghuwai/",
            "https://baidu.com",
            "https://google.com",
            "zhangchen"
            ]

    def parse(self, response):
        result = json.loads(response.body)
