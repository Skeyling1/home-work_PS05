# написать spider для нахождения всех источников освещения с сайта divan.ru
# # Нужно взять название источника освещения, цену и ссылку
# # *Можно попробовать сделать это на другом сайте с продажей источников освещения

import scrapy


class DivannewparsSpider(scrapy.Spider):
    name = "divannewpars"
    allowed_domains = ["https://divan.ru"]
    start_urls = ["https://www.divan.ru/syktyvkar/category/svet"]

    def parse(self, response):
        lamps = response.css('div.WdR1o')
        for lamp in lamps:
            yield {
                'name': lamp.css('span').attrib['name'],
                'price': lamp.css('div.pY3d2 span::text').get(),
                'url': lamp.css('a').attrib['href']
            }




