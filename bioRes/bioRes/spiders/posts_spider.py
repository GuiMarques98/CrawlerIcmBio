import scrapy
from bioRes.items import ReservaItem
from scrapy.loader import ItemLoader


class PostsSpider(scrapy.Spider):
    name = "posts"
    start_urls = ["https://www.icmbio.gov.br/portal/unidades-de-conservacao"]
    allowed_domains = ["icmbio.gov.br"]

    def parse(self, response, **kwargs):

        for un_con in response.css('.search-results li'):
            un_page = "https://www.icmbio.gov.br%s" % un_con.css(
                '.result-title a::attr(href)').get()

            yield scrapy.Request(un_page, callback=self.parsing_unidades)

        next_page = "https://www.icmbio.gov.br%s" % response.css(
            '.pagination-next a::attr(href)').get()
        is_next_page_ok = response.css('.pagination-next a::attr(href)').get()
        if is_next_page_ok is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)

    def parsing_unidades(self, response, **kwargs):
        loader = ItemLoader(item=ReservaItem(), selector=response)
        loader.add_value('name', response.meta['title'])
        loader.add_value('url_item', response.meta['url'])
        loader.add_css(
            'biome', '.item-page > table:nth-child(3) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(2) > p:nth-child(3)::text')
        loader.add_css(
            'size_area', '.item-page > table:nth-child(3) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(2) > p:nth-child(4)::text')
        loader.add_css(
            'unity_created_at', '.item-page > table:nth-child(3) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(2) > p:nth-child(5)::text')

        detail = response.xpath(
            '/html/body/div[2]/main/div/div/div/section/div/div[1]/table/tbody/tr[1]/td[2]/p[5]/text()').extract()
        loader.add_value('regional_administration', detail[0])
        loader.add_value('address', detail[1])
        loader.add_value('phones', detail[2])


        return loader.load_item()
