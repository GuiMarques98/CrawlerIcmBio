# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ReservaItem(scrapy.Item):
    # define the fields for your item here like:
    # Write field
    name = scrapy.Field()
    url_item = scrapy.Field()
    biome = scrapy.Field()
    size_area = scrapy.Field()
    unity_created_at = scrapy.Field()
    regional_administration = scrapy.Field()
    address = scrapy.Field()
    phones = scrapy.Field()
    site = scrapy.Field()
    endangered_species = scrapy.Field()

    # Downloaded field
    criation_file = scrapy.Field()
    map_limit = scrapy.Field()

    # Last update
    updated_at = scrapy.Field()
