import scrapy


class AudibleSpider(scrapy.Spider):
    name = 'audible'
    allowed_domains = ['www.audible.com']
    start_urls = ['https://www.audible.com/search']

    def parse(self, response):
        product_container = response.css('div.adbl-impression-container > div >span>ul>li')

        for product in product_container:
            book_title = product.css('li span.bc-text.bc-size-base.bc-color-secondary::text').getall()
            author_book = product.css(' li.bc-list-item.authorLabel > span > a::text').getall()

            yield {
                'Title': book_title,
                'Author': author_book,
            }

