import scrapy
import json

class AmazonSpider(scrapy.Spider):
    name = "amazon"

    def start_requests(self):
        urls = ['https://www.amazon.co.uk/s?k=samsung+phones&rh=n%3A560798%2Cp_89%3ASamsung',]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        phones = response.xpath('//span[contains(@class, "a-size-base-plus a-color-base a-text-normal")]/text()').getall()
        priceWholeNumbers = response.xpath('//span[contains(@class, "a-price-whole")]/text()').getall()
        priceDecimalNumbers = response.xpath('//span[contains(@class, "a-price-fraction")]/text()').getall()
        self.logger.debug(f'phone numbers, {", ".join(phones)}')
        self.logger.debug(f'price whole numbers, {", ".join(priceWholeNumbers)}')
        self.logger.debug(f'price decimal numbers, {", ".join(priceDecimalNumbers)}')

        self.logger.info(json.dumps(list(map(self.formatter, phones, priceWholeNumbers, priceDecimalNumbers))))

    def formatter(self, phones, wholeNumbers, decimalNumbers):
        return {'phones': phones, 'price': wholeNumbers+'.'+decimalNumbers}
