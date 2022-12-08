import scrapy


class CountrySpider(scrapy.Spider):
    name = 'country'
    allowed_domains = ['www.countries-ofthe-world.com']
    start_urls = ['https://www.countries-ofthe-world.com/flags-of-the-world.html']

    def parse(self, response):

        rows = response.xpath('//div[@class="container"]')

        for row in rows:
            country_name = row.xpath('//td[2]/text()').getall()
            country_flag = row.xpath('//td[1]//img/@src').getall()

            yield {
                'Country Name': country_name,
                'Country Flag': country_flag,
        }



