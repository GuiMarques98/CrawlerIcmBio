import scrapy
from bioRes.items import ReservaItem
from scrapy.loader import ItemLoader


class PostsSpider(scrapy.Spider):
    name = "unidade"
    start_urls = ["https://www.icmbio.gov.br/portal/flona-de-urupadi"]
    allowed_domains = ["icmbio.gov.br"]

    def parse(self, response, **kwargs):
        loader = ItemLoader(item=ReservaItem(), selector=response)
        loader.add_value('url_item', response.url)
        loader.add_css(
            'name', '.item-page > table:nth-child(3) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(2) > p:nth-child(2)')
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

        yield loader.load_item()
