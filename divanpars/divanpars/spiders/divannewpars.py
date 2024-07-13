# написать spider для нахождения всех источников освещения с сайта divan.ru
# # Нужно взять название источника освещения, цену и ссылку
# # *Можно попробовать сделать это на другом сайте с продажей источников освещения

import scrapy


class DivannewparsSpider(scrapy.Spider):
    name = "divannewpars"
    allowed_domains = ["https://divan.ru"]
    start_urls = ["https://www.divan.ru/category/svet"]

    def parse(self, response):
        pass
