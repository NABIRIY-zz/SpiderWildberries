import scrapy
import getters as get


class Spudi(scrapy.Spider):
    name = "spudi"
    base_url = 'https://www.wildberries.ru/catalog/obuv/zhenskaya/sabo-i-myuli/myuli?page=%s'
    start_urls = [base_url % 1]

    def parse(self, response):
        k = 0
        page = 3
        for i in response.css('div.dtList'):
            yield {
                # '': i.css('').extract_first(),
                'timestamp': None,
                'RPC': i.css('div::attr(id)').extract_first(),
                'url': i.css('a::attr(href)').extract_first(),
                'title': i.css('span.goods-name::text').extract_first(),
                'marketing_tags': None,
                'brand': i.css('strong.brand-name::text').extract_first(),
                'selection': response.css('div.breadcrumbs span::text').extract(),
                'price_data':
                {
                    'current': get.CurrentPrice(i),
                    'original': get.OriginalPrice(i),
                    'sale_tag': get.Sale(i),
                },

                'stock':
                {
                    'in_stock': get.Size(i),
                },
                'assets':
                {
                    'main_image': i.css('img.thumbnail::attr(src)').extract_first(),
                    'set_images': None,
                },
                'metadata':
                {
                    '__description': None,
                },
            }
            k += 1
            if k % 100 == 0:
                k = 0
                page += 1
                yield scrapy.Request(self.base_url % page)
